# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 20:54:09 2017

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

x_0 = 10
vlc_mps = vlc / 3.6

P = 0
x_hat = 0

x_est_array = []
x_tr_array = []
z_array = []
x_klm_array = []

for t in np.arange(0, T, dt):
    x_tr = vlc_mps * t + x_0
    x_tr_array.append(x_tr)
    
    x_hat_minus = x_hat
    P_minus = P + Q
    
    x_est_array.append(x_hat_minus)
    
    z = x_tr + np.random.normal(0, R)
    z_array.append(z)
    
    S = P_minus + R
    K = P_minus / S
    x_hat = x_hat_minus + K*(z - x_hat_minus)
    P = (1-K) * P_minus
    
    x_klm_array.append(x_hat)

fig = plt.figure()
ax = fig.add_subplot(111)    
ax.plot(np.arange(0, T, dt), x_tr_array, color='red',marker='o',label='gt')
ax.plot(np.arange(0, T, dt), z_array, color='blue',marker='o',label='observed')
ax.plot(np.arange(0, T, dt), x_klm_array, color='orange',marker='o',label='filtered')
#ax.plot(np.arange(0, T, dt), x_est_array, color='cyan',marker='o',label='x_est_array')
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.legend(loc="lower right")