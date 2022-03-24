import json
from typing import List
from random import randrange


class Patient():
    #Creation d'un nouveau compte patient avec identification pour lui permettre
    # d'avoir accès à ses propres données.
    def __init__(self, email: str, password: str):
        self.id = str(randrange(100))
        self.email = email
        self.password = password

        #On admet que le json créé est l'equivalent d'une base de données ou l'on pourra
        # retrouver les différentes data du patient.
        #Du simple nom, taille ou poids, au calendrier de disponibilités du patient en passant
        # par son historique d'interventions
        #Voir data_exemple.json
        self.json_file_name = "data." + self.id + ".json"
        with open(self.json_file_name, 'w') as f:
            print("New patient datas file")

    #Le patient peut s'inscrire en renseignant ses informations personnelles
    def register(self, name: str, taille: int, poids: float):
        print("Notif de nouveau patient")

    #Le patient peut ajouter des interventions passées pour compléter son historique
    def add_past_event(self, date: str, organisme: str, lieu: str, description: str):
        pass
    
    #Le patient peut ajouter ses disponibilité ou un rendez-vous avec un practicien sur son calendrier perso 
    def book_event(self, date: str, organisme: str, lieu: str, description: str):
        pass
    