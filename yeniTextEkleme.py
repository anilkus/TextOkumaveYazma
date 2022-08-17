# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 12:45:41 2022

@author: LENOVO
"""

with open('C:/Users/LENOVO/Desktop/text.txt','r') as readfile:
    with open('C:/Users/LENOVO/Desktop/Example3.txt','a+') as writefile:
          for line in readfile:
                writefile.write(line)