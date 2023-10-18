# Publication, Funding, and Experimental Data in Support of Human Reference Atlas Construction and Usage
Yongxin Kong<sup>1,2, * </sup> and Katy Börner <sup>1,* </sup>

<sup>* </sup>Joint corresponding authors

<sup>1 </sup>Indiana University;   <sup>2 </sup>Sun Yat-sen University

---

Experts from 18 consortia are collaborating on the Human Reference Atlas (HRA) which aims to map the 37 trillion cells in the healthy human body. Information relevant for HRA construction and usage is held by experts (clinicians, pathologists, anatomists, single-cell experts), published in scholarly papers, and captured in experimental data. However, these data sources use different metadata schemes and cannot be cross-searched efficiently. This paper documents the compilation of a dataset, called HRAlit, that links 136 HRA v1.4 digital objects (31 organs with 2,689 anatomical structures, 590 cell types, 1,770 biomarkers) to 583,117 experts; 7,103,180 publications; 896,680 funded projects, and 1,816 experimental datasets. The resulting HRAlit represents 21,704,001 records as a network with 8,694,233 nodes and 14,096,735 links. We demonstrate how HRAlit can be mined to identify leading experts, major papers, funding trends, or alignment with existing ontologies in support of systematic HRA construction and usage.

## Introduction
This repository provides the supporting code and data for "Publication, Funding, and Experimental Data in Support of Human Reference Atlas Construction and Usage" paper, detailing the assembly of the HRAlit dataset—a comprehensive compilation linking HRA data to various entities like experts, publications, and ontologies. Our aim is to facilitate a deeper exploration of HRA trends, from identifying leading experts and major publications to understanding funding patterns and alignment with existing ontologies.

The repo is structured in the following way:
```
├── extract
├── database
├── application
├── data
```

## Quick Start
### Requirements:
- **Linux System**: Or ensure you have WSL or WSL2 installed on your Windows machine.
- **Python3**: Install Python3 ```sudo apt install python3 python3-pip```
- **PostgreSQL**: Ensure you have at least PostgreSQL version 9.6 installed on your system.
- **PSQL CLI**: The corresponding command-line interface (CLI) application for PostgreSQL should also be installed.
- **Libraries**: Use ```requirements.txt``` to install the required libraries using the command: ```pip install -r requirements.txt```
### Download dataset
- **SQL Database**: To access the HRAlit database using SQL, you can use the provided SQL file: [hralit.sql](data/db/hralit.sql)
- **CSV Tables**: If you prefer to work with CSV files, we've provided individual CSVs for each table in the HRAlit database. 
### Restore the Database from the Dump:
```psql -U [your-username] -d [your-database-name] < hralit.sql```
### Entity Relationship Diagram （ERD）
[The Entity Relationship Diagram of HRAlit database](https://dbdiagram.io/d/HRAlit-database-652a4fe1ffbf5169f0abf1a2) is available.

![img](https://github.com/cns-iu/hra-literature/blob/main/data/db/Entity%20Relationship%20Diagram.png?raw=true)

## Running Reports
### Summary statistics
[Code in this direcory](application/app0) generates summary statistics of the HRAlit database, including linkage counts, node counts, and publication comparison for ASCT+B Tables, CellMarker, and CZ CELLxGENE datasets.

### Providing Data Evidence for the HRA
[Code in this direcory](application/app1) is run to provide expert, publication, and experimental data evidence for the HRA.
- **Statistics**: The total number of publications, citations, experts, average _h_-index, funded projects, funders, datasets, and cells for 31 organs.
- **Visualization**: Visualizations of these statistics.

### Comparison with different datasets
[Code in this direcory](application/app2) is run for comparing the publications reported in ASCT+B Tables, CellMarker, and CZ CELLxGENE datasets.

### Prioritize Atlas Construction
[Code in this direcory](application/app3) is run for computing the types of DOs and HRAlit data types per organ to help prioritize HRA construction.

### HRA diversity
[Code in this direcory](application/app4) has code for analyzing the diversity and inclusiveness of HRA survey, HRA experts, general publication authors, and donor metadata.
- **Predicting Gender**: Uses [gender_guesser](https://pypi.org/project/gender-guesser/) package to determine gender based on the first name.
- **Predicting Race**: Uses [ethnicolr](https://github.com/appeler/ethnicolr) package to determine race based on the first name and last name.

## Supplementary information
- [**Mapping for HuBMAP, CxG, and GTEx data**](data/experimental/dataset_mapping.csv): A mapping table that correlates identifiers across HuBMAP, CZ CELLxGENE, and GTEx.
- [**Additional funding metadata**](data/funding/merged_metadata.7z): Provides metadata related to six additional funded projects, including ARDC, CIHR, EC, KAKEN, NIH, and NSF.
- **HRA diversity survey**: Includes [HRA Diversity Survey](data/results/app6/survey/HRA_Diversity_Survey.pdf), [the report of its results](data/results/app6/survey/HRA_Diversity_Results.pdf), and [the results in CSV format](data/results/app6/survey/HRA_survey.csv).
- **HRA expert diversity**: Provides details on [the gender and career age of HRA creators and reviewers](data/expert/experts_meta.csv), as well as [statistics on race](data/results/app6/expert-race.csv).
- **Data dictionary of HRAlit database**: Provides details on the [data description](data/results/app0/data-dictionary.xlsx) for each table in the HRAlit database, as well as statistics on the number of [rows](data/results/app0/row-ct.csv), [nodes](data/results/app0/node-ct.csv), and [linkages of relationships](data/results/app0/linkage-ct.csv).
- **Expert, Literature, and Experimental Data Evidence for HRA**: Provides details on 31 organs, including an [overview](data/results/app1/merged_output.csv), [average citations](data/results/app1/avg-citation.csv), [funding amounts from six additional funders](data/results/app1), [trends in publications over the years](data/results/app1/pub-trend.csv), and [relationships](data/results/app1/relationship.csv).
- **HRA diversity**: Provides details on gender distribution across ages for [surveys](data/results/app6/gender-age-survey.csv), [donors](data/results/app6/gender-age-donor.csv), and the [world population](data/results/app6/gender-age-world-population.csv), as well as [gender distribution in career ages](data/results/app6/gender-in-career-ages.csv), [racial demographics](data/results/app6/race.csv), and [the number of authors by geolocation](data/results/app6/authors-in-geolocation.csv).
  
## Development
### Extract data
Code for extracting data in different types sourced from different datasets.
- [**Experimental data**](extract/experimental-data): Extract the CellMarker, CZ CELLxGENE, HRA digital objects, HuBMAP data. Merge data from these four sources, and output the dataset metadata and donor metadata.
    - CellMarker: Human cell markers via [CellMarker](http://xteam.xbio.top/CellMarker/index.jsp) portal. 
    - CZ CELLxGENE: Datasets for healthy human adults are extracted via [CELLxGENE Census](https://chanzuckerberg.github.io/cellxgene-census/index.html) API, including datasets and donors.
    - HRA: Digital objects are selected from [HRA metadata across five versions](data/hra-v1.4-metadata.json).
    - HuBMAP: Datasets and donors are extracted via [Smart API](https://smart-api.info/ui/0065e419668f3336a40d1f5ab89c6ba3). 
- [**Ontology**](extract/ontology): Extract the ontology terms in 5th release ASCT+B Tables through [CCF-ASCTB-ALL data](data/ontology/ccf-asctb-all.json), including anatomical structures (AS), cell types (CT), biomarkers (B), and their linkages.
    - AS, CT, B: Extract the id, rdfs_label, and name.
    - Linkages: Tag ```part_of ``` for ASs, ```located_in``` for ASs and CTs, ```is_a``` for CTs, ```characterizes``` for CTs and Bs.
- [**Publication**](extract/publication): Extract the HRA references and PubMed publications associated with [31 organs in 5th release HRA](data/experimental/organ.csv), and calculated citation using WoS data.
    - HRA references: Extract the general references and specific references in 5th release ASCT+B Tables through [CCF-ASCTB-ALL data](data/ontology/ccf-asctb-all.json).
    - PubMed: Retrieve the PubMed publications where the titles or MeSH terms contain any of the 31 organ names. 
    - Web of Science: Using WoS data linked by WoS IDs to PMIDs, count publication citations, which refers to the number of papers citing a publication.
- [**Experts**](extract/experts):  From PubMed data, extract the authors associated with the selected PubMed publications. Additionally, extract the HRA experts across all versions, including creators and reviewers.
    - HRA experts: Extract the creators and reviewers from [HRA metadata across five versions](data/hra-v1.4-metadata.json), including ORCIDs, author names, associated digital objects. 
    - Authors: Extract the authors with ORCIDs associated with the selected publications, and query the information for authors. Then calculate authors' _h_-indexes based on the citation data from WoS data.
- [**Funding**](extract/funding): From PubMed data, extract the funding data associated with the selected PubMed publications (in database section). Additionally, extract additional funded project data sourced from six agencies, including Australian Research Data Commons (ARDC), the Canadian Institutes of Health Research (CIHR), European Commission (EC), Grants-in-Aid for Scientific Research (KAKEN), National Institutes of Health (NIH), and National Science Foundation (NSF).
    - ARDC: Extract funding data using the [ARDC API](https://archive-intranet.ardc.edu.au/display/DOC/Research+Activities+API) by using the 31 organ names as search keywords.
    - CIHR: Extract funding data from [CIHR portal](https://open.canada.ca/data/dataset/) from year 2000 to 2021. 
    - EC: Extract funding data from [CIHR portal](https://open.canada.ca/data/dataset/) under the Framework (from FP1 to FP7, h2000, horizon) Programme of the European Union.
    - KAKEN: Extract funding data using the [KAKEN API](https://support.nii.ac.jp/en/kaken/api/api_outline) by using the 31 organ names as search keywords.
    - NIH: Extract funding data using the [NIH API](https://api.reporter.nih.gov/) by searching fiscal_years from 1985 to 2023.
    - NSF: Extract funding data using the [NSF API](https://resources.research.gov/common/webapi/awardapisearch-v1.htm) by using the 31 organ names as search keywords.
    - Merge: Extract the data schema of each dataset, and mapping by [manual mapping table](data/funding/mapping_table.csv), extract the additional funding metadata.
- [**Funder**](extract/funder): Extract the funder metadata and the linkage among publications, funded projects, and funders from [OpenAlex](https://docs.openalex.org/api-entities/funders).
- [**Institution**](extract/institutions): Extract the institution metadata and the linkage among authors and institutions from [OpenAlex](https://docs.openalex.org/api-entities/institutions).


### Build database
Construct the HRAlit database in PostgreSQL via the following steps:
- **Create tables**: Create 23 tables for HRAlit database.
- **Load data**: Load data into 23 tables from the output of the ```extract``` section.
    - Experimental data: Load experimental data and ontology from the output of the section to HRAlit database.
    - Publication data: Select publication data associated with 31 organs, references associated with ASCT+B Tables, publications associated with CellMarker, GTEx, or CellMarker, and then add them to ```hrait_publication``` table.
    - Publication - Authors: Import the linkages between selected publications and authors to ```hralit_publication_author``` table.
    - Authors: Import the metadata of selected authors to ```hralit_author``` table, as well as the HRA experts.
    - Authors - Institutions: Link the selected authors with institution data in OpenAlex, and import into ```hralit_author_institution``` table.
    - Institutions: Import the metadata of selected institutions sourced from OpenAlex into ```hralit_institution``` table.
    - Publications - Funding: Import the linkage of publications and funding id sourced from PubMed into ```hralit_funding``` table.
    - Publications - Funding - Funder: Link the selected publications and funding IDs with the funders. Additionally, connect them to the cleaned funders sourced from OpenAlex using the same PMIDs and funding IDs. Then import the results into the ```hralit_pub_funding_funder``` table.
- **Diagram**: Use [```schemaspy```](https://schemaspy.org/) to output a diagram of the HRAlit database.
- **Export database**: Export HRAlit database in SQL format, and the 23 tables within the HRAlit database in CSV format.

## Credits
This HRAlit dataset is developed by the [Cyberinfrastructure for Network Science Center at Indiana University](https://cns.iu.edu/). This research has been funded by the China Scholar Council [YK] and the NIH Common Fund through the Office of Strategic Coordination/Office of the NIH Director under awards OT2OD033756 and OT2OD026671, by the Cellular Senescence Network (SenNet) Consortium through the Consortium Organization and Data Coordinating Center (CODCC) under award number U24CA268108, by the Kidney Precision Medicine Project grant U2CDK114886, by the NIDDK under awards U24DK135157 and U01DK133090 and by The Multiscale Human CIFAR project [KB]. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript. 
