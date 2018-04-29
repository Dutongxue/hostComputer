from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QDesktopWidget
from PyQt5.QtCore import pyqtSignal, QObject

from ui.SignIn_ui import *

class LoginDialog(QDialog, Ui_LoginDiaog):

    login_sig = pyqtSignal(bool, str)
    type = True

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.LoginButton.clicked.connect(lambda: self.clicked(True))
        self.LoginButton_2.clicked.connect(lambda: self.clicked(False))

    def clicked(self, type):
        self.type = type
        self.close()

    def ok(self):
        self.show()

    def closeEvent(self, event):
        username = self.usernameEdit.text()
        pwd = self.pwdEdit.text()
        if username == pwd and username != '':
            self.login_sig.emit(self.type, username)
            self.usernameEdit.setText("")
            self.pwdEdit.setText("")
            self.hide()
        else:
            print("密码错误")
        event.ignore()
