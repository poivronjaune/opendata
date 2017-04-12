# -*- coding: utf-8 -*-
"""
  Data converter of XML to New Line Delimited Json file for import in Google BigQuery
"""

import codecs
import xmltodict
import json
import xml.etree.ElementTree as et


def GetFileNames():
    filenames = []
    filenames.append('2017-03\Contrats_20170301_20170331.xml')
    filenames.append('2017-02\Contrats_20170201_20170228.xml')
    filenames.append('2017-01\Contrats_20170101_20170131.xml')
    filenames.append('2016-12\Contrats_20161201_20161231.xml')
    filenames.append('2016-11\Contrats_20161101_20161130.xml')
    filenames.append('2016-10\Contrats_20161001_20161031.xml')
    filenames.append('2016-09\Contrats_20160901_20160930.xml')
    filenames.append('2016-08\Contrats_20160801_20160831.xml')
    filenames.append('2016-07\Contrats_20160701_20160731.xml')
    filenames.append('2016-06\Contrats_20160601_20160630.xml')
    filenames.append('2016-05\Contrats_20160501_20160531.xml')
    filenames.append('2016-04\Contrats_20160401_20160430.xml')
    filenames.append('2016-03\Contrats_20160301_20160331.xml')
    filenames.append('2016-02\Contrats_20160201_20160229.xml')
    filenames.append('2016-01\Contrats_20160101_20160131.xml')
    filenames.append('2015\Contrats_20150101_20151231.xml')
    filenames.append('2014\Contrats_20140101_20141231.xml')
    filenames.append('2013\Contrats_20130101_20131231.xml')
    
    return filenames

def CleanString(str_data):
    content_start = str_data.find('<contrat>')
    
    escapes = ''.join([chr(char) for char in range(1, 32)])
    escapes = escapes + '"'
    replaced = " " * len(escapes)
    t = str.maketrans(escapes,replaced)
    
    newstr = str_data[:content_start] + str_data[content_start:].translate(t)
    
    return newstr

def saveJsonFile(loadedXMLFile,JSonToSave_str):
    slash = loadedXMLFile.find("\\")
    outfile = "json\\contrat-" + loadedXMLFile[:slash] + ".jsonl"
    file = codecs.open(outfile, "w", "utf-8")
    file.write(JSonToSave_str)
    file.close()
    print("- JSON File saved as : " + outfile)



fnames = GetFileNames()
for i in range(0,len(fnames)):
    f = codecs.open(fnames[i], 'r', encoding='utf8')
    str_data = f.read()
    f.close()
    print("- File opened : " + fnames[i])
    
    str_data_cleaned = CleanString(str_data)
    print("- Loaded string cleaned...")
    
    xml_data = et.fromstring(str_data_cleaned)
    print("- Cleaned string data converted to python Dict...")
    
    all_contrat = xml_data.findall('contrat')
    print("- Number of contract data elements in XML File : " + str(len(all_contrat)))

    xml_dict = xmltodict.parse(str_data_cleaned)
    print("- XML Data converted to dictionnary")
    
    json_str = json.dumps(xml_dict, indent=None)
    print("- XML from dictionnary tranformed as JSON string")
    
    json_dict = json.loads(json_str)
    print("- JSON dictionnary loaded, ready for manipulation")

    new_json = ""
    x = 0
    milliers = 0
    for uncontrat in json_dict['export']['contrat']:
        new_json = new_json + json.dumps(uncontrat) + chr(10)
        x = x + 1
        if x > 1000:
            x = 0
            milliers = milliers + 1000
            print('Generated : ' + str(milliers))

    saveJsonFile(fnames[i],new_json)
    print("- Json file saved")

print("End of execution")


