# SEAO Open Data Analaysis

This project cleans and transforms the province of Quebec's public RFP data to be loaded in a database. Uses python to load XML data.
Data quality analysis from 2009  to 2021

### Original system and Open Data
[SEAO](https://www.seao.ca/) : Systeme Electronique d'Appel d'Offres (du gouvernement du quebec)

Published [Open Data for SEAO](https://www.donneesquebec.ca/recherche/fr/dataset/systeme-electronique-dappel-doffres-seao)


## Context
SEAO Data is stored in three types of information files
1) Avis              : Published RFPs contains all signed contracts with unique number (numeroseao)
2) AvisRevision      : Revised RFPs (adjustments can go back to previous years - WOW) 
3) Contrats          : Contains final information on closed contracts
4) ContratsRevision  : Contains revised information on final closed contracts (WHAT?)
5) Depenses          : Contains exta spending on signed contracts
6) DepensesRevisions : Contains all revisions on extra spending for signed contracts (empty amount value means all spending were removed for this contract)

See [SEAO XML Schema](https://www.donneesquebec.ca/recherche/fr/dataset/systeme-electronique-dappel-doffres-seao/resource/af41596c-b07f-4664-82c8-577e1ef9a6f3) PDF file for detailed information (in french)

