# HRA Literature
Welcome to the HRA Literature GitHub repository. This repository contains the supporting code and data for the paper that documents the compilation of the HRAlit dataset.

## Introduction
This repository provides the supporting code and data for "Publication, Funding, and Experimental Data in Support of Human Reference Atlas Construction and Usage" paper, detailing the assembly of the HRAlit dataset — a comprehensive compilation linking HRA data to various entities like experts, publications, and ontologies. Our aim is to facilitate a deeper exploration of HRA trends, from identifying leading experts and major publications to understanding funding patterns and alignment with existing ontologies.

## Quick Start
### Requirements:
- **PostgreSQL**: Ensure you have PostgreSQL installed on your system.
- **PSQL CLI**: The command-line interface (CLI) application for PostgreSQL should also be installed.
### Download dataset
- **SQL Database**: To access the HRAlit database using SQL, you can use the provided SQL file: [hralit.sql](data/db/hralit.sql)
- **CSV Tables**: If you prefer to work with CSV files, we've provided individual CSVs for each table in the HRAlit database. 
### Restore the Database from the Dump:
```psql -U [your-username] -d [your-database-name] < hralit.sql```

## Running Reports
### Summary statistics
[This section](application/app0) is for the summary statistic of HRAlit database, including linkage counts, node counts, publication comparison among ASCT+B table, CellMarker, and CZ CELLxGENE.

### Providing Data Evidence for the HRA
[This section](application/app1) is for providing expert, publication, and experimental data evidence for the HRA.
- **Statistic**: The total number of publications, citations, experts, Avg. h-index, funded projects, funders, datasets, cells for 31 organ.
- **Visualization**: Visualizations for these statistics.

### Comparison with different datasets
[This section](application/app2) is for comparing the publications among ASCT+B table, CellMarker, and CZ CELLxGENE.

### Prioritize Atlas Contruction
[This section](application/app3) is for computing the types of DOs and HRAlit data types per organ to help prioritize HRA construction. 

### HRA diversity
[This section](application/app4) is for analyzing the diversity and inclusiveness of HRA survey, HRA experts, general publication authors, and donor metadata.
- **Predicting Gender**: uses [gender_guesser](https://pypi.org/project/gender-guesser/) package to determine gender based on the first name.
- **Predicting Race**: uses [ethnicolr](https://github.com/appeler/ethnicolr) package to determine race based on the first name and last name.

## Development
### Extract data
- [**Experimental data**](extract/experimental-data) : Extract the CellMarker, CZ CELLxGENE, HRA digital objects, HuBMAP data.
- **Experts**:
- **Funder**:
- **Funding**:
- **Institution**:
- **Ontology**:
- **Publication**:


### Build database



## Credits
This hralit dataset is developed by the [Cyberinfrastructure for Network Science Center at Indiana University](https://cns.iu.edu/). It is funded by NIH Award OT2OD033756 and OT2OD026671.