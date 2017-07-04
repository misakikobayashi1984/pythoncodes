# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 21:08:52 2017

@author: mi_o3
"""

import numpy as np
import matplotlib.pyplot as plt
import math

tnum = 10
dt = 0.1
acc = 0.1

x_est = np.array([[0, 0]]).T
P_est = np.array([[0, 0],[0, 0]])
F = np.array([[1, dt],[0, 1]])
G = np.array([[0.5*dt**2, dt]]).T
w = acc
H = np.array([[1, 0],[0, 1]])
R = np.array([[1, 0],[0, 1]])#観測値にのるノイズの共分散行列
Q = np.array([[1, 0],[0, 1]])#観測値にのるノイズの共分散行列

x_est_array = []
z_array = []
x_klm_array = []
t_array_0 = []
t_array = []

x_est_array.append(x_est)
t_array_0.append(0)

for i in range(tnum):
    x_est = F.dot(x_est) + G*w
    P_est = F.dot(P_est).dot(F.T) + Q
    
    z = H.dot(x_est) + np.array([[np.random.normal(0,R[0,0]), np.random.normal(0,R[1,1])]]).T
    e = z - H.dot(x_est)
    S = R + H.dot(P_est).dot(H.T)
    K = P_est.dot(H.T).dot(np.linalg.inv(S))

    x_klm = x_est + K.dot(e)
    P_klm = (np.matrix(np.identity(2)) - K.dot(H)).dot(P_est)
        
    x_est_array.append(x_est)
    z_array.append(z)
    x_klm_array.append(x_klm)
    
    t_array_0.append((i+1)*dt)
    t_array.append((i+1)*dt)
    
    ''' 更新 '''
    x_est = x_klm
    P_est = P_klm
    
x_est_array_pos = []
for i in range(len(x_est_array)):
    x_est_array_pos.append(x_est_array[i][0,0])

z_array_pos = []
x_klm_array_pos = []
for i in range(len(z_array)):
    z_array_pos.append(z_array[i][0,0])   
    x_klm_array_pos.append(x_klm_array[i][0,0]) 
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(t_array_0,x_est_array_pos,color='red',marker='o',label='gt')
ax.plot(t_array,z_array_pos,color='blue',marker='o',label='signal')
ax.plot(t_array,x_klm_array_pos,color='orange',marker='o',label='signal filtered')
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.legend(loc="lower right")