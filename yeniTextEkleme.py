# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:45:41 2022

@author: AnilKus
"""

with open('Varolan dosyanın yolu','r') as readfile:
    with open('yeni ekleyeceğiniz dosyanın yolu','a+') as writefile:
          for line in readfile:
                writefile.write(line)
