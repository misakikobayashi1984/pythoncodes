# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 20:47:25 2017

@author: mi_o3
"""

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPushButton, QButtonGroup, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QSlider

class FormTest(QDialog):
    def __init__(self, parent=None):
        super(FormTest, self).__init__(parent)

        button1 = QPushButton("一")
        #button1.setCheckable(True)
        button1.setFocusPolicy(Qt.NoFocus)

        button2 = QPushButton("二")
        #button2.setCheckable(True)
        button2.setFocusPolicy(Qt.NoFocus)

        button3 = QPushButton("三")
        #button3.setCheckable(True)
        button3.setFocusPolicy(Qt.NoFocus)

        button4 = QPushButton("四")
        button4.setCheckable(True)
        button4.setFocusPolicy(Qt.NoFocus)

        button5 = QPushButton("五")
        button5.setCheckable(True)
        button5.setFocusPolicy(Qt.NoFocus)

        self.group = QButtonGroup()
        self.group.addButton(button1,1)
        self.group.addButton(button2,2)
        self.group.addButton(button3,3)
        self.group.addButton(button4,4)
        self.group.addButton(button5,5)

        #self.label = QLabel("ラジオボタンをクリックしてください")
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setFocusPolicy(Qt.StrongFocus)
        self.slider.setTickPosition(QSlider.TicksBothSides)
        self.slider.setTickInterval(10)
        self.slider.setSingleStep(1)
        
        #QHboxLayout()は、Horizonal(水平方向に)レイアウトします
        layout = QHBoxLayout()

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addWidget(button4)
        layout.addWidget(button5)


        #QVBoxLayout()は、vertical（垂直方向）にレイアウトします
        Vlayout = QVBoxLayout()

        #Vlayout.addWidget(self.label)
        Vlayout.addWidget(self.slider)
        Vlayout.addLayout(layout)

        self.setLayout(Vlayout)

        button1.clicked.connect(self.clicked)
        button2.clicked.connect(self.clicked)
        button3.clicked.connect(self.clicked)
        button4.clicked.connect(self.clicked)
        button5.clicked.connect(self.clicked)

    def clicked(self):
        button = self.sender()
        if button is None or not isinstance(button,QPushButton):
            return
        #self.label.setText("あなたは '%s' のラジオボタンをクリックしました" % button.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    formtest = FormTest()
    formtest.show()
    app.exec_()