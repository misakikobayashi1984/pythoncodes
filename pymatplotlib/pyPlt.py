# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 22:02:27 2017

@author: mi_o3
"""

# -*- coding: utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def main():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    rect = np.array([-1,20,5,1.7])
    print("rect ", (rect[0] - (rect[2]/2)), (rect[1] - (rect[3]/2)), rect[2],rect[3])
    obj_rect = plt.Rectangle(((rect[0] - (rect[2]/2)),(rect[1] - (rect[3]/2))),rect[2],rect[3],edgecolor="#ff0000",fill=False,lw=2)
    obj_poly = plt.Polygon(((rect[0],(rect[1] + (rect[3]/2))),(rect[0],(rect[1] - (rect[3]/2))),((rect[0] + (rect[2]/2)),rect[1])),edgecolor="#ff0000",fill=False,lw=2)
    ax.add_patch(obj_rect)
    ax.add_patch(obj_poly)
    
    line_width = 3
    x = np.array([-10,20])
    y = np.array([rect[1] - line_width/2, rect[1] - line_width/2])
    plt.plot(x,y,color="#000000",lw=1)
    x = np.array([-10,20])
    y = np.array([rect[1] + line_width/2, rect[1] + line_width/2])
    plt.plot(x,y,color="#000000",lw=1)
    
    x = np.linspace(0,20,20) # 0～3まで20刻みでxの値を生成
    y = x + 1            # 曲線の式(2次関数)
    plt.plot(x,y,"r-")      # 曲線を引く
    plt.show()

if __name__ == '__main__':
    main()