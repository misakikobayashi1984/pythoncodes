# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 22:17:11 2017

@author: mi_o3
"""

#y_dev = D * ( sin(Theta + Alpha) - sin(Theta) )
#= 2 * D * cos(Theta+Alpha/2)*sin(Alpha/2)
#cos(Theta+Alpha/2)*sin(Alpha/2) =  1/2{sin(Theta + Alpha) - sin(Theta)}

#x_dev = D * ( cos(Theta + Alpha) - cos(Theta) )
#= - 2 * D * sin(Theta+Alpha/2)*sin(Alpha/2)
#sin(Theta+Alpha/2)*sin(Alpha/2) =  -1/2{cos(Theta + Alpha) - cos(Theta)}

import numpy as np
import math
import matplotlib.pyplot as plt

range_dist = np.arange(0,100,1)
range_angle = np.arange(-90,90,1)
err_angle = [1.5, 1.5, 3.3, 10]
range_err_angle = [[0,60],[60,70],[70,80],[80,90]]

#angele, dist map
angle_dist_img_x = []
angle_dist_img_y = []
for dst in range_dist:
    for agl in range_angle:
        x_gt = dst * np.sin( math.radians(agl) )
        alpha = 0
        for e_agl, rng_e_agl in zip(err_angle, range_err_angle):
            if rng_e_agl[0] <= abs(agl) and rng_e_agl[1] > abs(agl):
                alpha = e_agl
                break
        x_obs = dst * np.sin( math.radians(agl + alpha) )
        x_err = abs(x_gt - x_obs)
        angle_dist_img_x.append(x_err)
 
angle_dist_img_x = np.array( angle_dist_img_x )
angle_dist_img_x = np.reshape( angle_dist_img_x, (len(range_dist), len(range_angle)) )
plt.imshow(angle_dist_img_x)

#x_di, y_di map