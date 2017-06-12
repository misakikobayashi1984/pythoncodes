# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 07:34:27 2017

@author: mi_o3
"""

import sys
import struct

# PPMからRAWに変換
inFname = 'tmp1.ppm'
outFname = 'tmp1.raw'

infile = open(inFname, 'r')
outfile = open(outFname, 'w')

for i in range(3):
    d = infile.readline()

#RAW形式として保存
data = infile.read()
odata = ''
for i in range(len(data)/3):
    r = ord(data[3*i])/2
    odata += struct.pack('B', r)

outfile.write(odata)

infile.close()
outfile.close()