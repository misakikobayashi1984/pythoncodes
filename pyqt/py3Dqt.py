# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 22:43:39 2017

@author: mi_o3
"""

from matplotlib import pyplot
from scipy import genfromtxt
from mpl_toolkits.mplot3d import Axes3D
import sys
import struct
import seaborn as sns
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QSlider,
    QTextEdit, QGridLayout, QApplication, QSizePolicy)



class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        # ファイル読み込み
        d = genfromtxt("iris.csv", delimiter=",")

        # 軸ラベルの設定
        #ax.set_xlabel("X-axis")
        #ax.set_ylabel("Y-axis")
        #ax.set_zlabel("Z-axis")

        # 表示範囲の設定
        #ax.set_xlim(4, 8)
        #ax.set_ylim(2, 5)
        #ax.set_zlim(1, 8)

        # 抽出条件設定
        d1 = d[d[:,0] >= 7]
        d2 = d[(d[:,0] < 7) & ((d[:,1] > 3) & (d[:,1] <= 3.5))]
        d3 = d[(d[:,0] < 7) & ((d[:,1] <= 3) | (d[:,1] > 3.5))]
        
        self.d_array2D = d1
        
        fig = pyplot.figure()
        self.fig_canvas = FigureCanvas(fig)
        self.axes = Axes3D(fig)
        self.axes.plot(d1[:,0], d1[:,1], d1[:,2], "o", color="#cccccc", ms=4, mew=0.5)
        ##sns.heatmap(self.d_array2D, vmin=0, vmax=7, annot=False, ax=self.axes)
        self.fig_canvas.draw()
        
        #slder
        self.SIZE_Z = 999
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.setRange(0, self.SIZE_Z-1)
        sld.valueChanged[int].connect(self.changeValue)        

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(sld, 1, 0)
        grid.addWidget(self.fig_canvas, 2, 0)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()
        
    def changeValue(self, value):
       # self.set_figure(value)
        print('self.idx_z: ', self.idx_z)
            
    def set_figure(self, idx_z_):
        self.d_array2D = []
        self.idx_z = idx_z_
        for y in range(self.SIZE_Y):
            for x in range(self.SIZE_X):
                idx = x + self.SIZE_X * ( y + self.SIZE_Y * self.idx_z)
                self.d_array2D.append(self.d_array[idx])
        self.d_array2D = np.array(self.d_array2D).reshape(self.SIZE_Y,self.SIZE_X)
        sns.heatmap(self.d_array2D, vmin=0, vmax=7, annot=False, ax=self.axes, cbar = False)
        self.fig_canvas.draw()
        
    def saveRawImg(self, d_array):
        fout = open('d_array.raw', 'wb')
        for i in range(len(d_array)):
            fout.write(struct.pack('f', d_array[i]))
        fout.close()
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())