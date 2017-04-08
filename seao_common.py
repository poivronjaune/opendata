# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 12:38:28 2017

@author: poivron jaune

Library used to store SEAO information coming from
https://www.donneesquebec.ca/recherche/fr/dataset?sort=metadata_modified+desc&q=seao

"""
import codecs
import xml.etree.ElementTree as et


"""
  Initialize an array of all file name in the SEAO dataset
  
    TODO: Add automatic file detection and move to a dedicated subfolder called SEAODATA
    TODO: Add automatic download from SEAO
   
"""
def InitDataPaths():
    Avis = []
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
    xml_data = et.fromstring(str_data)
    return xml_data

"""
  Extracts all Avis rom the export structure in the XML Data
  
  The <avis></avis> tag is ususally lower case, but sometimes mistakes are introduced
"""
def ExtractAllAvis(xml_data):
    all_avis = xml_data.findall('avis')
    if (len(all_avis) == 0):
        all_avis = xml_data.findall('Avis')
    
    return all_avis

"""
  Extracts all fournisseurs elements from an XML Tree containing
  the detailed data from Avis
"""
def RemoveFournisseurs(allavis):
    smallavis = et.Element('seao')
    for unavis in allavis:
        unavis.remove(unavis.find('fournisseurs'))
        smallavis.append(unavis)
        
    return smallavis.findall('avis')


"""
  Use an XML Tree containing all Avis without any Fournisseurs to generate
  a JSON String delimited with New lines (JSON format for Big Query)
"""
def GenerateJsonString(allavis):
    str_avis = ""
    for unavis in allavis:
        str_avis = str_avis + "{"
        for i in range(0,len(unavis)-2):
            clean_str = str(unavis[i].text).replace('"', '')
            clean_str = clean_str.strip()
            str_avis = str_avis + '"' + unavis[i].tag + '":"' + clean_str + '",' 
        
        clean_str = str(unavis[len(unavis)-1].text).replace('"', '')
        str_avis = str_avis + '"' + unavis[len(unavis)-1].tag + '":"' + clean_str + '"' 
        str_avis = str_avis + "}\n"
    return str_avis
    
    
    
    
    
    
    
    