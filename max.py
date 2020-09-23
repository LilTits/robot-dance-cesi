#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 11:45:01 2020

@author: cesi
"""
from pypot.creatures import PoppyErgoJr
poppy = PoppyErgoJr(
    simulator='vrep', 
    scene='poppy_ergo_jr_holder.ttt', 
    camera='dummy'
    )