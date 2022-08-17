# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:27:09 2022

@author: LENOVO
"""

Liste=["AHMET","ela","Kuş","5","Toros Üniversitesi"]

with open ("C:/Users/LENOVO/Desktop/text.txt","w",encoding="utf-8") as ozet:
    
    for satir in Liste:
        ozet.write(satir)
        print(ozet)