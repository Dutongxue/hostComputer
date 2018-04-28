# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/SignIn.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoginDiaog(object):
    def setupUi(self, LoginDiaog):
        LoginDiaog.setObjectName("LoginDiaog")
        LoginDiaog.resize(259, 137)
        self.usernameEdit = QtWidgets.QLineEdit(LoginDiaog)
        self.usernameEdit.setGeometry(QtCore.QRect(50, 20, 161, 30))
        self.usernameEdit.setObjectName("usernameEdit")
        self.pwdEdit = QtWidgets.QLineEdit(LoginDiaog)
        self.pwdEdit.setGeometry(QtCore.QRect(50, 49, 161, 30))
        self.pwdEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwdEdit.setObjectName("pwdEdit")
        self.LoginButton = QtWidgets.QPushButton(LoginDiaog)
        self.LoginButton.setGeometry(QtCore.QRect(50, 90, 161, 30))
        self.LoginButton.setObjectName("LoginButton")

        self.retranslateUi(LoginDiaog)
        QtCore.QMetaObject.connectSlotsByName(LoginDiaog)

    def retranslateUi(self, LoginDiaog):
        _translate = QtCore.QCoreApplication.translate
        LoginDiaog.setWindowTitle(_translate("LoginDiaog", "登录"))
        self.LoginButton.setText(_translate("LoginDiaog", "Login"))



