from bs4 import BeautifulSoup
import urllib.request as url
import xml.etree.ElementTree as et
import itertools
import codecs
import json
import xmltodict

# Test d'ouverture de données Web
def test_xml():
	url1 = 'http://www.w3schools.com/xml/cd_catalog.xml'
	web_data = url.urlopen(url1)
	str_data = web_data.read()

	xml_data = et.fromstring(str_data)
	cd_list = xml_data.findall("CD")
	cd_prices = []
	
	i = 0
	for x in cd_list:
		cd_prices.append(float(x.find("PRICE").text))
		print(str(cd_prices[i]) + " | " + x.find("TITLE").text )
		i = i + 1

# Début dossier analyse du SEAO

##
# Chargement des avis d'appels d'offres
##
def get_avis(fichier):
	f = codecs.open(fichier, 'r', encoding='utf8')
	str_data = f.read()
	f.close()
	xml_data = et.fromstring(str_data)
	avis_list = xml_data.findall("avis")
	return avis_list

##
# Recherche des avis avec révision dans les anciens appels d'offres
##	
def trouveRevision(seao_AvisRev, seao_Avis):
	match = 0
	matchlist = []
	for rev in seao_AvisRev:
		numeroRev = rev.find("numeroseao").text
		for avis in seao_Avis:
			numero = avis.find("numeroseao").text
			if numeroRev == numero:
				match = match + 1
				matchlist.append(numeroRev)
				
	return [match, matchlist]

##
# Initialisation des répertoires de chargement
##
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

fichier_AvisRev = '2017-01\AvisRevisions_20170101_20170131.xml'

# print("***************     Recherche années révision ***")	
# seao_AvisRev = get_avis(fichier_AvisRev)
# print("Nombre avis révisée   : " + str(len(seao_AvisRev)))

# total_match = 0
# for fichier in Avis:
	# seao_Avis = get_avis(fichier)
	# print(fichier + "   Nombre avis : " + str(len(seao_Avis)))
	# match = trouveRevision(seao_AvisRev,seao_Avis)
	# total_match = total_match + match[0]
	# print("Révision retrouvée : " + str(match[0]))
	# print("Révision liste : " + str(match[1]))
	# print("--------------------------------------------")

# print("Nombre total retrouvé : " + str(total_match))


print("***************     Analyse des données **********")	
seao_Avis = get_avis(Avis[0])
print(Avis[0])

# Répartition des avis selon les codes municipales, type contrat, nature ocntrat
municipale = [0,0,0]  
type_contrat = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
nature_contrat = [0,0,0,0,0,0,0,0,0,0]
nombre_fournisseurs = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
montant_cumul = 0
nbr_contrat_multiple_adju = 0
liste_multi_adju = []

# Analyse de janvier 2017
for avis in seao_Avis:
	# Municipal vs non municipal
	code_mun = avis.find("municipal").text
	if code_mun in ["0","1"]:
		municipale[int(code_mun)] = municipale[int(code_mun)] + 1
	else:
		municipale[2] = municipale[2] + 1

	# Type de contrat 
	code_type = avis.find("type").text
	if code_type in ["3","9","10","14","16","17"]:
		type_contrat[int(code_type)] = type_contrat[int(code_type)] + 1
	else:
		type_contrat[18] = type_contrat[18] + 1 

	# Nature de contrat
	code_nature = avis.find("nature").text
	if code_nature in ["1","2","3","5","6","7","8"]:
		nature_contrat[int(code_nature)] = nature_contrat[int(code_nature)] + 1
	else:
		nature_contrat[9] = nature_contrat[9] + 1
	
	fournisseurs = avis.find("fournisseurs")
	if len(fournisseurs) < 16:
		nombre_fournisseurs[len(fournisseurs)] = nombre_fournisseurs[len(fournisseurs)] + 1
		if len(fournisseurs) == 1:
			montantcontrat = float(fournisseurs[0].find("montantcontrat").text)
			montant_cumul = montant_cumul + montantcontrat
	else:
		nombre_fournisseurs[16] = nombre_fournisseurs[16] + 1

	nbr_adjudicatire = 0
	for f in fournisseurs:
		if f.find("adjudicataire").text == "1":
			nbr_adjudicatire = nbr_adjudicatire + 1
	
	if nbr_adjudicatire > 1:
		nbr_contrat_multiple_adju = nbr_contrat_multiple_adju + 1
		liste_multi_adju.append(avis.find("numeroseao").text)
		
	
# Print résultats d'analyse		
print("Municipale  : " + str(municipale) + "      Total : " + str(municipale[0]+municipale[1]+municipale[2]))
print("Type        : " + str(type_contrat))
print("Nature      : " + str(nature_contrat))
print("Nbr fournisseurs : " + str(nombre_fournisseurs))
print("Cumul montant 1F : " + str(montant_cumul))
print("Contrat moyen 1F : " + str(montant_cumul / nombre_fournisseurs[1]))
print("Nbr multi-adjudicataire : " + str(nbr_contrat_multiple_adju))
print("Liste multi-adju : " + str(liste_multi_adju))



print("\n\n\n\n******************* test écriture *****************************")

# seao_obj = []
# xmlfield = ['numeroseao','numero','organisme','adresse1','adresse2','ville','province','pays','codepostal','titre','type','nature','precision','datepublication','datefermeture','dateadjudication']
# for unavis in seao_Avis:
	# avis_obj = {xmlfield[0]:avis.find(xmlfield[0]).text}
	# print(type(avis_obj))
	# seao_obj.append(avis_obj)
	# print(seao_obj)
	# print(type(seao_obj))
	# break


fichier = Avis[0]
f = codecs.open(fichier, 'r', encoding='utf8')
str_data = f.read()
f.close()
root = et.fromstring(str_data)
print(root.tag)
print(root.attrib)
print(root.find('avis').find('numeroseao').text)
print(et.iselement(root.find('avis')))


i = 0
for avis in root.findall('avis'):
    fournisseurs = avis.find('fournisseurs')
    avis.remove(fournisseurs)
    if i == 0:
        newavis = avis
    else:
        newavis.append(avis)
    i = i + 1 
    print(newavis)
    if i > 5:
        break


		
#xmlstr = et.tostring(newavis, encoding="utf8", method='xml')		
#
#jsonstr = json.dumps(xmltodict.parse(xmlstr), indent=4)
#
#fileout = open('newavis.json','w')
#fileout.write(jsonstr)
#fileout.close()
	





# with open(fichier) as fd:
	# xml_dict = xmltodict.parse(fd.read())

# print(type(xml_dict))
# jsonstr_avis = json.dumps(xml_dict['export']['avis'], indent=4)
#print(type(jsonstr_avis))

# fileout = open('avis.json','w')
# fileout.write(jsonstr_avis)
# fileout.close()





