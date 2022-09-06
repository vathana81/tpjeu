#!/usr/bin/env python3
#--coding:utf-8--

from degats.py import *

def gestioncombat(statjoueur,statmonstre):
    while True:
        statmonstre[1]=gestDegats(statmonstre[1],statjoueur[2],statmonstre[3])
        print("Il reste ", statmonstre[1], "HP au monstre")
        if statmonstre[1]>=0:
            statjoueur[1]=gestDegats(statjoueur[1],statmonstre[2],statjoueur[3])
            print("Il reste ", statjoueur[1], "HP au monstre")
        
        if statmonstre[1]<=0:
            print("Monstre mort")
            break
        if statjoueur[1]<=0:
            print("Joueur mort")
            break











