# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/ahshoe/Desktop/CamProfile/core/main.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.harmonic_mode = QtWidgets.QRadioButton(self.centralWidget)
        self.harmonic_mode.setChecked(True)
        self.harmonic_mode.setObjectName("harmonic_mode")
        self.horizontalLayout_2.addWidget(self.harmonic_mode)
        self.cycloidal_mode = QtWidgets.QRadioButton(self.centralWidget)
        self.cycloidal_mode.setObjectName("cycloidal_mode")
        self.horizontalLayout_2.addWidget(self.cycloidal_mode)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.show_base = QtWidgets.QCheckBox(self.centralWidget)
        self.show_base.setChecked(True)
        self.show_base.setObjectName("show_base")
        self.horizontalLayout.addWidget(self.show_base)
        self.show_route = QtWidgets.QCheckBox(self.centralWidget)
        self.show_route.setChecked(True)
        self.show_route.setObjectName("show_route")
        self.horizontalLayout.addWidget(self.show_route)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.baseVal = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.baseVal.setMinimum(1.0)
        self.baseVal.setMaximum(10.0)
        self.baseVal.setProperty("value", 3.0)
        self.baseVal.setObjectName("baseVal")
        self.horizontalLayout.addWidget(self.baseVal)
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lift = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.lift.setMinimum(1.0)
        self.lift.setMaximum(10.0)
        self.lift.setProperty("value", 1.0)
        self.lift.setObjectName("lift")
        self.horizontalLayout.addWidget(self.lift)
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.cutter_radius = QtWidgets.QDoubleSpinBox(self.centralWidget)
        self.cutter_radius.setMinimum(0.5)
        self.cutter_radius.setMaximum(10.0)
        self.cutter_radius.setProperty("value", 0.5)
        self.cutter_radius.setObjectName("cutter_radius")
        self.horizontalLayout.addWidget(self.cutter_radius)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        self.rotate_bar = QtWidgets.QSlider(self.centralWidget)
        self.rotate_bar.setMaximum(360)
        self.rotate_bar.setOrientation(QtCore.Qt.Horizontal)
        self.rotate_bar.setObjectName("rotate_bar")
        self.horizontalLayout_3.addWidget(self.rotate_bar)
        self.rotate_angle = QtWidgets.QSpinBox(self.centralWidget)
        self.rotate_angle.setMaximum(360)
        self.rotate_angle.setSingleStep(10)
        self.rotate_angle.setObjectName("rotate_angle")
        self.horizontalLayout_3.addWidget(self.rotate_angle)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.canvas_layout = QtWidgets.QVBoxLayout()
        self.canvas_layout.setObjectName("canvas_layout")
        self.horizontalLayout_4.addLayout(self.canvas_layout)
        self.zoom_bar = QtWidgets.QSlider(self.centralWidget)
        self.zoom_bar.setMinimum(1)
        self.zoom_bar.setMaximum(50)
        self.zoom_bar.setPageStep(1)
        self.zoom_bar.setProperty("value", 30)
        self.zoom_bar.setOrientation(QtCore.Qt.Vertical)
        self.zoom_bar.setObjectName("zoom_bar")
        self.horizontalLayout_4.addWidget(self.zoom_bar)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.harmonic_mode.setText(_translate("MainWindow", "Harmonic"))
        self.cycloidal_mode.setText(_translate("MainWindow", "Cycloidal"))
        self.label_4.setText(_translate("MainWindow", "Unit: inch"))
        self.show_base.setText(_translate("MainWindow", "Base circle"))
        self.show_route.setText(_translate("MainWindow", "Cutter Route"))
        self.label_3.setText(_translate("MainWindow", "Base Circle:"))
        self.label_2.setText(_translate("MainWindow", "Lift:"))
        self.label.setText(_translate("MainWindow", "Cutter radius:"))
        self.label_5.setText(_translate("MainWindow", "Rotate Angle:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

