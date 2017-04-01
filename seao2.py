# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:05:48 2017
"""
import codecs
import xml.etree.ElementTree as et
import json
import xmltodict


"""
Initialisation des répertoires de chargement
TODO: Add automatic file detection and move to a dedicated subfolder called SEAODATA
TODO: Add automatic download from SEAO
"""
def InitDataPaths():
	Avis.append('2017-01\Avis_20170101_20170131.xml')
	Avis.append('2016-12\Avis_20161201_20161231.xml')
	Avis.append('2016-11\Avis_20161101_20161130.xml')
	Avis.append('2016-10\Avis_20161001_20161031.xml')
	Avis.append('2016-09\Avis_20160901_20160930.xml')
	Avis.append('2016-08\Avis_20160801_20160831.xml')
	Avis.append('2016-07\Avis_20160701_20160731.xml')
	Avis.append('2016-06\Avis_20160601_20160630.xml')
	Avis.append('2016-05\Avis_20160501_20160531.xml')
	Avis.append('2016-04\Avis_20160401_20160430.xml')
	Avis.append('2016-03\Avis_20160301_20160331.xml')
	Avis.append('2016-02\Avis_20160201_20160229.xml')
	Avis.append('2016-01\Avis_20160101_20160131.xml')
	Avis.append('2015\Avis_20150101_20151231.xml')
	Avis.append('2014\Avis_20140101_20141231.xml')
	Avis.append('2013\Avis_20130101_20131231.xml')
	Avis.append('2012\Avis_20120101_20121231.xml')
	Avis.append('2011\Avis_20110101_20111231.xml')
	Avis.append('2010\Avis_20100101_20101231.xml')
	Avis.append('2009\Avis_20090101_20091231.xml')



"""
*******   Begin of data transformation
"""



""" Load data from local folder """
Avis = []
InitDataPaths()



""" Get first file from Avis[] array and load XML data as a string """
fichier = Avis[0]
f = codecs.open(fichier, 'r', encoding='utf8')
str_data = f.read()
f.close()



""" Transform XML Data string into a Python Dictionnary """
root = et.fromstring(str_data)
print("- SEAO XML File loaded")



""" Extract all AVIS (RFPs) including FOURNISSEURS list """
allavis = root.findall('avis')
print("- All Avis retreived from XML Data : " + str(len(allavis)))



""" Remove all FOURNISSEURS data to keep only the AVIS """
smallavis = et.Element('seao')
x = 0
for unavis in allavis:
    unavis.remove(unavis.find('fournisseurs'))
    smallavis.append(unavis)
    x = x + 1
    if x >= 5:
        break
print("- Removed all fournisseurs from avis")


""" Save the new XML data to a file? Before we convert it could skipped if converted directly to JSON """
outfile = "avis_seulement.xml"
tree = et.ElementTree(smallavis)
tree.write(outfile)
print("- New avis without fournisseurs saved to file : " + outfile)



""" Convert tree to JSON Format """
f = codecs.open(outfile, 'r', encoding='utf8')
str_data = f.read()
f.close()
json_data = xmltodict.parse(str_data)
with open('avis.json', 'w') as fout:
    json.dump(json_data, fout, indent=4)

print("- End of execution")




"""
newavis = None
i = 0
for unavis in root.findall('avis'):
#    fournisseurs = unavis.find('fournisseurs')
#    unavis.remove(fournisseurs)
    str1 = et.tostring(unavis, encoding="utf8", method='xml')
    print(str1)
    break
    if i == 0:
        newavis = unavis
    else:
        newavis.append(unavis)
    i = i + 1 
    print(newavis)
    if i > 5:
        break
"""



