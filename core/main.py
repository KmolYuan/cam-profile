# -*- coding: utf-8 -*-

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from .Ui_main import Ui_MainWindow
from .canvas import camProfile

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.camProfile = camProfile()
        self.canvasLayout.addWidget(self.camProfile)
        self.camProfile.changeType(True)
    
    @pyqtSlot()
    def on_toHar_clicked(self): self.camProfile.changeType(True)
    @pyqtSlot()
    def on_toCy_clicked(self): self.camProfile.changeType(False)
    @pyqtSlot(bool)
    def on_showBase_clicked(self, checked): self.camProfile.setShowBase(checked)
    @pyqtSlot(bool)
    def on_showRoute_clicked(self, checked): self.camProfile.setShowCutterRoute(checked)
    
    @pyqtSlot(int)
    def on_rotateBar_valueChanged(self, value):
        self.camProfile.setAngle(value)
    
    @pyqtSlot(int)
    def on_zoomBar_valueChanged(self, value):
        self.camProfile.setRate(value)
