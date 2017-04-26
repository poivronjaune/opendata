# SEAO Open Data Analaysis

This project cleans and transforms the province of Quebec's public RFP data to be loaded in a Google BigQuery data set. Uses python to load XML data, clean unwanted characters and transforms the information to a new line delimited Json file [(jsonl)](http://jsonlines.org/).

Data quality analysis from 2009  to 2017

## Getting Started

Download the project and all XML files to a working directory. Run python seao.py to convert all XML data to JSONL. Might take many hours to execute.

### Prerequisites

Must have python 3 installed. Developped using ANACONDA.
Must have the following libraries installed : codecs, xmltodict, json, xml.etree.ElementTree

### Original system and Open Data
[SEAO](https://www.seao.ca/) : Systeme Electronique d'Appel d'Offres (du gouvernement du quebec)

Published [Open Data for SEAO](https://www.donneesquebec.ca/recherche/fr/dataset/systeme-electronique-dappel-doffres-seao)


## Context
SEAO Data is stored in three type of information
1) Avis              : Published RFPs contains all signed contracts with unique number (numeroseao)
2) AvisRevision      : Revised RFPs (adjustments can go back to previous years - WOW) 
3) Contrats          : Contains final information on closed contracts
4) ContratsRevision  : Contains revised information on final closed contracts (WHAT?)
5) Depenses          : Contains exta spending on signed contracts
6) DepensesRevisions : Contains all revisions on extra spending for signed contracts (empty amount value means all spending were removed for this contract)

See [SEAO XML Schema](https://www.donneesquebec.ca/recherche/fr/dataset/systeme-electronique-dappel-doffres-seao/resource/af41596c-b07f-4664-82c8-577e1ef9a6f3) PDF file for detailed information (in french)

## Solution (work in progress)

- Extract and transform the <XML> data to JSON
-- Many Avis files to be combined in one table Avis_all contains all published avis from 2009
-- TODO: Many Soumissionaires files to be combined in one table Soumisionaires_all contains all companies who responded to the RFP (Avis)
-- Many Contrats files to be combined in one table Contrat_all contains all published contracts with fournisseur and amount
-- Many Depenses files to be combined in one table Depenses_all contains all published contracts with fournisseur and amount (denormalized to repeat numeroseao IDs)
- Export to JSON format for easy loading in a public big data warehouse (Google BigQuery) - AVIS and CONTRAT

## TODO : Other functions to develop
- Finish loading the rest of Data : Soumissionnaires, AvisRevision, ContratsRevision, DepensesRevision
- Add Google DATASTUDIO examples to analyse the data
- Develop a user interface to access data with predefined searches and slicers in DataStudio or a Dedicated website
- Maybe use an open source data visualisation tool connected directly on BigQuery (investigating Power BI)
- Automate data loading : Improve function that loads raw data to connect directly open data website, download the zip file, extact and save to disk
- Automate data load quality with stats to validate that number of XML elements have been coverted to JSON lines and check number of elements loaded into BigQuery
- Add notification to all subscribed followers of this data (need to clarify this requirement)

