# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 21:19:51 2017

@author: mi_o3
"""

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a bit
more complicated window layout using
the QGridLayout manager. 

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

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
        
        #figure
        self.SIZE_X = 41
        self.SIZE_Y = 61
        self.SIZE_Z = 999        
        self.d_array = []
        for z in range(self.SIZE_Z):
            for y in range(self.SIZE_Y):
                for x in range(self.SIZE_X):
                    if (y < ( self.SIZE_Y / 2 )) and (x < ( self.SIZE_X / 2 )) and (z < ( self.SIZE_Z / 2 )):
                        self.d_array.append(0)
                    elif (y < ( self.SIZE_Y / 2 )) and (x >= ( self.SIZE_X / 2 )) and (z < ( self.SIZE_Z / 2 )):
                        self.d_array.append(1)
                    elif (y >= ( self.SIZE_Y / 2 )) and (x < ( self.SIZE_X / 2 )) and (z < ( self.SIZE_Z / 2 )):
                        self.d_array.append(2)
                    elif (y >= ( self.SIZE_Y / 2 )) and (x >= ( self.SIZE_X / 2 )) and (z < ( self.SIZE_Z / 2 )):
                        self.d_array.append(3) 
                    elif (y < ( self.SIZE_Y / 2 )) and (x < ( self.SIZE_X / 2 )) and (z >= ( self.SIZE_Z / 2 )):
                        self.d_array.append(4)
                    elif (y < ( self.SIZE_Y / 2 )) and (x >= ( self.SIZE_X / 2 )) and (z >= ( self.SIZE_Z / 2 )):
                        self.d_array.append(5)
                    elif (y >= ( self.SIZE_Y / 2 )) and (x < ( self.SIZE_X / 2 )) and (z >= ( self.SIZE_Z / 2 )):
                        self.d_array.append(6)
                    elif (y >= ( self.SIZE_Y / 2 )) and (x >= ( self.SIZE_X / 2 )) and (z >= ( self.SIZE_Z / 2 )):
                        self.d_array.append(7)
        #self.saveRawImg(self.d_array)
        
        self.d_array2D = []
        self.idx_z = 30
        for y in range(self.SIZE_Y):
            for x in range(self.SIZE_X):
                idx = x + self.SIZE_X * ( y + self.SIZE_Y * self.idx_z)
                self.d_array2D.append(self.d_array[idx])
        self.d_array2D = np.array(self.d_array2D).reshape(self.SIZE_Y,self.SIZE_X)
        
        fig = Figure()
        self.axes = fig.add_subplot(111)
        self.fig_canvas = FigureCanvas(fig)
        sns.heatmap(self.d_array2D, vmin=0, vmax=7, annot=False, ax=self.axes)
        self.fig_canvas.draw()
        #self.axes.imshow( self.d_array2D )
    
        #slder
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
        self.set_figure(value)
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