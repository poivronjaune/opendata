# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:05:48 2017
"""
import codecs

import seao_common as seao

def saveJsonFile(loadedXMLFile,JSonToSave_str):
    slash = loadedXMLFile.find("\\")
    outfile = "json\\avis-" + loadedXMLFile[:slash] + ".jsonl"
    file = codecs.open(outfile, "w", "utf-8")
    file.write(JSonToSave_str)
    file.close()
    print("- JSON File saved as : " + outfile)


""" Load data from local folder """
Avis = seao.InitDataPaths()


""" Get first file from Avis[] array and load XML data as a string """
#for fileIndex in range(13,len(Avis)):
fileIndex = 8
xml_data = seao.LoadXMLFile(Avis[fileIndex])
print("- Avis File Loaded : " + Avis[fileIndex])

all_avis = seao.ExtractAllAvis(xml_data)
print("- Extracted all avis with fournisseurs")

small_avis = seao.RemoveFournisseurs(all_avis)
print("- Fournisseurs striped from all loaded Avis")

str_avis = seao.GenerateJsonString(small_avis)
print("- Generated Json File to save")

saveJsonFile(Avis[fileIndex],str_avis)
print("- End of execution")




