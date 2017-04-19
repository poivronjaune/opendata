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
#for i in range(0,len(fnames)):
for i in range(15,16):    
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

    numseao = ['487181']
    doublons = 0
    for unavis in all_avis:
        numeroseao = unavis.find('numeroseao').text.replace(" ","")
        if numeroseao in numseao:
            doublons = doublons + 1
        else:
            numseao.append(numeroseao)
    

    numseao.sort()
    print(numseao)
    print(doublons)
    
print("End of execution")





