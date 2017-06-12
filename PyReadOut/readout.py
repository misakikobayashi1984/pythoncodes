# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 05:36:17 2017

@author: mike
"""

import sys
import struct

inFname = 'tmp1.ppm'
outFname = 'tmp2.ppm'

infile = open(inFname, 'r')
outfile = open(outFname, 'w')

for i in range(3):
    d = infile.readline()
    outfile.write(d)

data = infile.read()
odata = ''
for i in range(len(data)/3):
    r = ord(data[3*i])/2
    g = ord(data[3*i+1])/2
    b = ord(data[3*i+2])/2
    odata += struct.pack('BBB', r, g, b)

outfile.write(odata)

infile.close()
outfile.close()