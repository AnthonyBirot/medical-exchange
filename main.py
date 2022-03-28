#!/usr/bin/env python3

from Patient import Patient
from Practicien import Practicien

email_p = "martin@gmail.com"
mdp_p = "toto"

#Le patient s'identifie sur la plateforme
patient1 = Patient(email_p, mdp_p)

#Il crée son compte en remplissant ses informations personnelles
patient1.register("Martin", 185, 90.5)

email_pra = "doc@gmail.com"
mdp_pra = "tata"

#Le practicien s'identifie sur la plateforme
practicien1 = Practicien(email_pra, mdp_pra)

#Le practitien ajoute le patient 1 à sa liste
practicien1.add_patient(patient1)

#Le practicien veut avoir accès aux données du patient 1
practicien1.check_patient_data(email_p)