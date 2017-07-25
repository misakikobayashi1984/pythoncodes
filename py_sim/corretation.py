# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 09:33:09 2017

@author: mi_o3
"""


import numpy as np
import matplotlib.pyplot as plt
import math

T = 5 #[s]
dt = 0.1 #[s]
vlc = 30 #[kph]

R = 10
Q = 1

x_0 = -10
y_0 = 0
vlc_mps = vlc / 3.6

y_array = []
x_array = []

y_array_sig1 = []
x_array_sig1 = []

y_array_sig2 = []
x_array_sig2 = []

for t in np.arange(0, T, dt):
    x = vlc_mps * t + x_0
    y = y_0
    x_array.append(x)
    y_array.append(y)
    
    x_sig1 = x + np.random.normal(0,0.1)
    y_sig1 = y + np.random.normal(0,0.01)
    x_array_sig1.append(x_sig1)
    y_array_sig1.append(y_sig1)
    
    x_sig2 = 0 + np.random.normal(0,0.01)
    y_sig2 = 0 + np.random.normal(0,0.01)
    x_array_sig2.append(x_sig2)
    y_array_sig2.append(y_sig2)
 
x_array = np.array(x_array)
y_array = np.array(y_array)

x_array_sig1 = np.array(x_array_sig1)
y_array_sig1 = np.array(y_array_sig1)

x_array_sig2 = np.array(x_array_sig2)
y_array_sig2 = np.array(y_array_sig2)

# crr計算
crrsig_a = np.append(x_array, y_array)
crrsig_b = np.append(x_array_sig1, y_array_sig1)
crrsig_c = np.append(x_array_sig2, y_array_sig2)

crrsig_a = crrsig_a - np.min(crrsig_a)
crrsig_b = crrsig_b - np.min(crrsig_b)
crrsig_c = crrsig_c - np.min(crrsig_c)

crrval_a = np.correlate(crrsig_a,crrsig_a)
crrval_b = np.correlate(crrsig_a,crrsig_b)
crrval_c = np.correlate(crrsig_a,crrsig_c)

print('crr val: ', crrval_a,crrval_b,crrval_c)

#dist計算
diffx = x_array - x_array
diffy = y_array - y_array
dist_ar = diffx *diffx + diffy*diffy
dist = 0
for val in dist_ar:
    dist += val

diffx_sig1 = x_array - x_array_sig1
diffy_sig1 = y_array - y_array_sig1
dist_sig1_ar = diffx_sig1 *diffx_sig1 + diffy_sig1*diffy_sig1
dist_sig1 = 0
for val in dist_sig1_ar:
    dist_sig1 += val
    
diffx_sig2 = x_array - x_array_sig2
diffy_sig2 = y_array - y_array_sig2
dist_sig2_ar = diffx_sig2 *diffx_sig2 + diffy_sig2*diffy_sig2
dist_sig2 = 0
for val in dist_sig2_ar:
    dist_sig2 += val
    
print('dist val: ', dist,dist_sig1,dist_sig2)

fig = plt.figure()
ax = fig.add_subplot(111)    
ax.plot(x_array, y_array, color='red',marker='o',label='gt')
ax.plot(x_array_sig1, y_array_sig1, color='blue',marker='o',label='sig1')
ax.plot(x_array_sig2, y_array_sig2, color='orange',marker='o',label='sig2')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend(loc="lower right")