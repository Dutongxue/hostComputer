from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QDesktopWidget
from ui.Main_ui import *

class MyMainWindow(QMainWindow, Ui_Main):

    type = False

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

    def ok(self, val):
        if val:
            self.type = True

        self.show()
