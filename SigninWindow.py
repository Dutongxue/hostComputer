from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QDesktopWidget
from PyQt5.QtCore import pyqtSignal, QObject

from ui.SignIn_ui import *

class LoginDialog(QDialog, Ui_LoginDiaog):

    login_sig = pyqtSignal(bool)

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.clicked)

    def clicked(self):
        self.close()

    def closeEvent(self, event):
        if self.usernameEdit.text() == self.pwdEdit.text() and self.usernameEdit.text() != '':
            self.login_sig.emit(True)
            # self.hide()
            event.accept()
        else:
            print("密码错误")
            event.ignore()