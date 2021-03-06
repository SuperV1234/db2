from pprint import pprint
from query import *
import json

def caricaDatiDaJson(jsonFile):
    with open(jsonFile) as data_file:
        data = json.load(data_file)
        return data

def popolaPazienti(data,db):
    for i in data['patients']:
        queryInserisciPaziente(db, i['id'], i['surname'], i['name'], i['date_of_birth'], i['address'], i['telephone'], i['email'])

def popolaDevices(data,db):
    for i in data['devices']:
        queryInserisciDevice(db, i['id'], i['manufacturer'], i['model'])

def popolaParametri(data,db):
    for i in data['parameters']:
        queryInserisciParametri(db, i['id'], i['description'], i['frequency'])

def popolaOsservazione(data,db):
    for i in data['observations']:
        queryInserisciOsservazioni(db, i['id'], i['timestamp'], i['value'],i['uom'])

def popolaTerapia(data,db):
    for i in data['therapies']:
        queryInserisciTerapia(db, i['id'], i['starting_time'], i['duration'],i['medicine'], i['posology'])

def popolaSalute(data,db):
    for i in data['health_states']:
        queryInserisciSalute(db, i['id'], i['timestamp'], i['disease_type'], i['disease_degree'])

def popolaDottore(data,db):
    for i in data['doctors']:
        queryInserisciDottore(db, i['id'], i['name'], i['surname'])

def popolaInstall(data,db):
    for i in data['install']:
        queryInserisciInstallazione(db, i['id'], i['where'], i['when'], i['id_patients'], i['id_devices'])

def popolaMisurazioni(data,db):
    for i in data['measurement']:
        queryInserisciMisurazioni(db, i['id'], i['id_devices'], i['id_parameters'])

def popolaEffetto(data,db):
    for i in data['affect']:
        queryInserisciEffetto(db, i['id'], i['id_observations'], i['id_health_states'])

def popolaValutare(data,db):
    for i in data['evaluate']:
        queryInserisciValutare(db, i['id'], i['id_doctors'], i['id_health_states'])

def popolaSettare(data,db):
    for i in data['set']:
        queryInserisciSettare(db, i['id'], i['id_therapies'], i['id_health_states'])

def popolaMonitoraggio(data,db):
    for i in data['monitoring']:
        queryInserisciMonitoraggio(db, i['id'], i['id_observations'], i['id_parameters'])

def popolaRelativo(data,db):
    for i in data['related']:
        queryInserisciRelativo(db, i['id'], i['id_health_states'], i['id_patients'])

def popolaTutto(data,db):
    popolaPazienti(data,db)
    popolaDevices(data,db)
    popolaDottore(data,db)
    popolaEffetto(data,db)
    popolaInstall(data,db)
    popolaMisurazioni(data,db)
    popolaMonitoraggio(data,db)
    popolaOsservazione(data,db)
    popolaParametri(data,db)
    popolaRelativo(data,db)
    popolaSalute(data,db)
    popolaSettare(data,db)
    popolaTerapia(data,db)
    popolaValutare(data,db)