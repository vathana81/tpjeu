# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 14:00:36 2022

@author: Administrateur
"""
import random
def degatMonstre(pseudo):
    pv=random.randint(5,20)
    force=random.randint(3,8)
    armure=random.randint(0,5)
    arrayDegat=[pseudo,pv,force,armure]
    return arrayDegat
a=degatMonstre("martin")
print(a)
   

def degatPerso(array,degats):
    pvRestant=""
    pvRestant=array[1]-degats
    return pvRestant