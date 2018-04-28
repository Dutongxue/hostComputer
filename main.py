
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QDesktopWidget
from PyQt5.QtCore import pyqtSignal, QObject
from ui.Main_ui import *
from ui.SignIn_ui import *

class MyMainWindow(QMainWindow, Ui_Main):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def ok(self):
        self.show()

class LoginDialog(QDialog, Ui_LoginDiaog):

    login_sig = pyqtSignal()

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.clicked)

    def clicked(self):
        if self.usernameEdit.text() == self.pwdEdit.text():
            self.close()
        else:
            print("密码错误")

    def closeEvent(self, QCloseEvent):
        self.login_sig.emit()


def RunMain():
    app = QApplication(sys.argv)

    signin = LoginDialog()
    signin.show()

    mainWin = MyMainWindow()
    signin.login_sig.connect(mainWin.ok)



    # myWin.show()


    sys.exit(app.exec_())

if __name__ == "__main__":

    RunMain()