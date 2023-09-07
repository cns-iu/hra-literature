import json
import csv

# File path for the input JSON file
file_path = 'data/ontology/ccf-asctb-all.json'

# Reading the JSON file
with open(file_path, 'r') as file:
    data = json.load(file)

# extract anatomical_structures
with open('data/ontology/anatomical_structures.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(['id', 'rdfs_label', 'name'])

    # Iterating through the organ names (e.g., 'blood')
    for organ_name, organ_data in data.items():
        # Iterating through the data and extracting the required attributes
        for entry in organ_data['data']:
            for anatomical_structure in entry['anatomical_structures']:
                writer.writerow(
                    [anatomical_structure['id'], anatomical_structure['rdfs_label'], anatomical_structure['name']])
                

# extract cell_types
with open('data/ontology/cell_types.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(['id', 'rdfs_label', 'name'])

    # Iterating through the organ names (e.g., 'blood')
    for organ_name, organ_data in data.items():
        # Iterating through the data and extracting the required attributes
        for entry in organ_data['data']:
            for cell_types in entry['cell_types']:
                writer.writerow(
                    [cell_types['id'], cell_types['rdfs_label'], cell_types['name']])


# extract biomarkers
with open('data/ontology/biomarkers.csv', mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(['id', 'rdfs_label', 'name', 'b_type'])

    # Iterating through the organ names (e.g., 'blood')
    for organ_name, organ_data in data.items():
        # Iterating through the data and extracting the required attributes
        for entry in organ_data['data']:
            for biomarkers in entry['biomarkers']:
                writer.writerow(
                    [biomarkers['id'], biomarkers['rdfs_label'], biomarkers['name'], biomarkers['b_type']])

# extract biomarkers_protein
with open('data/ontology/biomarkers_protein.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(['id', 'rdfs_label', 'name', 'proteinPresence', 'b_type'])

    # Iterating through the organ names (e.g., 'blood')
    for organ_name, organ_data in data.items():
        # Iterating through the data and extracting the required attributes
        for entry in organ_data['data']:
            for biomarkers in entry['biomarkers_protein']:
                writer.writerow(
                    [biomarkers['id'], biomarkers['rdfs_label'], biomarkers['name'], biomarkers['proteinPresence'],biomarkers['b_type']])

# extract biomarkers_gene
with open('data/ontology/biomarkers_gene.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(['id', 'rdfs_label', 'name', 'b_type'])

    # Iterating through the organ names (e.g., 'blood')
    for organ_name, organ_data in data.items():
        # Iterating through the data and extracting the required attributes
        for entry in organ_data['data']:
            for biomarkers in entry['biomarkers_gene']:
                writer.writerow(
                    [biomarkers['id'], biomarkers['rdfs_label'], biomarkers['name'], biomarkers['b_type']])

# extract biomarkers_lipids
with open('data/ontology/biomarkers_lipids.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(['id', 'rdfs_label', 'name', 'b_type', 'notes'])

    # Iterating through the organ names (e.g., 'blood')
    for organ_name, organ_data in data.items():
        # Iterating through the data and extracting the required attributes
        for entry in organ_data['data']:
            for biomarkers in entry['biomarkers_lipids']:
                writer.writerow(
                    [biomarkers['id'], biomarkers['rdfs_label'], biomarkers['name'], biomarkers['b_type'], biomarkers['notes'])

# extract biomarkers_meta
with open('data/ontology/biomarkers_meta.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Writing the header
    writer.writerow(['id', 'rdfs_label', 'name', 'b_type'])

    # Iterating through the organ names (e.g., 'blood')
    for organ_name, organ_data in data.items():
        # Iterating through the data and extracting the required attributes
        for entry in organ_data['data']:
            for biomarkers in entry['biomarkers_meta']:
                writer.writerow(
                    [biomarkers['id'], biomarkers['rdfs_label'], biomarkers['name'], biomarkers['b_type'])
