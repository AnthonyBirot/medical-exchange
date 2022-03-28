import json
from typing import List
from random import randrange

from Patient import Patient


class Practicien(object):
    #Un practicien (medecin, hopital, kine, ...) peut se connecter sur la plateforme avec ses identifiants
    def __init__(self, email: str, password: str) -> None:
        self.id: str = str(randrange(100))
        self.email: str = email
        self.password: str = password

        #Un practicien possède une liste de patients desquels il pourra checker les données stockées
        # dans la base de données
        #Cette liste pourra étre update losque qu'un patient prendra rendez vous via son calendrier
        # avec le practicien en question ou lorsqu'un autre practicien aura décidé de passer la main
        # (généraliste => kiné, médecin => chirurgien, ...)
        self.patients: List[Patient] = []

    #Le practicien peut ajouter un patient à sa liste de patients
    def add_patient(self, p: Patient) -> None:
        self.patients.append(p)

    #Le practicien peut checker les datas de son patient dans la base de données
    def check_patient_data(self, email: str) -> str:
        patient: Patient = None
        json_data: str = ""

        for p in self.patients:
            if p.email == email:
                patient = p
            else:
                print("Vous n'avez pas accès aux données de ce patient")
                return json_data
        
        json_file_name: str = "data" + patient.id + ".json"
        f = open(json_file_name, "r")
        data = json.loads(f.read())
        json_data = json.dumps(data)
        f.close()

        print(json_data)
        return json_data

    #Le practicien peut checker l'historique des interventions du patient
    def check_patient_past_event(self, email:str) -> str:
        patient_event:str = ""
        
        #TO DO

        return patient_event

    #Le practicien peut checker les interventions du patient prévu dans son calendrier
    def check_patient_event(self, email:str) -> str:
        patient_event:str = ""
        
        #TO DO

        return patient_event

    #Le practicien peut programmer des rendez vous pour un patient
    # Cela notifie le patient en question et ajoute un event dans son calendrier
    def book_event(self, email:str, date: str, organisme: str, lieu: str, description: str) -> None:
        print("Un nouveau rendez-vous est enregistré")