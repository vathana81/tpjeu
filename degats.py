#!/usr/bin/env python3
# -*- coding: utf-8 -*-
pv_perso1=50
pv_perso2=10
force=7
armure=2
def attaque():
    coup=force-armure
    pv_restant=(pv_perso1-coup)
    print(pv_restant)
attaque()