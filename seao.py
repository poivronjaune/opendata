import sys
import os
import os.path
import json
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

import xml.etree.ElementTree as ET

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB/avis.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

def cls():
    cls = os.system('cls')


class Avis(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numeroseao = db.Column(db.String(250))
    numero = db.Column(db.String(250))
    organisme = db.Column(db.String(250))
    municipal = db.Column(db.String(250))
    adresse1 = db.Column(db.String(250))
    adresse2 = db.Column(db.String(250))
    ville = db.Column(db.String(250))
    province = db.Column(db.String(250))
    pays = db.Column(db.String(250))
    codepostal = db.Column(db.String(250))
    titre = db.Column(db.String(250))
    type_ = db.Column(db.String(250))
    nature = db.Column(db.String(250))
    precision = db.Column(db.String(250))
    categorieseao = db.Column(db.String(250))
    datepublication = db.Column(db.String(250))
    datefermeture = db.Column(db.String(250))
    datesaisieouverture = db.Column(db.String(250))
    datesaisieadjudication = db.Column(db.String(250))
    dateadjudication = db.Column(db.String(250))
    regionlivraison = db.Column(db.String(250))
    unspscprincipale = db.Column(db.String(250))
    disposition = db.Column(db.String(250))
    hyperlienseao = db.Column(db.String(250))

class Fournisseurs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    neq = db.Column(db.String(20))
    nomorganisation = db.Column(db.String(30))
    adresse1 = db.Column(db.String(250))
    adresse2 = db.Column(db.String(250))
    ville = db.Column(db.String(250))
    province = db.Column(db.String(10))
    pays = db.Column(db.String(50))
    codepostal = db.Column(db.String(10))



def SaveAvis(unavis):
    avis = Avis()
    avis.numeroseao = unavis.find('numeroseao').text
    avis.numero = unavis.find('numero').text
    avis.organisme = unavis.find('organisme').text
    avis.municipal = unavis.find('municipal').text
    avis.adresse1 = unavis.find('adresse1').text
    avis.adresse2 = unavis.find('adresse2').text
    avis.ville = unavis.find('ville').text
    avis.province = unavis.find('province').text
    avis.pays = unavis.find('pays').text
    avis.codepostal = unavis.find('codepostal').text
    avis.titre = unavis.find('titre').text
    avis.type_ = unavis.find('type').text
    avis.nature = unavis.find('nature').text
    avis.precision = unavis.find('precision').text
    avis.categorieseao = unavis.find('categorieseao').text
    avis.datepublication = unavis.find('datepublication').text
    avis.datefermeture = unavis.find('datefermeture').text
    avis.datesaisieouverture = unavis.find('datesaisieouverture').text
    avis.datesaisieadjudication = unavis.find('datesaisieadjudication').text
    avis.dateadjudication = unavis.find('dateadjudication').text
    avis.regionlivraison = unavis.find('regionlivraison').text
    avis.unspscprincipale = unavis.find('unspscprincipale').text
    avis.disposition = unavis.find('disposition').text
    avis.hyperlienseao = unavis.find('hyperlienseao').text

    db.session.add(avis)
    db.session.commit()
    return avis.id

def SaveFournisseurs(unavis):
    fournisseurs = unavis.find('fournisseurs')
    neqs = []
    for unfournisseur in fournisseurs:
        neqs.append(unfournisseur.find('neq').text)
        fournisseur = Fournisseurs()
        fournisseur.neq             = unfournisseur.find('neq').text
        fournisseur.nomorganisation = unfournisseur.find('nomorganisation').text
        fournisseur.adresse1        = unfournisseur.find('adresse1').text
        fournisseur.adresse2        = unfournisseur.find('adresse2').text
        fournisseur.ville           = unfournisseur.find('ville').text
        fournisseur.province        = unfournisseur.find('province').text
        fournisseur.pays            = unfournisseur.find('pays').text
        fournisseur.codepostal      = unfournisseur.find('codepostal').text
        db.session.add(fournisseur)
        db.session.commit()

    return neqs



def load_db_from_xml_file(file):
    file_name = 'DATA/SEAO/'+file
    if os.path.isfile(file_name):
        avistree = ET.parse(file_name)
        avisroot = avistree.getroot()
        for avis in avisroot:
            # Save to DB and print to output
            print(f"{SaveAvis(avis)} : {avis.find('numeroseao').text }, {SaveFournisseurs(avis)}")
    else:
        file_name = 'DATA/SEAO/'+file
        print(f"\n\nFile not found : {file_name}\n\n")


def print_menu():
    print(f"███████╗███████╗ █████╗  ██████╗     ██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ ")
    print(f"██╔════╝██╔════╝██╔══██╗██╔═══██╗    ██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
    print(f"███████╗█████╗  ███████║██║   ██║    ██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝")
    print(f"╚════██║██╔══╝  ██╔══██║██║   ██║    ██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗")
    print(f"███████║███████╗██║  ██║╚██████╔╝    ███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║")
    print(f"╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
    print(f"\n")
    print(f"py seao.py --initdb      : Dangerous use with caution, reset databases")
    print(f"py seao.py --load <file> : load xml avis file")
    print(f"\n")

# mytree = ET.parse('test.xml')
# myroot = mytree.getroot()
# print(f"myroot: {myroot.tag}")

if len(sys.argv) > 1:
    if sys.argv[1] == '--initdb':
        db.drop_all()
        db.create_all()
        print(f"\n\nAll tables defined by models were reset to empty\n\n")

    if len(sys.argv) > 1:
        if sys.argv[1] == '--load':
            load_db_from_xml_file(sys.argv[2])

print_menu()


