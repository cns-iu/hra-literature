import pandas as pd
import json
import urllib.parse

def read_json(file):
    with open(file, 'r') as in_file:
        data = json.load(in_file)
        return pd.DataFrame(data)

#Import datasets
publication_metadata = read_json('data/publiccation_metadata.json')
experts_metadata = read_json('data/authors_metadata.json')
institutions_metadata = read_json('data/institutions_metadata.json')
fundings_metadata = read_json('data/fundings_metadata.json')
funder_metadata = pd.read_csv('data/funder_metadata.csv')
dataset_metadata = pd.read_csv('data/dataset_metadata.csv')
organ_metadata = pd.read_csv('data/organ_metadata.csv')
donor_metadata = pd.read_csv('data/donor_metadata.csv')


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

        # Establish relationships in JSON-LD structure
        if entity_type == 'Publication':
            node["@id"] = f"{entity_type}/{row[id_field]}"
            node['hasOrgan'] = [f"Organ/{organ}" for organ in row['organs'] if organ != '']
            node['hasAuthor'] = [f"Author/{author_id}" for author_id in row['author_ids'] if author_id != '']
            node['hasFunding'] = [f"Funding/{grant_id}" for grant_id in row['grant_ids'] if grant_id != '']

        if entity_type == 'Author':
            node["@id"] = f"{entity_type}/{row[id_field]}"
            node['belongsToInstitution'] = [f"Institution/{institution_id[0]}" for institution_id in
                                              row["institution_ids"] if institution_id != '']
        if entity_type == 'Funding':
            node["@id"] = f"{entity_type}/{row[id_field]}"
            node['hasFunder'] =  [f"Organ/{funder_id}" for funder_id in row['funder_ids'] if funder_id != '']

        jsonld_nodes.append(node)
    return jsonld_nodes

# Create JSON-LD nodes for each entity
publications_nodes = create_jsonld_nodes(publication_metadata, "Publication", "pmid", "article_title")
authors_nodes = create_jsonld_nodes(experts_metadata, "Author", "author_id", "full_name")
institutions_nodes = create_jsonld_nodes(institutions_metadata, "Institution", "institution_id", "institution_name")
fundings_nodes = create_jsonld_nodes(fundings_metadata, "Funding", "grant_id")
datasets_nodes = create_jsonld_nodes(dataset_metadata, "Dataset", "dataset_id")
donors_nodes = create_jsonld_nodes(donor_metadata, "Donor", "donor_id")
organs_nodes = create_jsonld_nodes(organ_metadata, "Organ", "organ_ontology", "organ")
funders_nodes = create_jsonld_nodes(funder_metadata, "Funder", "agency", "agency")

print("Finished reading data")

# Link datasets to publications, donors, and organs
for dataset in datasets_nodes:
    dataset_id = dataset['identifier']
    linked_publication = dataset_metadata.loc[
        dataset_metadata['dataset_id'] == dataset_id, 'publication_doi'].dropna().unique()
    linked_donor = dataset_metadata.loc[dataset_metadata['dataset_id'] == dataset_id, 'donor_id'].dropna().unique()
    linked_organ = dataset_metadata.loc[
        dataset_metadata['dataset_id'] == dataset_id, 'organ_ontology'].dropna().unique()
    dataset['linkedToPublication'] = []
    if len(linked_publication) > 0:
        dataset['linkedToPublication'] = normalize_id(f"Publication/{linked_publication[0]}")
    dataset['hasDonor'] = []
    if len(linked_donor) > 0:
        dataset['hasDonor'] = normalize_id(f"Donor/{linked_donor[0]}")
    dataset['hasOrgan'] = []
    if len(linked_organ) > 0:
        dataset['hasOrgan'] = normalize_id(f"Organ/{linked_organ[0]}")


# Combine all nodes into a single JSON-LD structure
jsonld_data = publications_nodes + authors_nodes + institutions_nodes + fundings_nodes + funders_nodes + datasets_nodes + donors_nodes + organs_nodes
jsonld_data[:5]  # Display the first 5 nodes for review

# Embed the generated data directly within the JSON-LD document's @graph
document["@graph"] = jsonld_data

# Convert the JSON-LD data structure with context to a string
jsonld_str_with_context = json.dumps(document, indent=2)

# Save the string to a JSON-LD file
with open("data/hra-lit.jsonld", "w") as jsonld_file:
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
nodes_filepath = "data/nodes.csv"
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
edges_filepath = "data/edges.csv"
edges_df.to_csv(edges_filepath, index=False)
