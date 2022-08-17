# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:27:09 2022

@author: AnilKus
"""

Liste=["AHMET","ela","Kuş","5","Toros Üniversitesi"]

with open ("Path/Dosya Yolu","w",encoding="utf-8") as ozet:
    
    for satir in Liste:
        ozet.write(satir)
        print(ozet)
