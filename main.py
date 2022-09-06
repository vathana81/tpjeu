# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 15:47:37 2022
@author: Administrateur
"""

import creationPerso.py, generationMonstre.py, cptr.py, createMonster.py, degats.py, gestioncombat.py

compteurKills= 0
playAgain = 0
persoMort = ""

while playAgain == 0:
    statPerso = creationPerso.createPerso("Louis",20,50,15)
    
    while statPerso[1] > 0:
        monstre = createMonster.createMonster()
        gestioncombat.gestioncombat(statPerso, monstre)
        
    if statPerso[1] > 0:
        compteurKills=cptr.compteur(compteurKills)
    if statPerso[1] <= 0:
        while persoMort!="O" or persoMort!="N":
            persoMort=input("Continuer 'O' ou 'N'")
    if persoMort=="O":
        print("Continuez à jouer !")
        playAgain = 0
    elif persoMort=="N":
        print("Game Over !")
        playAgain = 1
