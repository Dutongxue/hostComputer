from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QDialog, QPushButton, QDesktopWidget,
                             QHBoxLayout, QVBoxLayout, QLineEdit)
from PyQt5.QtGui import QIcon
from ui.Main_ui import *
import pymysql

class MyMainWindow(QWidget):

    type = False

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # self.setupUi(self)
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        self.btn = QPushButton("连接数据库")
        self.btn.clicked.connect(self.link)
        self.btn2 = QPushButton("查询数据")
        self.btn2.clicked.connect(self.select)

        self.ledit = QLineEdit()

        hbox.addStretch(1)
        hbox.addWidget(self.btn)
        hbox.addStretch(1)
        hbox.addWidget(self.btn2)
        hbox.addStretch(1)

        vbox.addWidget(self.ledit)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 500, 500 * 0.618)
        self.setWindowIcon(QIcon('/home/enheng/Pictures/Icon/music.png'))
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

    def link(self):
        try:
            self.db = pymysql.connect('localhost', 'enheng', '', 'book')
        except pymysql.err.Error:
            print("db Link error")
        else:
            self.cursor = self.db.cursor()

    def select(self):
        try:
            self.cursor.execute(self.ledit.text())
            res = self.cursor.fetchall()
            print(res)
        except:
            print("db Select error")


    def closeEvent(self, a0: QtGui.QCloseEvent):
        if hasattr(self, 'db'):
            self.db.close()