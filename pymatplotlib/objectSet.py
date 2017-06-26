# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 23:29:24 2017

@author: mi_o3
"""
import matplotlib.pyplot as plt
import numpy as np

class objectSet():
    
    def __init__(self, cx,cy,w,h,lw,lxs,lxe):
        self.rect= np.array([cx,cy,w,h])
        self.line_width = lw
        self.line_xs = lxs
        self.line_xe = lxe
        
    def plot_rect(self,ax):
        obj_rect = plt.Rectangle(((self.rect[0] - (self.rect[2]/2)),(self.rect[1] - (self.rect[3]/2))),self.rect[2],self.rect[3],edgecolor="#ff0000",fill=False,lw=2)
        obj_poly = plt.Polygon(((self.rect[0],(self.rect[1] + (self.rect[3]/2))),(self.rect[0],(self.rect[1] - (self.rect[3]/2))),((self.rect[0] + (self.rect[2]/2)),self.rect[1])),edgecolor="#ff0000",fill=False,lw=2)
        ax.add_patch(obj_rect)
        ax.add_patch(obj_poly)
        
    def plot_line(self):
        x = np.array([self.line_xs,self.line_xe])
        y = np.array([self.rect[1] - self.line_width/2, self.rect[1] - self.line_width/2])
        plt.plot(x,y,color="#000000",lw=1)
        x = np.array([self.line_xs,self.line_xe])
        y = np.array([self.rect[1] + self.line_width/2, self.rect[1] + self.line_width/2])
        plt.plot(x,y,color="#000000",lw=1)

if __name__ == '__main__':
    fig = plt.figure()
    ax = fig.add_subplot(111)
    obj = objectSet(-1,20,5,1.7,3,-10,10)
    obj.plot_rect(ax)
    obj.plot_line()
    plt.show()