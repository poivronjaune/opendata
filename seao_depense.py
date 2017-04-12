# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 20:44:04 2017

  Data converter of XML to New Line Delimited Json file for import in Google BigQuery

"""
import codecs
import xmltodict
import json
import xml.etree.ElementTree as et


def GetFileNames():
    filenames = []
    filenames.append('2017-03\Depenses_20170301_20170331.xml')
    filenames.append('2017-02\Depenses_20170201_20170228.xml')
    filenames.append('2017-01\Depenses_20170101_20170131.xml')
    filenames.append('2016-12\Depenses_20161201_20161231.xml')
    filenames.append('2016-11\Depenses_20161101_20161130.xml')
    filenames.append('2016-10\Depenses_20161001_20161031.xml')
    filenames.append('2016-09\Depenses_20160901_20160930.xml')
    filenames.append('2016-08\Depenses_20160801_20160831.xml')
    filenames.append('2016-07\Depenses_20160701_20160731.xml')
    filenames.append('2016-06\Depenses_20160601_20160630.xml')
    filenames.append('2016-05\Depenses_20160501_20160531.xml')
    filenames.append('2016-04\Depenses_20160401_20160430.xml')
    filenames.append('2016-03\Depenses_20160301_20160331.xml')
    filenames.append('2016-02\Depenses_20160201_20160229.xml')
    filenames.append('2016-01\Depenses_20160101_20160131.xml')
    filenames.append('2015\Depenses_20150101_20151231.xml')
    filenames.append('2014\Depenses_20140101_20141231.xml')
    filenames.append('2013\Depenses_20130101_20131231.xml')
    
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
    outfile = "json\\depense-" + loadedXMLFile[:slash] + ".jsonl"
    file = codecs.open(outfile, "w", "utf-8")
    file.write(JSonToSave_str)
    file.close()
    print("- JSON File saved as : " + outfile)




fnames = GetFileNames()
for i in range(0,len(fnames)):
#for i in range(0,1):    
    f = codecs.open(fnames[i], 'r', encoding='utf8')
    str_data = f.read()
    f.close()
    print("- File opened : " + fnames[i])
    
    str_data_cleaned = CleanString(str_data)
    print("- Loaded string cleaned...")
    
    xml_data = et.fromstring(str_data_cleaned)
    print("- Cleaned string data converted to python Dict...")
    
    all_avis = xml_data.findall('avis')
    print("- Number of avis data elements in XML File : " + str(len(all_avis)))

    xml_dict = xmltodict.parse(str_data_cleaned)
    print("- XML Data converted to dictionnary")
    json_str = json.dumps(xml_dict, indent=None)
    print("- XML from dictionnary tranformed as JSON string")
    json_dict = json.loads(json_str)
    print("- JSON dictionnary loaded, ready for manipulation")

    new_str_json = ""
    nbr_depenses = 0
    for x in range(0,len(json_dict['export']['avis'])):
        unavis = json_dict['export']['avis'][x]
        all_depenses = unavis.pop('depenses')
        if type(all_depenses['depense']) == list:
            for y in range(0,len(all_depenses['depense'])):
                une_depense = all_depenses['depense'][y]
                tmp_str_json = json.dumps(unavis) + json.dumps(une_depense) + chr(10)
                tmp_str_json = tmp_str_json.replace("}{",",")           
                new_str_json = new_str_json + tmp_str_json
                nbr_depenses = nbr_depenses + 1
        else:
            une_depense = all_depenses['depense']
            tmp_str_json = json.dumps(unavis) + json.dumps(une_depense) + chr(10)
            tmp_str_json = tmp_str_json.replace("}{",",")           
            new_str_json = new_str_json + tmp_str_json
            nbr_depenses = nbr_depenses + 1
#           

    saveJsonFile(fnames[i],new_str_json)
    print("- Transform stats -> XML avis : " + str(len(all_avis)) + " JSON avis : " + str(len(json_dict['export']['avis'])) + " depenses : " + str(nbr_depenses))

    
print("End of execution")





