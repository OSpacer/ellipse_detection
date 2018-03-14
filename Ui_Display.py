# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Display.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Display(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(888, 620)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 0, 1, 1, 1)
        self.label_40 = QtWidgets.QLabel(Form)
        self.label_40.setObjectName("label_40")
        self.gridLayout.addWidget(self.label_40, 3, 1, 1, 1)
        self.label_30 = QtWidgets.QLabel(Form)
        self.label_30.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 3, 0, 1, 1)
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 6, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(Form)
        self.label_1.setMinimumSize(QtCore.QSize(300, 200))
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setMinimumSize(QtCore.QSize(300, 200))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 6, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setMinimumSize(QtCore.QSize(300, 200))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(300, 200))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        self.horizontalSlider_1 = QtWidgets.QSlider(Form)
        self.horizontalSlider_1.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_1.setObjectName("horizontalSlider_1")
        self.gridLayout.addWidget(self.horizontalSlider_1, 2, 0, 1, 1)
        self.horizontalSlider_2 = QtWidgets.QSlider(Form)
        self.horizontalSlider_2.setMaximum(20)
        self.horizontalSlider_2.setMinimum(1)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.gridLayout.addWidget(self.horizontalSlider_2, 2, 1, 1, 1)
        self.horizontalSlider_3 = QtWidgets.QSlider(Form)
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName("horizontalSlider_3")
        self.gridLayout.addWidget(self.horizontalSlider_3, 5, 0, 1, 1)
        self.horizontalSlider_4 = QtWidgets.QSlider(Form)
        self.horizontalSlider_4.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_4.setObjectName("horizontalSlider_4")
        self.gridLayout.addWidget(self.horizontalSlider_4, 5, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_10.setText(_translate("Form", "Original Image"))
        self.label_20.setText(_translate("Form", "Blurred Image"))
        self.label_30.setText(_translate("Form", "Edged "))
        self.label_40.setText(_translate("Form", "TextLabel"))
        self.pushButton_1.setText(_translate("Form", "PushButton"))
        self.label_1.setText(_translate("Form", "TextLabel"))
        self.label_3.setText(_translate("Form", "TextLabel"))
        self.pushButton_2.setText(_translate("Form", "Save"))
        self.label_4.setText(_translate("Form", "TextLabel"))
        self.label_2.setText(_translate("Form", "TextLabel"))
