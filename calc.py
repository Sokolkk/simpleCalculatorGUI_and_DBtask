# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(382, 393)
        Form.setStyleSheet("QPushButton{\n"
"width: 40px;\n"
"height: 30px;    \n"
"}\n"
"QPushButton:hover{\n"
"background-color: silver;\n"
"}")
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Maiandra GD")
        font.setPointSize(19)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_2.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_1 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_1.setFont(font)
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_mult.setFont(font)
        self.btn_mult.setObjectName("btn_mult")
        self.gridLayout.addWidget(self.btn_mult, 0, 2, 1, 1)
        self.btn_div = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 0, 1, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_8.setFont(font)
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)
        self.btn_4 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_4.setFont(font)
        self.btn_4.setObjectName("btn_4")
        self.gridLayout.addWidget(self.btn_4, 2, 0, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_2.setFont(font)
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_5.setFont(font)
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_3.setFont(font)
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_6.setFont(font)
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_9.setFont(font)
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_7.setFont(font)
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_equal = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_equal.setFont(font)
        self.btn_equal.setObjectName("btn_equal")
        self.gridLayout.addWidget(self.btn_equal, 4, 3, 1, 1)
        self.btn_erase = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_erase.setFont(font)
        self.btn_erase.setObjectName("btn_erase")
        self.gridLayout.addWidget(self.btn_erase, 0, 0, 1, 1)
        self.btn_add = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_add.setFont(font)
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 2, 3, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_0.setFont(font)
        self.btn_0.setStyleSheet("")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 1)
        self.btn_sub = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_sub.setFont(font)
        self.btn_sub.setObjectName("btn_sub")
        self.gridLayout.addWidget(self.btn_sub, 1, 3, 1, 1)
        self.btn_reserved = QtWidgets.QPushButton(Form)
        self.btn_reserved.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_reserved.setFont(font)
        self.btn_reserved.setText("")
        self.btn_reserved.setObjectName("btn_reserved")
        self.gridLayout.addWidget(self.btn_reserved, 4, 2, 1, 1)
        self.btn_back = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        self.gridLayout.addWidget(self.btn_back, 0, 3, 1, 1)
        self.btn_reserved_2 = QtWidgets.QPushButton(Form)
        self.btn_reserved_2.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_reserved_2.setFont(font)
        self.btn_reserved_2.setText("")
        self.btn_reserved_2.setObjectName("btn_reserved_2")
        self.gridLayout.addWidget(self.btn_reserved_2, 4, 1, 1, 1)
        self.btn_reserved_3 = QtWidgets.QPushButton(Form)
        self.btn_reserved_3.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_reserved_3.setFont(font)
        self.btn_reserved_3.setText("")
        self.btn_reserved_3.setObjectName("btn_reserved_3")
        self.gridLayout.addWidget(self.btn_reserved_3, 3, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_1.setText(_translate("Form", "1"))
        self.btn_1.setShortcut(_translate("Form", "1"))
        self.btn_mult.setText(_translate("Form", "X"))
        self.btn_mult.setShortcut(_translate("Form", "*"))
        self.btn_div.setText(_translate("Form", "÷"))
        self.btn_div.setShortcut(_translate("Form", "/"))
        self.btn_8.setText(_translate("Form", "8"))
        self.btn_8.setShortcut(_translate("Form", "8"))
        self.btn_4.setText(_translate("Form", "4"))
        self.btn_4.setShortcut(_translate("Form", "4"))
        self.btn_2.setText(_translate("Form", "2"))
        self.btn_2.setShortcut(_translate("Form", "2"))
        self.btn_5.setText(_translate("Form", "5"))
        self.btn_5.setShortcut(_translate("Form", "5"))
        self.btn_3.setText(_translate("Form", "3"))
        self.btn_3.setShortcut(_translate("Form", "3"))
        self.btn_6.setText(_translate("Form", "6"))
        self.btn_6.setShortcut(_translate("Form", "6"))
        self.btn_9.setText(_translate("Form", "9"))
        self.btn_9.setShortcut(_translate("Form", "9"))
        self.btn_7.setText(_translate("Form", "7"))
        self.btn_7.setShortcut(_translate("Form", "7"))
        self.btn_equal.setText(_translate("Form", "="))
        self.btn_equal.setShortcut(_translate("Form", "Return"))
        self.btn_erase.setText(_translate("Form", "C"))
        self.btn_erase.setShortcut(_translate("Form", "Ctrl+Z"))
        self.btn_add.setText(_translate("Form", "+"))
        self.btn_add.setShortcut(_translate("Form", "+"))
        self.btn_0.setText(_translate("Form", "0"))
        self.btn_0.setShortcut(_translate("Form", "0"))
        self.btn_sub.setText(_translate("Form", "-"))
        self.btn_sub.setShortcut(_translate("Form", "-"))
        self.btn_back.setText(_translate("Form", "←"))
        self.btn_back.setShortcut(_translate("Form", "Backspace"))

