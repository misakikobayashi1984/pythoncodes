# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 06:34:03 2017

@author: mi_o3
"""

import sys
import struct

d_array = [2,3,4,5]
fout = open('d_array.raw', 'wb')
for i in range(len(d_array)):
    # byte列に変換
    # ′B' = chr
    # 'f' = float
    fout.write(struct.pack('B', d_array[i]))
fout.close()