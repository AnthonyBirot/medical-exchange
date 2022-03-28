import json
import typing
from random import randrange

class Patient(object):
    #Creation d'un nouveau compte patient avec identification pour lui permettre
    # d'avoir accès à ses propres données.
    def __init__(self, email: str, password: str) -> None:
        self.id: str = str(randrange(100))
        self.email: str = email
        self.password: str = password

        #On admet que le json créé est l'equivalent d'une base de données ou l'on pourra
        # retrouver les différentes data du patient.
        #Du simple nom, taille ou poids, au calendrier de disponibilités du patient en passant
        # par son historique d'interventions
        #Voir data_exemple.json
        self.json_file_name: str = "data" + self.id + ".json"

    #Le patient peut s'inscrire en renseignant ses informations personnelles
    def register(self, name: str, taille: int, poids: float) -> None:
        json_dict = {"name" : name, "taille" : taille, "poids": poids}
        json_string = json.dumps(json_dict)

        with open(self.json_file_name, "w") as f:
            f.write(json_string)

        print("Nouvelle fiche patient")

    #Le patient peut ajouter des interventions passées pour compléter son historique
    def add_past_event(self, date: str, organisme: str, lieu: str, description: str) -> None:
        print("Update de l'historique du patient")
    
    #Le patient peut ajouter ses disponibilité ou un rendez-vous avec un practicien sur son calendrier perso 
    def book_event(self, date: str, organisme: str, lieu: str, description: str) -> None:
        print("Un nouveau rendez-vous est enregistré")
    