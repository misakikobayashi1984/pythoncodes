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
    QTextEdit, QGridLayout, QApplication, QSizePolicy, QPushButton)
import random

SIZE_Z = 50
SIZE_Y = 30
SIZE_X = 20

class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        
        self.Max_th = 1.0
        self.Min_th = 0.9
        
        #3D画像生成
        self.img_3d = []
        for z in range(SIZE_Z):
            for y in range(SIZE_Y):
                for x in range(SIZE_X):
                    val = random.random()
                    self.img_3d.append(val)        
        self.img_3d = np.array(self.img_3d)
        
        idxes_x = []
        idxes_y = []
        idxes_z = []
        img_3d_show = []
        for z in range(SIZE_Z):
            for y in range(SIZE_Y):
                for x in range(SIZE_X):
                    img_idx = x + SIZE_X * ( y + SIZE_Y * z)
                    val = self.img_3d[img_idx]
                    if val < self.Max_th and val > self.Min_th:
                        idxes_x.append(x)
                        idxes_y.append(y)
                        idxes_z.append(z)
                        img_3d_show.append(val)
                        
        img_3d_show = np.array(img_3d_show)
        print("max min ", img_3d_show.max(), img_3d_show.min())
        print("len x,y,z,img_3d ",len(idxes_x), len(idxes_y), len(idxes_z), len(img_3d_show))
        
        fig = pyplot.figure()
        self.fig_canvas = FigureCanvas(fig)
        self.axes = Axes3D(fig)
        cm = pyplot.cm.get_cmap('jet')
        self.axes.scatter(idxes_x,idxes_y,idxes_z,c=img_3d_show,cmap=cm)
        self.fig_canvas.draw()
        
        #
        self.b1 = QPushButton('set')
        self.b1.setCheckable(True)
        self.b1.clicked.connect(self.btnstate)
        
        l1 = QLabel("max")
        l2 = QLabel("min")
        self.e1 = QLineEdit()
        self.e2 = QLineEdit()
        
        #
        grid = QGridLayout()
        grid.addWidget(self.fig_canvas, 1, 0)
        grid.addWidget(l1, 2, 0)
        grid.addWidget(self.e1, 2, 1)
        grid.addWidget(l2, 3, 0)
        grid.addWidget(self.e2, 3, 1)
        grid.addWidget(self.b1, 4, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()
        
    def btnstate(self):
      if self.b1.isChecked():
        print("button pressed")
        self.Max_th = float(self.e1.text())
        self.Min_th = float(self.e2.text())
        
        self.axes.clear()
        #3D画像表示
        idxes_x = []
        idxes_y = []
        idxes_z = []
        img_3d_show = []
        for z in range(SIZE_Z):
            for y in range(SIZE_Y):
                for x in range(SIZE_X):
                    img_idx = x + SIZE_X * ( y + SIZE_Y * z)
                    val = self.img_3d[img_idx]
                    if val < self.Max_th and val > self.Min_th:
                        idxes_x.append(x)
                        idxes_y.append(y)
                        idxes_z.append(z)
                        img_3d_show.append(val)
                        
        img_3d_show = np.array(img_3d_show)
        print("max min ", img_3d_show.max(), img_3d_show.min())
        print("len x,y,z,img_3d ",len(idxes_x), len(idxes_y), len(idxes_z), len(img_3d_show))
        
        #fig = pyplot.figure()
        #self.fig_canvas = FigureCanvas(fig)
        #self.axes = Axes3D(fig)
        cm = pyplot.cm.get_cmap('jet')
        self.axes.scatter(idxes_x,idxes_y,idxes_z,c=img_3d_show,cmap=cm)
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