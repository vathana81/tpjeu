#!/Usr/bin/env python
#-- coding:utf-8 --

arrayPerso=""
arrayDegat=""
pvRestant=""

def createPerso(pseudo,pv,force,armure):
    arrayPerso[pseudo,pv,force,armure]
    return arrayPerso

def degat(pseudo,pv,force,armure):
    arrayDegat[pseudo,pv,force,armure]
    return arrayDegat

def degatPerso(array,degats):
    pvRestant=array[1]-degats
    return pvRestant

