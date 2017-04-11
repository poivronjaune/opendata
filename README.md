# SEAO Open Data Analaysis

This project cleans and transforms the province of Quebec's public RFP data to be loaded in a Google BigQuery data set. Uses python to load XML data, clean unwanted characters and transforms the information to a new line delimited Json file (jsonl).

Data quality analysis from 2009  to 2017

## Getting Started

Download the project and all XML files to a working directory. Run python seao.py to convert all XML data to JSONL. Might take many hours to execute.

### Prerequisites

Must have python 3 installed. I used the ANACONDA version.

### Original system and Open Data
SEAO : Systeme Electronique d'Appel d'Offres (du gouvernement du quebec)
https://www.seao.ca/

Published Open Data for SEAO
https://www.donneesquebec.ca/recherche/fr/dataset/systeme-electronique-dappel-doffres-seao


## Context
SEAO Data is stored in three type of information
1) Avis              : Published RFPs contains all signed contracts with unique number (numeroseao)
2) AvisRevision      : Revised RFPs (adjustments can go back to previous years - WOW) 
3) Contrats          : Contains final information on closed contracts
4) ContratsRevision  : Contains revised information on final closed contracts (WHAT?)
5) Depenses          : Contains exta spending on signed contracts
6) DepensesRevisions : Contains all revisions on extra spending for signed contracts (empty amount value means all spending were removed for this contract)


see : "seao-specificationsxml-donneesouvertes-20141201.pdf" for detailed information (in french)

Solution summary (work in progress)
- Extract and transform the <XML> data to JSON
-- One table Avis_all contains all published avis from 2009
-- One table Soumisionaires_all contains all companies who responded to the RFP (Avis) TODO
-- One table Contrat_all contains all published contracts with fournisseur and amount
- Export to JSON format for easy loading in a public big data warehouse (Google BigQuery) - AVIS and CONTRAT

- TODO:
- Finish loading the rest of Data : Soumissionnaires, AvisRevision, ContratsRevision, Depenses, DepensesRevision
- Combine data from all other information files into one main database for numeroseao and all other changes
- Add Google DATASTUDIO examples to analyse data
- Develop a user interface to access data with predefined searches and slicers
- Maybe use an open source data visualisation tool connected directly on BigQuery
