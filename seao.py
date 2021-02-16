import sys
import os
import os.path
import json
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

import xml.etree.ElementTree as ET

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB/seao.sqlite3'
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

class Propositions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    numeroseao = db.Column(db.String(250))
    neq = db.Column(db.String(20))
    fournisseurs_id = db.Column(db.Integer)
    avis_id = db.Column(db.Integer)
    admissible = (db.String(20))
    conforme = (db.String(20))
    adjudicataire = (db.String(20))
    montantsoumis = (db.String(20))
    montantssoumisunite = (db.String(20))
    montantcontrat = (db.String(20))
    montanttotalcontrat = (db.String(20))

class Region(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    desc = db.Column(db.String(150))
 
class Nature(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    desc = db.Column(db.String(150))

class Type(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(10))
    desc = db.Column(db.String(150))

class Disposition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    municipal = db.Column(db.String(1))             # 0:Non municipal, 1:Municipal
    code = db.Column(db.String(10))
    desc = db.Column(db.String(300))


#
# Helper functions to simplify loader functions
#
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
    return avis.id, avis.numeroseao

def SaveProposition(fournisseur, f_id, s_id, seao_num):
    p = Propositions()
    p.numeroseao          = seao_num
    p.neq                 = fournisseur.find('neq').text
    p.fournisseurs_id     = f_id
    p.avis_id             = s_id
    p.admissible          = fournisseur.find('admissible').text
    p.conforme            = fournisseur.find('conforme').text
    p.adjudicataire       = fournisseur.find('adjudicataire').text
    p.montantsoumis       = fournisseur.find('montantsoumis').text
    p.montantssoumisunite = fournisseur.find('montantssoumisunite').text
    p.montantcontrat      = fournisseur.find('montantcontrat').text
    p.montanttotalcontrat = fournisseur.find('montanttotalcontrat').text
    db.session.add(p)
    db.session.commit()

def SaveFournisseurs(unavis, s_id, seao_num):
    fournisseurs = unavis.find('fournisseurs')
    neqs = []
    f_ids = []
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
        f_ids.append(fournisseur.id)
        SaveProposition(unfournisseur, fournisseur.id, s_id, seao_num)

    return f_ids, neqs


#
# Loader functions
#
def load_db_from_xml_file(file):
    file_name = 'DATA/SEAO/'+file
    if os.path.isfile(file_name):
        avistree = ET.parse(file_name)
        avisroot = avistree.getroot()
        for avis in avisroot:
            # Save to DB and print to output
            s_id, seao_num = SaveAvis(avis) 
            f_ids, neqs = SaveFournisseurs(avis, s_id, seao_num)
            print(f"({s_id}, {seao_num}) : {avis.find('numeroseao').text }, {neqs}")
    else:
        file_name = 'DATA/SEAO/'+file
        print(f"\n\nFile not found : {file_name}\n\n")


def load_regions():
    regions = [
        {"code": 1, "desc": "Bas St-Laurent"},
        {"code": 2, "desc": "Saguenay-Lac-St-Jean"},
        {"code": 3, "desc": "Capitale Nationale"},
        {"code": 4, "desc": "Mauricie"},
        {"code": 5, "desc": "Estrie"},
        {"code": 6, "desc": "Montréal"},
        {"code": 7, "desc": "Outaouais"},
        {"code": 8, "desc": "Abitibi-Témiscaminque"},
        {"code": 9, "desc": "Côte-Nord"},
        {"code": 11,"desc":"Nord-du-Québec"},
        {"code": 12,"desc":"Chaudière-Appalaches"},
        {"code": 13,"desc":"Laval"},
        {"code": 14,"desc":"Laurentides"},
        {"code": 15,"desc":"Montérégie"},
        {"code": 16,"desc":"Lanaudière"},
        {"code": 17,"desc":"Centre-du-Québec"},
        {"code": 18,"desc":"Gaspésie-Iles-de-la-Madeleine"},
        {"code": 19,"desc":"Hors Québec"}
    ]
    for un_item in regions:
        un_record = Region()
        un_record.code = un_item["code"]
        un_record.desc = un_item["desc"]
        db.session.add(un_record)
        db.session.commit()

def load_nature():
    natures = [
        {"code": 1, "desc": "Approvisionnement (biens)"},
        {"code": 2, "desc": "Services"},
        {"code": 3, "desc": "Travaux de construction"},
        {"code": 4, "desc": "Non défini"},
        {"code": 5, "desc": "Autre"},
        {"code": 6, "desc": "Concession"},
        {"code": 7, "desc": "Vente de biens immeubles"},
        {"code": 8, "desc": "Vente de biens meubles"}
    ]
    for un_item in natures:
        un_record = Nature()
        un_record.code = un_item["code"]
        un_record.desc = un_item["desc"]
        db.session.add(un_record)
        db.session.commit()

def load_type():
    types_ = [
        {"code": 3, "desc": "Contrat adjugé suite à un appel d'offres public"},
        {"code": 9, "desc": "Contrat octroyé de gré à gré"},
        {"code": 10,"desc": "Contrat adjugé suite à un appel d'offres sur invitation"},
        {"code": 14,"desc": "Contrat suite à un appel d'offres sur invitation publié au SEAO"},
        {"code": 16,"desc": "Contrat conclu relatif aux infrastructure de transport"},
        {"code": 17,"desc": "Contrat conclu - Appel d'offres public non publié au SEAO"}
    ]
    for un_item in types_:
        un_record = Type()
        un_record.code = un_item["code"]
        un_record.desc = un_item["desc"]
        db.session.add(un_record)
        db.session.commit()


#
# Menu display function
#
def print_menu():
    print(f"███████╗███████╗ █████╗  ██████╗     ██╗      ██████╗  █████╗ ██████╗ ███████╗██████╗ ")
    print(f"██╔════╝██╔════╝██╔══██╗██╔═══██╗    ██║     ██╔═══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗")
    print(f"███████╗█████╗  ███████║██║   ██║    ██║     ██║   ██║███████║██║  ██║█████╗  ██████╔╝")
    print(f"╚════██║██╔══╝  ██╔══██║██║   ██║    ██║     ██║   ██║██╔══██║██║  ██║██╔══╝  ██╔══██╗")
    print(f"███████║███████╗██║  ██║╚██████╔╝    ███████╗╚██████╔╝██║  ██║██████╔╝███████╗██║  ██║")
    print(f"╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝")
    print(f"\n")
    print(f"py seao.py --initdb      : Dangerous use with caution, reset databases")
    print(f"py seao.py --load <file> : load xml avis file (path:/DATA/SEAO/..., please indicate year/filename)")
    print(f"py seao.py --region      : load description list for Region")
    print(f"py seao.py --nature      : load description list for Nature")
    print(f"py seao.py --type        : load description list for Type")
    print(f"\n")

# mytree = ET.parse('test.xml')
# myroot = mytree.getroot()
# print(f"myroot: {myroot.tag}")

if len(sys.argv) > 1:
    if sys.argv[1] == '--initdb':
        db.drop_all()
        db.create_all()
        print(f"\n\nAll tables defined by models were reset to empty\n\n")

    if sys.argv[1] == '--region':
        load_regions()

    if sys.argv[1] == '--type':
        load_type()

    if sys.argv[1] == '--nature':
        load_nature()

    if len(sys.argv) > 1:
        if sys.argv[1] == '--load':
            load_db_from_xml_file(sys.argv[2])

print_menu()


