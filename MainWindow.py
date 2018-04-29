from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QDialog, QPushButton, QDesktopWidget,
                             QHBoxLayout, QVBoxLayout, QLineEdit, QLabel,
                             QTextBrowser, QGridLayout, QTableView, QTableWidget,
                             QTableWidgetItem)
from PyQt5.QtGui import QIcon, QStandardItemModel
from ui.Main_ui import *
import pymysql, time

class MyMainWindow(QWidget):

    type = False

    def __init__(self):
        super().__init__()
        self.row = 0
        self.col = 0

        self.initUI()

    def initUI(self):
        # self.setupUi(self)
        bgHbox = QHBoxLayout()
        bgrid = QGridLayout()
        bgrid.setSpacing(10)
        leftVbox = QVBoxLayout()

        idHbox = QHBoxLayout()
        idLabel = QLabel("学号：")
        self.idLabelval = QLabel("20151110048")
        idHbox.addWidget(idLabel)
        idHbox.addWidget(self.idLabelval)

        nameHbox = QHBoxLayout()
        nameLable = QLabel("姓名：")
        self.nameLableval = QLabel("三胖")
        nameHbox.addWidget(nameLable)
        nameHbox.addWidget(self.nameLableval)

        classHbox = QHBoxLayout()
        classLabel = QLabel("班级：")
        self.classLabelval = QLabel("物联网1502  ")
        classHbox.addWidget(classLabel)
        classHbox.addWidget(self.classLabelval)

        self.btn = QPushButton("退出")
        self.btn.clicked.connect(self.ret)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.VLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)

        rightVbox = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(10)
        self.table.setRowCount(100)
        self.table.setHorizontalHeaderLabels(['图书名', '图书ID', '归还时间', '', '', '', '', '', '', ''])
        for i in range(self.col):
            self.table.setColumnWidth(i, 200)

        rightVbox.addWidget(self.table)
        # self.printBrowser = QTextBrowser()
        # rightVbox.addWidget(self.printBrowser)

        leftVbox.addStretch(20)
        leftVbox.addLayout(idHbox)
        leftVbox.addStretch(1)
        leftVbox.addLayout(nameHbox)
        leftVbox.addStretch(1)
        leftVbox.addLayout(classHbox)
        leftVbox.addStretch(1)
        leftVbox.addWidget(self.btn)
        leftVbox.addStretch(20)

        bgHbox.addLayout(leftVbox)
        bgHbox.addWidget(line)
        bgHbox.addLayout(rightVbox)

        self.setLayout(bgHbox)
        self.setWindowTitle("图书信息")
        self.setGeometry(300, 300, 1000, 1000 * 0.618)
        self.setWindowIcon(QIcon('/home/enheng/Pictures/Icon/music.png'))
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def ok(self, val, id):
        if val:
            self.type = True

        self.idLabelval.setText(id)
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

    def addItem(self, v):
        j = 0
        for i in range(len(v)):
            item = QTableWidgetItem(v[i])
            self.table.setItem(self.row, j, item)
            j += 1
        item = QTableWidgetItem(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self.table.setItem(self.row, j, item)

    def ret(self):
        self.table.clearContents()
        self.hide()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        if hasattr(self, 'db'):
            self.db.close()