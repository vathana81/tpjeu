#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#force_att=7
#armure_def=2
#def attaque():
#    coup=force_att-armure_def
#    print(coup)
#attaque()

def gestDegats(pvdef, forceatt, armuredef):
    if (forceatt-armuredef):
        return pvdef-(forceatt-armuredef)
    else:
        return pvdef-1