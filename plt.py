# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 21:07:49 2017

@author: mi_o3
"""
import matplotlib.pyplot as plt

f = open("numbers.txt")
data1 = f.readlines()
f.close()
data1

datax = []
datay = []
for i in range( len( data1 ) ):
    a_str, b_str = data1[i].split(" ")
    c_str, tmp = b_str.split("\n")
    datax.append(float( a_str ))
    datay.append(float( c_str ))
    
plt.plot(datax,datay)