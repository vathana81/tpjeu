# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:47:37 2022

@author: Administrateur
"""

import creationPerso, generationMonstre
from compteur import *

compteurKills= 0
playAgain = 0

while playagain == 0:
    nomPerso = input("choisissez un perso : ")
    monPerso = personnage.personnage(nomPerso,20,6,3)
    while monPerso[1] > 0:
        Ennemi = creationMonstre.creationMonstre()
        fight.fight(monPerso, Ennemi)
        
    if monPerso[1] > 0:
        compteurKills=compteurEnnemiisTrue(compteurKills)