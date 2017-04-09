Open Data Project for fun. 
Started with contract information from quebec governement signed contracts from 2009 till today (2017-04-01)

SEAO : Systeme Electronique d'Appel d'Offres (du gouvernement du quebec)
https://www.seao.ca/

Published Open Data for SEAO
https://www.donneesquebec.ca/recherche/fr/dataset/systeme-electronique-dappel-doffres-seao


No install insctructions for now because I am learning....

CONTEXT
-------
SEAO Data is stored in three type of information
1) Avis              : Published RFPs contains all signed contracts with unique number (numeroseao)
2) AvisRevision      : Revised RFPs (adjustments can go back to previous years - WOW) 
3) Contrats          : Contains final information on closed contracts
4) ContratsRevision  : Contains revised information on final closed contracts (WHAT?)
5) Depenses          : Contains exta spending on signed contracts
6) DepensesRevisions : Contains all revisions on extra spending for signed contracts (empty amount value means all spending were removed for this contract)


see : "seao-specificationsxml-donneesouvertes-20141201.pdf" for detailed information (in french)

Solution summary (work in progress)
- Extract and transform the <XML> data to JSON and split AVIS (RFPs) from FOURNISSEURS (contracters)
- Combine data from all other information type in the AVIS data
- Export to JSON format for easy loading in a public big data warehouse (Google BigQuery) - AVIS and FOURNISSEURS
- To be determined
