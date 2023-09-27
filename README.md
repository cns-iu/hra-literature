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
- **CSV Tables**: If you prefer to work with CSV files, we've provided individual CSVs for each table in the HRAlit database. You can find them in [data/db/csv](data/db/csv)
### Restore the Database from the Dump:
```psql -U [your-username] -d [your-database-name] < hralit.sql```

## Running Reports
### Summary statistics


### Application 1 : Providing Data Evidence for the HRA


### Application 2 : Identify HRA Reviewers



### Application 3 : Identify HRA Reviewers



## Development


## Credits
This hralit dataset is developed by the [Cyberinfrastructure for Network Science Center at Indiana University](https://cns.iu.edu/). It is funded by NIH Award OT2OD033756 and OT2OD026671.