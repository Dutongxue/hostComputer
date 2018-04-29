
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QDesktopWidget

from MainWindow import *
from SigninWindow import *


def runMain():
    app = QApplication(sys.argv)

    signin = LoginDialog()
    signin.show()

    mainWin = MyMainWindow()
    mainWin.retbtn.clicked.connect(signin.ok)
    signin.login_sig.connect(mainWin.ok)

    # mainWin.show()

    sys.exit(app.exec_())


if __name__ == "__main__":

    runMain()