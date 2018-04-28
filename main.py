
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QDesktopWidget

from MainWindow import *
from SigninWindow import *

def RunMain():
    app = QApplication(sys.argv)

    signin = LoginDialog()
    signin.show()

    mainWin = MyMainWindow()
    signin.login_sig.connect(mainWin.ok)

    # mainWin.show()

    sys.exit(app.exec_())

if __name__ == "__main__":

    RunMain()