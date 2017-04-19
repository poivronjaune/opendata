# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 16:10:14 2017

"""
import codecs
import xmltodict
import json
import xml.etree.ElementTree as et

def saveJsonFile(loadedXMLFile,JSonToSave_str):
    slash = loadedXMLFile.find("\\")
    outfile = "json\\soumissionnaire-" + loadedXMLFile[:slash] + ".jsonl"
    file = codecs.open(outfile, "w", "utf-8")
    file.write(JSonToSave_str)
    file.close()
    print("- JSON File saved as : " + outfile)
    
def InitDataPaths():
    Avis = []
    Avis.append('2017-03\Avis_20170301_20170331.xml')
    Avis.append('2017-02\Avis_20170201_20170228.xml')
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
    return Avis

"""
  Load a specific SEAO XML File and return XML Data tree
"""
def LoadXMLFile(filename):
    filename = filename
    f = codecs.open(filename, 'r', encoding='utf8')
    str_data = f.read()
    f.close()
    return str_data


"""
  Function to remove special charcaters from XML Data values
  Pass a string, get a cleaned string back
"""
def CleanString(str_data):
    content_start = str_data.find('<avis>')
    if content_start == 0:
        content_start = str_data.find('<Avis>')
    
    escapes = ''.join([chr(char) for char in range(1, 32)])
    escapes = escapes + '"'
    replaced = " " * len(escapes)
    t = str.maketrans(escapes,replaced)
    
    newstr = str_data[:content_start] + str_data[content_start:].translate(t)
    
    return newstr

"""
  Extracts all Avis rom the export structure in the XML Data
  
  The <avis></avis> tag is ususally lower case, but sometimes mistakes are introduced
"""
def ExtractAllAvis(xml_data):
    all_avis = xml_data.findall('avis')
    if (len(all_avis) == 0):
        all_avis = xml_data.findall('Avis')
    
    return all_avis




""" Load data from local folder """
Avis = InitDataPaths()


""" Get first file from Avis[] array and load XML data as a string """
for fileIndex in range(0, len(Avis)):
#for fileIndex in range(0, 1):

    str_data = LoadXMLFile(Avis[fileIndex])
    print("- Avis File Loaded as String: " + Avis[fileIndex])

    str_data_cleaned = CleanString(str_data)
    print("- XML data has been cleaned")

    xml_data = et.fromstring(str_data)
    all_avis = ExtractAllAvis(xml_data)

    xml_dict = xmltodict.parse(str_data_cleaned)
    print("- XML Data converted to dictionnary")
    json_str = json.dumps(xml_dict, indent=None)
    print("- XML from dictionnary tranformed as JSON string")
    json_dict = json.loads(json_str)
    print("- JSON dictionnary loaded, ready for manipulation")

    avis_key = 'avis'
    if avis_key not in json_dict['export']:
        avis_key = 'Avis'

    new_json = ''
    x = 0
    milliers = 0
    nbr_fournisseurs = 0
    for unavis in json_dict['export'][avis_key]:
        #unavis.pop('fournisseurs')
        avisid = '{"numeroseao":"' + str(unavis['numeroseao']) + '"}'
        fournisseurs = unavis['fournisseurs']['fournisseur']
        if type(fournisseurs) == list:
            for unfournisseur in fournisseurs:
                new_json = new_json + avisid[:-1] + "," + json.dumps(unfournisseur)[1:] + chr(10)
                nbr_fournisseurs = nbr_fournisseurs + 1
        else:
            new_json = new_json + avisid[:-1] + "," + json.dumps(fournisseurs)[1:] + chr(10)
            nbr_fournisseurs = nbr_fournisseurs + 1
            
        x = x + 1
        if x > 1000:
            x = 0
            milliers = milliers + 1000
            print('Generated : ' + str(milliers))  
  
    print("XML Data items, Avis : " + str(len(all_avis)) + " , Nbr fournisseurs : " + str(nbr_fournisseurs) )

    saveJsonFile(Avis[fileIndex],new_json)
    print("- Json file saved")











