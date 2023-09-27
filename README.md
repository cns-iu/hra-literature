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
This section is for extracting data in different types sourced from different datasets.
- [**Experimental data**](extract/experimental-data): Extract the CellMarker, CZ CELLxGENE, HRA digital objects, HuBMAP data. Merge data from these four sources, and output the dataset metadata and donor metadata.
    - CellMarker: Human cell markers via [CellMarker](http://xteam.xbio.top/CellMarker/index.jsp) portal. 
    - CZ CELLxGENE: Datasets for Healthy human adult are extracted via [CELLxGENE Census](https://chanzuckerberg.github.io/cellxgene-census/index.html) API, including datasets and donors.
    - HRA: Digital objects are selected from [HRA metadata across five versions](data/hra-v1.4-metadata.json).
    - HuBMAP: Datasets and donors are extracted via [Smart API](https://smart-api.info/ui/0065e419668f3336a40d1f5ab89c6ba3). 
- [**Ontology**](extract/ontology): Extract the ontology terms in 5th release ASCT+B tables through [CCF-ASCTB-ALL data](data/ontology/ccf-asctb-all.json), including anatomical structures (AS), cell types (CT), biomarkers (B), and their linkages.
    - AS, CT, B: Etract the id, rdfs_label, and name.
    - Linkages: Tag ```part_of ``` for ASs, ```located_in``` for ASs and CTs, ```is_a``` for CTs, ```characterizes``` for CTs and Bs.
- [**Publication**](extract/publication): Extract the HRA references and PubMed publications associated with [31 organs in 5th release HRA](data/experimental/organ.csv), and calculated citation using WoS data.
    - HRA references: Extract the general references and spetific referencs in 5th release ASCT+B tables through [CCF-ASCTB-ALL data](data/ontology/ccf-asctb-all.json).
    - PubMed: Retrieve the PubMed publications where the titles or MeSH terms contain any of the 31 organ names. 
    - Web of Science: Using WoS data linked by WoS IDs to PMIDs, count publication citations, which refers to the number of paper citing a publication.
- [**Experts**](extract/experts):  From PubMed data, extract the authors associated with the selected PubMed publications. Additionaly, extract the HRA experts across all versions, including creators and reviewers.
    - HRA experts: Extract the creators and reviewers from [HRA metadata across five versions](data/hra-v1.4-metadata.json), including ORCIDs, author names, associated digital objects. 
    - Authors: Extract the authors with ORCIDs associated with the selected publications, and query the informations for authors. Then calculate authors' h-indexes based on the citation data from WoS data.
- [**Funding**](extract/funding): From PubMed data, extract the funding data associated with the selected PubMed publications (in database section). Additionaly, extract additional funded project data sourced from six agencies, inlcuding Australian Research Data Commons (ARDC) , the Canadian Institutes of Health Research (CIHR) , European Commission (EC) , Grants-in-Aid for Scientific Research (KAKEN), National Institutes of Health (NIH), and National Science Foundation (NSF).
    - ARDC: Extract funding data using the [ARDC API](https://archive-intranet.ardc.edu.au/display/DOC/Research+Activities+API) by searching with the 31 organ names as keywords.
    - CIHR: Extract funding data from [CIHR portal](https://open.canada.ca/data/dataset/) from 2000 to 2021 year. 
    - EC: Extract funding data from [CIHR portal](https://open.canada.ca/data/dataset/) under the Framework (from FP1 to FP7, h2000, horizon) Programme of the European Union.
    - KAKEN: Extract funding data using the [KAKEN API](https://support.nii.ac.jp/en/kaken/api/api_outline) by searching with the 31 organ names as keywords.
    - NIH: Extract funding data using the [NIH API](https://api.reporter.nih.gov/) by searching fiscal_years from 1985 to 2023.
    - NSF: Extract funding data using the [NSF API](https://resources.research.gov/common/webapi/awardapisearch-v1.htm) by searching with the 31 organ names as keywords.
    - Merge: Extract the data schema of each dataset, and mapping by [manual mapping table](data/funding/mapping_table.csv), extract the additional funding metadata.
- [**Funder**](extract/funder): Extract the funder metadata and the linkage among publictions, funded projects, and funders from [OpenAlex](https://docs.openalex.org/api-entities/funders).
- [**Institution**](extract/institutions): Extract the institution metadata and the linkage among authors and institutions from [OpenAlex](https://docs.openalex.org/api-entities/institutions).


### Build database
This section is for HRAlit database construction using PostgreSQL.
- **Create tables**: Create 23 tables for HRAlit database.
- **Load data**: Load data into 23 tables from the output of the ```extract``` section.
    - Experimental data: Load experimental data and ontology from the output of the section to HRAlit database.
    - Publication data: Select publication data associated with 31 organs, references associated with ASCT+B tables, publications associated with CellMarker, GTEx, or CellMarker, and then add them to ```hrait_publication``` table.
    - Publication - Authors: Import the linkages between seleted publications and authors to ```hralit_publication_author``` table.
    - Authors: Import the metadata of seleted authors to ```hralit_author``` table, as well as the HRA experts.
    - Authors - Institutions: Link the seleted authors with institution data in OpenAlex, and import into ```hralit_author_institution``` table.
    - Institutions: Import the metadata of seleted institution sourced from OpenAlex into ```hralit_institution``` table.
    - Publications - Funding: Import the linkage of publications and funding id sourced from PubMed into ```hralit_funding``` table.
    - Publications - Funding - Funder: Link the seleted publications and funding IDs with the funders. Additionally, connect them to the cleaned funders sourced from OpenAlex using the same PMIDs and funding IDs. Then import the results into the ```hralit_pub_funding_funder``` table.
- **Diagram**: Use [```schemaspy```](https://schemaspy.org/) to output diagram of HRAlit database.
- **Export database**: Export HRAlit database in SQL format, and the 23 tables within the HRAlit database in CSV format.

## Credits
This hralit dataset is developed by the [Cyberinfrastructure for Network Science Center at Indiana University](https://cns.iu.edu/). It is funded by NIH Award OT2OD033756 and OT2OD026671.