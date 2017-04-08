# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 00:17:39 2017

@author: poivron jaune

This Pyton App, counts the number of avis in SEAO Files
The original XML file downloaded is used
https://www.donneesquebec.ca/recherche/fr/dataset?sort=metadata_modified+desc&q=seao

WHY:
    Since many invalid characters have been found in these files this progam
    helps in validating amount of data loaded in Big Query by displaying
    number of Avis in each file
"""

import seao_common as seao


""" Load data from local folder """
Avis = seao.InitDataPaths()

for i in range(0,len(Avis)):
    xml_data = seao.LoadXMLFile(Avis[i])
    all_avis = seao.ExtractAllAvis(xml_data)
    
    print("File name________ : " + Avis[i])
    print("XML Data items___ : " + str(len(all_avis)))

print('End of execution!') 
