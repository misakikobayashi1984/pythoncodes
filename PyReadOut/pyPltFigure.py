# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 20:32:37 2017

@author: mi_o3
"""

import random
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib as plt

from PyQt5.QtCore import (QLineF, QPointF, QRectF, Qt, QTimer)
from PyQt5.QtGui import (QBrush, QColor, QPainter)
from PyQt5.QtWidgets import (QApplication, QGraphicsView, QGraphicsScene, QGraphicsItem,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QSizePolicy,
                             QLabel, QLineEdit, QPushButton)

# FigureCanvas inherits QWidget
class MainWindow(FigureCanvas):
    def __init__(self, parent=None):
        fig = Figure()
        #1行1列に1つのグラフを描画
        self.axes = fig.add_subplot(111)
        self.axes.hold(False)

        super(MainWindow, self).__init__(fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        SIZE_X = 41
        SIZE_Y = 61
        self.d_array = []
        for y in range(SIZE_Y):
             for x in range(SIZE_X):
                  if y < ( SIZE_Y / 2 ):
                      self.d_array.append(0)
                  else:
                      self.d_array.append(1)
        self.d_array = np.array(self.d_array).reshape(SIZE_Y,SIZE_X)

        self.setWindowTitle("Sin Curve")
        self.set_figure()
        
    def set_figure(self):
        self.axes.imshow( self.d_array )

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()

    mainWindow.show()
    sys.exit(app.exec_())