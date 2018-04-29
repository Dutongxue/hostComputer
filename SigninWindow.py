from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QDesktopWidget
from PyQt5.QtCore import pyqtSignal, QObject

from ui.SignIn_ui import *

class LoginDialog(QDialog, Ui_LoginDiaog):

    login_sig = pyqtSignal(bool, str)

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.clicked)

    def clicked(self):
        self.close()

    def ok(self):
        self.show()

    def closeEvent(self, event):
        username = self.usernameEdit.text()
        pwd = self.pwdEdit.text()
        if username == pwd and username != '':
            self.login_sig.emit(True, username)
            self.usernameEdit.setText("")
            self.pwdEdit.setText("")
            self.hide()
        else:
            print("密码错误")
        event.ignore()
