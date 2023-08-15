import pandas as pd
import json
import urllib.parse

#Import datasets
publication_metadata = pd.read_csv('publication_metadata.csv', nrows=1000) # Added nrows as pd.merge method below runs out of memory
institutions_metadata = pd.read_csv('institution_metadata.csv')
fundings_metadata = pd.read_csv('funding_metadata.csv', nrows=1000)
funder_metadata = pd.read_csv('funder_metadata.csv', nrows=1000)
experts_metadata = pd.read_csv('expert_metadata.csv', nrows=1000)
dataset_metadata = pd.read_csv('dataset_metadata.csv', nrows=1000)
organ_metadata = pd.read_csv('organ_metadata.csv')
donor_metadata = pd.read_csv('donor_metadata.csv')


# Create unique ID for institutions
institutions_metadata['institution_id'] = institutions_metadata['organization'] + "_" + institutions_metadata['suborganization'].fillna("")

# Merge datasets to establish relationships
publications_authors = pd.merge(publication_metadata, experts_metadata, on='author_id', how='left')
publications_authors_fundings = pd.merge(publications_authors, fundings_metadata, on='grant_id', how='left')
authors_institutions = pd.merge(experts_metadata, institutions_metadata, on=['organization', 'suborganization'], how='left')


# Get the @context for the JSON-LD document that becomes the base document
document = json.load(open('context.jsonld'))

def normalize_id(id):
    return '#' + urllib.parse.quote_plus(id.lower(), safe='')

def create_jsonld_nodes(df, entity_type, id_field, name_field=None):
    jsonld_nodes = []
    for idx, row in df.iterrows():
        node = {
            "@id": normalize_id(f"{entity_type}/{row[id_field]}"),
            "@type": entity_type,
            "identifier": str(row[id_field]),
            "role": entity_type
        }
        if name_field:
            node["name"] = str(row[name_field])
        jsonld_nodes.append(node)
    return jsonld_nodes

# Create JSON-LD nodes for each entity
publications_nodes = create_jsonld_nodes(publication_metadata, "Publication", "pmid", "article_title")
authors_nodes = create_jsonld_nodes(experts_metadata, "Author", "author_id", "full_name")
institutions_nodes = create_jsonld_nodes(institutions_metadata, "Institution", "institution_id", "organization")
fundings_nodes = create_jsonld_nodes(fundings_metadata, "Funding", "grant_id", "agency")
datasets_nodes = create_jsonld_nodes(dataset_metadata, "Dataset", "dataset_id")
donors_nodes = create_jsonld_nodes(donor_metadata, "Donor", "donor_id")
organs_nodes = create_jsonld_nodes(organ_metadata, "Organ", "organ_ontology", "organ")


# Establish relationships in JSON-LD structure

for pub in publications_nodes:
    pmid = pub['identifier']
    linked_authors = publications_authors_fundings.loc[
        publications_authors_fundings['pmid'] == int(pmid), 'author_id'].dropna().unique()
    linked_fundings = publications_authors_fundings.loc[
        publications_authors_fundings['pmid'] == int(pmid), 'grant_id'].dropna().unique()

    if len(linked_authors) > 0:
        pub['hasAuthor'] = [normalize_id(f"Author/{author_id}") for author_id in linked_authors]

    if len(linked_fundings) > 0:
        pub['hasFunding'] = [normalize_id(f"Funding/{grant_id}") for grant_id in linked_fundings]

# Link authors to institutions
for author in authors_nodes:
    author_id = author['identifier']
    linked_institution = authors_institutions.loc[
        authors_institutions['author_id'] == author_id, 'institution_id'].dropna().unique()

    if len(linked_institution) > 0:
        author['belongsToInstitution'] = normalize_id(f"Institution/{linked_institution[0]}")

# Link datasets to publications, donors, and organs
for dataset in datasets_nodes:
    dataset_id = dataset['identifier']
    linked_publication = dataset_metadata.loc[
        dataset_metadata['dataset_id'] == dataset_id, 'publication_doi'].dropna().unique()
    linked_donor = dataset_metadata.loc[dataset_metadata['dataset_id'] == dataset_id, 'donor_id'].dropna().unique()
    linked_organ = dataset_metadata.loc[
        dataset_metadata['dataset_id'] == dataset_id, 'organ_ontology'].dropna().unique()

    if len(linked_publication) > 0:
        dataset['linkedToPublication'] = normalize_id(f"Publication/{linked_publication[0]}")

    if len(linked_donor) > 0:
        dataset['hasDonor'] = normalize_id(f"Donor/{linked_donor[0]}")

    if len(linked_organ) > 0:
        dataset['hasOrgan'] = normalize_id(f"Organ/{linked_organ[0]}")

# Since the relationship between fundings and funders is directly based on the 'agency' column, it's already established in the initial nodes.


# Combine all nodes into a single JSON-LD structure
jsonld_data = publications_nodes + authors_nodes + institutions_nodes + fundings_nodes + datasets_nodes + donors_nodes + organs_nodes
jsonld_data[:5]  # Display the first 5 nodes for review

# Embed the generated data directly within the JSON-LD document's @graph
document["@graph"] = jsonld_data

# Convert the JSON-LD data structure with context to a string
jsonld_str_with_context = json.dumps(document, indent=2)

# Save the string to a JSON-LD file
with open("hra-lit.jsonld", "w") as jsonld_file:
    jsonld_file.write(jsonld_str_with_context)

print("Wrote hra-lit.jsonld")

# Create nodes and edges files
nodes_data=[]
edges_data=[]
# Add nodes for each entity
for pub in publications_nodes:
    nodes_data.append({"id": pub["@id"], "type": "Publication", "name": pub.get("name", None)})

for author in authors_nodes:
    nodes_data.append({"id": author["@id"], "type": "Author", "name": author.get("name", None)})

for inst in institutions_nodes:
    nodes_data.append({"id": inst["@id"], "type": "Institution", "name": inst.get("name", None)})

for funding in fundings_nodes:
    nodes_data.append({"id": funding["@id"], "type": "Funding", "name": funding.get("name", None)})

for dataset in datasets_nodes:
    nodes_data.append({"id": dataset["@id"], "type": "Dataset", "name": None})

for donor in donors_nodes:
    nodes_data.append({"id": donor["@id"], "type": "Donor", "name": None})

for organ in organs_nodes:
    nodes_data.append({"id": organ["@id"], "type": "Organ", "name": organ.get("name", None)})

nodes_df = pd.DataFrame(nodes_data)
nodes_filepath = "nodes.csv"
nodes_df.to_csv(nodes_filepath, index=False)


# Add edges for relationships
for pub in publications_nodes:
    if "hasAuthor" in pub:
        for author in pub["hasAuthor"]:
            edges_data.append({"source": pub["@id"], "target": author, "relationship": "hasAuthor"})
    if "hasFunding" in pub:
        for funding in pub["hasFunding"]:
            edges_data.append({"source": pub["@id"], "target": funding, "relationship": "hasFunding"})

for author in authors_nodes:
    if "belongsToInstitution" in author:
        edges_data.append({"source": author["@id"], "target": author["belongsToInstitution"], "relationship": "belongsToInstitution"})

for dataset in datasets_nodes:
    if "linkedToPublication" in dataset:
        edges_data.append({"source": dataset["@id"], "target": dataset["linkedToPublication"], "relationship": "linkedToPublication"})
    if "hasDonor" in dataset:
        edges_data.append({"source": dataset["@id"], "target": dataset["hasDonor"], "relationship": "hasDonor"})
    if "hasOrgan" in dataset:
        edges_data.append({"source": dataset["@id"], "target": dataset["hasOrgan"], "relationship": "hasOrgan"})

edges_df = pd.DataFrame(edges_data)
edges_filepath = "edges.csv"
edges_df.to_csv(edges_filepath, index=False)
