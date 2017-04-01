# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 21:05:48 2017
"""
import codecs
import xml.etree.ElementTree as et
import json


"""
Initialisation des répertoires de chargement
"""
def initChargement():
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

Avis = []
initChargement()


fichier = Avis[0]
f = codecs.open(fichier, 'r', encoding='utf8')
str_data = f.read()
f.close()


root = et.fromstring(str_data)
"""
print(root.tag)
print(root.attrib)
print(root.find('avis').find('numeroseao').text)
print(et.iselement(root.find('avis')))
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




print("Fin d'execution")