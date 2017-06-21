# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 21:08:49 2017

@author: mi_o3
"""

#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

This example shows a QSlider widget.

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
from PyQt5.QtWidgets import (QWidget, QSlider, 
    QLabel, QApplication)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):      

        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setGeometry(30, 40, 100, 30)
        sld.valueChanged[int].connect(self.changeValue)
        
        #self.label = QLabel(self)
        #self.label.setPixmap(QPixmap('mute.png'))
        #self.label.setGeometry(160, 40, 80, 30)
        
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('QSlider')
        self.show()
        
        
    def changeValue(self, value):

        if value == 0:
            print('value == 0')
        elif value > 0 and value <= 30:
            print('value > 0 and value <= 30')
        elif value > 30 and value < 80:
            print('value > 30 and value < 80')
        else:
            print(' ')
            

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_()) 