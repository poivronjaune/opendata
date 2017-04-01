import json
import xmltodict
import codecs

str1 = '<mydocument has="an attribute"><and><many>elements</many><many>more elements</many></and><plus a="complex">element as well</plus></mydocument>'
print(type(str1))
xml1 = xmltodict.parse(str1)
print(type(xml1))
print(json.dumps(xml1['mydocument'], indent=4))
