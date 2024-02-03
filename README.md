# Publication, Funding, and Experimental Data in Support of Human Reference Atlas Construction and Usage
Yongxin Kong<sup>1,2, * </sup> and Katy Börner <sup>1,* </sup>

<sup>* </sup>Joint corresponding authors

<sup>1 </sup>Indiana University;   <sup>2 </sup>Sun Yat-sen University

---

Experts from 18 consortia are collaborating on the Human Reference Atlas (HRA) which aims to map the 37 trillion cells in the healthy human body. Information relevant for HRA construction and usage is held by experts, published in scholarly papers, and captured in experimental data. However, these data sources use different metadata schemes and cannot be cross-searched efficiently. This paper documents the compilation of a dataset, called HRAlit, that links the 136 HRA v1.4 digital objects (31 organs with 4,279 anatomical structures, 1,210 cell types, 2,089 biomarkers) to 583,117 experts; 7,103,180 publications; 896,680 funded projects, and 1,816 experimental datasets. The resulting HRAlit has 22 tables with 20,939,937 records including 6 junction tables with 13,170,651 relationships. The HRAlit can be mined to identify leading experts, major papers, funding trends, or alignment with existing ontologies in support of systematic HRA construction and usage. 


## Introduction
This repository provides the supporting code and data for "Publication, Funding, and Experimental Data in Support of Human Reference Atlas Construction and Usage" paper, detailing the assembly of the HRAlit dataset—a comprehensive compilation linking HRA data to various entities like experts, publications, and ontologies. Our aim is to facilitate a deeper exploration of HRA trends, from identifying leading experts and major publications to understanding funding patterns and alignment with existing ontologies.

The repo is structured in the following way:
```
├── extract
├── data
├── database
├── validate
```

## Quick Start
### Requirements
- **Linux System**: Or ensure you have WSL or WSL2 installed on your Windows machine.
- **Python3**: Install Python3 ```sudo apt install python3 python3-pip```
- **PostgreSQL**: Ensure you have at least PostgreSQL version 9.6 installed on your system.
- **PSQL CLI**: The corresponding command-line interface (CLI) application for PostgreSQL should also be installed.
- **Libraries**: Use ```requirements.txt``` to install the required libraries using the command: ```pip install -r requirements.txt```
### Data availablity
- **Data**: The HRAlit database SQL file and all tables in CSV format are at Figshare, https://figshare.com/articles/dataset/24580669.  
- **SQL Database**: To access the HRAlit database using SQL, you can use the provided SQL file: hralit.sql
  - Use the following command to import the database:
  ```psql -U [your-username] -d [your-database-name] < /path/to/hralit.sql```Replace [your-username] with your PostgreSQL username and [your-database-name] with the name of the database you want to import the data into. Make sure to replace /path/to/hralit.sql with the actual path to the hralit.sql file on your local system.
- **CSV Tables**: If you prefer to work with CSV files, we've provided individual CSVs for each table in the HRAlit database. 

### Entity Relationship Diagram

![img](https://github.com/cns-iu/hra-literature/blob/main/data/db/HRAlit-Entity-relationship-diagram.svg)

## Supplementary information
- **Data dictionary of HRAlit database**: Provides details on the [data description](data/db/data-dictionary.xlsx) for each table in the HRAlit database, as well as statistics on the number of [rows](data/db/row-ct.csv), [nodes](data/db/node-ct.csv), and [linkages of relationships](data/db/linkage-ct.csv).

  
## Develop database
### Extract data
Code for extracting data in different types sourced from different datasets.
- [**HRA**]: Extract the HRA data.
  -  Digital objects: Selected from [HRA metadata across five versions](data/hra-v1.4-metadata.json).
  -  Organs: Organize the [31 organs in 5th release HRA](data/experimental/organ.csv).
  -  Anatomical, Cell, and Biomarker: Select AS, CT, and B in 5th HRA (see ontology section), as well as their relationships.
  -  HRA creators and reviewers across five versions (see experts section).
  -  HRA references and reviewers across five versions (see publication section).
- CellMarker: Human cell markers via [CellMarker](http://xteam.xbio.top/CellMarker/index.jsp) portal. 
- [**Experimental data**](extract/experimental-data): Extract the CellMarker, CZ CELLxGENE, HuBMAP data. Merge data through a mapping table [```dataset_mapping.csv```](data/experimental/dataset_mapping.csv) that correlates identifiers across these sources, and output the dataset metadata and donor metadata.
    - CZ CELLxGENE: Datasets for healthy human adults are extracted via [CELLxGENE Census](https://chanzuckerberg.github.io/cellxgene-census/index.html) API, including datasets and donors.
    - HuBMAP: Datasets and donors are extracted via [Smart API](https://smart-api.info/ui/0065e419668f3336a40d1f5ab89c6ba3). 
- [**Ontology**](extract/ontology): Extract the ontology terms in 5th release ASCT+B Tables through [CCF-ASCTB-ALL data](data/ontology/ccf-asctb-all.json), including anatomical structures (AS), cell types (CT), biomarkers (B), and their linkages.
    - AS, CT, B: Extract the id, rdfs_label, and name.
    - Linkages: Tag ```part_of ``` for ASs, ```located_in``` for ASs and CTs, ```is_a``` for CTs, ```characterizes``` for CTs and Bs.
    - Triple：Build the linkage among anatomical structures, cell types, and biomarkers listed in the same row of a ASCT+B Table through assigning a unique identifier called “row_id” to each row
- [**Publication**](extract/publication): Extract the HRA references and PubMed publications associated with [31 organs in 5th release HRA](data/experimental/organ.csv).
    - HRA references: Extract the general references and specific references in 5th release ASCT+B Tables through [CCF-ASCTB-ALL data](data/ontology/ccf-asctb-all.json).
    - PubMed: Retrieve the PubMed publications where the titles or MeSH terms contain any of the 31 organ names. 
    - Web of Science: Using WoS data linked by WoS IDs to PMIDs, only for technical validation.
- [**Experts**](extract/experts):  From PubMed data, extract the authors associated with the selected PubMed publications. Additionally, extract the HRA experts across all versions, including creators and reviewers.
    - HRA experts: Extract the creators and reviewers from [HRA metadata across five versions](data/hra-v1.4-metadata.json), including ORCIDs, author names, associated digital objects. 
    - Authors: Extract the authors with ORCIDs associated with the selected publications, and query the information for authors. 
- [**Funding**](extract/funding): From PubMed data, extract the funding data associated with the selected PubMed publications. 
- [**Funder**](extract/funder): Extract the funder metadata and the linkage among publications, funded projects, and funders from [OpenAlex](https://docs.openalex.org/api-entities/funders).
- [**Institution**](extract/institutions): Extract the institution metadata and the linkage among authors and institutions from [OpenAlex](https://docs.openalex.org/api-entities/institutions).


### Build database
Construct the HRAlit database in PostgreSQL via the following steps:
- **Create tables**: Create 23 tables for HRAlit database.
- **Load data**: Load data into 23 tables from the output of the ```extract``` section.
    - HRA data:
      - Import digital objects from HRA across 5 versions to ```hralit_digital_objects``` table
      - Import organs listed in HRA v1.4 to ```hralit_organ``` table
      - Import creators information listed in HRA across 5 versions to ```hralit_creator``` table
      - Import reviewers information listed in HRA across 5 versions to ```hralit_reviewer``` table
      - Import anatomical structures listed in HRA v1.4 to ```hralit_anatomical_structures``` table
      - Import cell types listed in HRA v1.4 to ```hralit_cell_types``` table
      - Import biomarkers listed in HRA v1.4 to ```hralit_biomarkers``` table
      - Import linkages among anatomical structures, cell types, and biomarkers listed in HRA v1.4 to ```hralit_triple``` table
      - Import specific relationships within the ASCT+B tables in 5th release to ```hralit_asctb_linkage``` table
      - Import general and specific references from ASCT+B Tables in 5th release to ```hralit_asctb_publication``` table
    - Experimental data:
      - Load donor metadata to ```hralit_donor``` table
      - Load dataset metadata to ```hralit_dataset``` table
    - Publication data:
      - Import publications in experimental datasets or CellMarker to ```hralit_other_publication``` table
      - Select publication data associated with 31 organs, and store the linkage between PMIDs and organs to ```hralit_publication_subject``` table
      - Select publication data associated with 31 organs(recorded in "hralit_publication_subject" table), references associated with ASCT+B Tables (recorded in "hralit_asctb_publication" table), publications associated with CellMarker, GTEx, or CellMarker (recorded in "hralit_other_publication" table), and then add them to ```hrait_publication``` table.
    - Publication - Authors: Import the linkages between publications in "hralit_publication" table and associated authors to ```hralit_publication_author``` table.
    - Authors:
      - Query the linkage between ORCIDs and organs to ```hralit_author_expertise``` table by joing "hralit_publication_subject" table and "hralit_publication_author" table.
      - Import the metadata of selected authors to ```hralit_author``` table, as well as the HRA experts.
    - Authors - Institutions: Link the selected authors with institution data in OpenAlex, and import into ```hralit_author_institution``` table.
    - Institutions: Import the metadata of selected institutions sourced from OpenAlex into ```hralit_institution``` table.
    - Publications - Funding: Import the linkage of publications and funding id sourced from PubMed into ```hralit_funding``` table.
    - Publications - Funding - Funder: Link the selected publications and funding IDs with the funders. Additionally, connect them to the cleaned funders sourced from OpenAlex using the same PMIDs and funding IDs. Then import the results into the ```hralit_pub_funding_funder``` table.
    - Funders: Select the cleaned funder metadata from OpenAlex to ```hralit_funder_cleaned``` table by matching the funder ID in the "hralit_pub_funding_funder" table.
- **Diagram**: Use [```schemaspy```](https://schemaspy.org/) to output a diagram of the HRAlit database.
- **Export database**: Export HRAlit database in SQL format, and the 23 tables within the HRAlit database in CSV format.

### Validate database
- **Coverage of publications**: Compare the publications in HRAlit database with those in WoS and OpenAlex.
  - Coverage of HRAlit publications in WoS and OpenAlex databases.
  - Number of papers published per year for the 31 organs.
  - Growth in the number of publications in the HRAlit database over time with linear regression analysis.
- **Coverage of linkages from publication to funding, from publication to author ORCID**: Compare the linkages in HRAlit database with those in WoS and OpenAlex.

## Credits
This HRAlit dataset is developed by the [Cyberinfrastructure for Network Science Center at Indiana University](https://cns.iu.edu/). This research has been funded by the China Scholar Council [YK] and the NIH Common Fund through the Office of Strategic Coordination/Office of the NIH Director under awards OT2OD033756 and OT2OD026671, by the Cellular Senescence Network (SenNet) Consortium through the Consortium Organization and Data Coordinating Center (CODCC) under award number U24CA268108, by the Kidney Precision Medicine Project grant U2CDK114886, by the NIDDK under awards U24DK135157 and U01DK133090 and by The Multiscale Human CIFAR project [KB]. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript. 
