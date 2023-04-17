# Literature (HRA Literature)
This file provides easy access to data and code used in the HRA literature.
It is included in the following way:
* CellMarker
* PubMed
* BioGRID
* Alliance Genome
* Textpresso
* iReceptor
* BioStudies
* Pharos NIH
* MetGene


## Code
1. wos.sql
> Retrieve the publication data for [34 HRA organs](./data/list_of_organs.csv) from Web of Science database.

2. pubmed.sql
> Retrieve the publication data for [34 HRA organs](./data/list_of_organs.csv) from PubMed database.

3. alliancegene.py
> Retrieve the [alliancegene](https://www.alliancegenome.org/) data.

4. textpresso_api.py
> This api is used for extracting the data from [textpresso database](https://www.textpresso.org/). Please refer to the [documentation](https://gist.github.com/yokongkk/4c9eaebdb46b68dd88bf87b592f8c775) for more information.


 
## Data
```list_of_organs.csv```contains the 34 HRA organs.

```alliance_publications_all.csv```contains the literature data from alliancegene database, including pmid, biotype and identifier_type data.
 
```Human_cell_markers.csv```contains the literature data from CellMarker database, including speciesType, tissueType, UberonOntologyID, cancerType, cellType, cellName, CellOntologyID, cellMarker, geneSymbol, geneID, proteinName, proteinID, markerResource, PMID, Company, DOI

