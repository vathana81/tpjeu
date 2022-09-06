#!/usr/bin/env python
#-- coding:utf-8 --

import random

def createPerso(pseudo,pv,force,armure):
    arrayPerso=""
    arrayPerso[pseudo,pv,force,armure]
    return arrayPerso

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

    