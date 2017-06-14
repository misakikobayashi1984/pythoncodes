# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:20:45 2017

@author: mi_o3
"""
import sys
import struct

SIZE_X = 41
SIZE_Y = 61
SIZE_Z = 999

d_array = []
for z in range(SIZE_Z):
    for y in range(SIZE_Y):
        for x in range(SIZE_X):
            if y < ( SIZE_Y / 2 ):
                d_array.append(0)
            else:
                d_array.append(1)

fout = open('d_array.raw', 'wb')
for i in range(len(d_array)):
    # byte列に変換
    # ′B' = chr
    # 'f' = float
    fout.write(struct.pack('f', d_array[i]))
fout.close()