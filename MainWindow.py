from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow, QDialog, QPushButton, QDesktopWidget,
                             QHBoxLayout, QVBoxLayout, QLineEdit, QLabel,
                             QTextBrowser, QGridLayout, QTableView, QTableWidget,
                             QTableWidgetItem, QFrame)
from PyQt5.QtGui import QIcon, QStandardItemModel
from PyQt5.QtCore import pyqtSignal, QUrl
from PyQt5.QtMultimedia import QMediaPlayer
from ui.Main_ui import *
import pymysql, time
from comm import *

class MyMainWindow(QWidget):

    type = False
    type_sig = pyqtSignal(bool)

    def __init__(self):
        super().__init__()
        self.row = 0
        self.col = 10

        self.initUI()
        self.link()
        self.js = '/home/pi/pyqt/mp3/js.mp3'
        self.hs = '/home/pi/pyqt/mp3/hs.mp3'
        self.tx = '/home/pi/pyqt/mp3/tx.mp3'


    def initUI(self):
        # self.setupUi(self)

        self.player = QMediaPlayer()
        self.player.setVolume(100)

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

        self.retbtn = QPushButton("退出")
        self.retbtn.clicked.connect(self.ret)

        # self.insertbtn = QPushButton("插入")
        # self.insertbtn.clicked.connect(self.insertClick)

        line = QFrame()
        line.setFrameShape(QFrame.VLine)
        line.setFrameShadow(QFrame.Sunken)

        rightVbox = QVBoxLayout()
        self.table = QTableWidget()
        self.table.setColumnCount(self.col)
        self.table.setRowCount(100)
        self.table.setHorizontalHeaderLabels(['图书名', '图书ID', '归还时间', '', '', '', '', '', '', ''])
        for i in range(self.col):
            self.table.setColumnWidth(i, 150)

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
        leftVbox.addWidget(self.retbtn)
        # leftVbox.addWidget(self.insertbtn)
        leftVbox.addStretch(20)

        bgHbox.addLayout(leftVbox)
        bgHbox.addWidget(line)
        bgHbox.addLayout(rightVbox)

        self.setLayout(bgHbox)
        self.setWindowTitle("Main")
        self.setGeometry(300, 300, 1000, 1000 * 0.618)
        self.setWindowIcon(QIcon('/home/enheng/Pictures/Icon/music.png'))
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    # def insertClick(self, item):
    #     self.addItem(["这是书名", "这是ID"])

    # 载入Main窗口
    def ok(self, type, id):
        self.type = type
        self.type_sig.emit(type)
        if type:
            self.setWindowTitle("借阅信息")
        else:
            self.setWindowTitle("归还信息")
            self.player.setMedia(QUrl.fromLocalFile(self.tx))
            self.player.play()

        self.idLabelval.setText(id)
        ret = self.dbcmd("select Name, Class from stu where Id = '{0}'".format(id))
        # print(ret)
        if len(ret) != 0:
            self.nameLableval.setText(ret[0][0])
            self.classLabelval.setText(ret[0][1] + "  ")
        self.show()

    # 连接数据库
    def link(self):
        try:
            self.db = pymysql.connect('localhost', 'enheng', '123456', 'sorting', charset='utf8')
        except pymysql.err.Error:
            print("db Link error")
            self.close()
        else:
            self.cursor = self.db.cursor()
            self.c = comm(self.db, self.cursor)
            self.type_sig.connect(self.c.settype)
            self.c.book_sig.connect(self.addItem)
            self.c.start()

    # 数据库查询
    def dbcmd(self, cmd):
        try:
            self.cursor.execute(cmd)
            self.db.commit()
            return self.cursor.fetchall()
        except:
            self.db.rollback()
            print("db Select error")

    # 添加数据项
    def addItem(self, v):
        j = 0
        for i in range(len(v)):
            item = QTableWidgetItem(v[i])
            self.table.setItem(self.row, j, item)
            j += 1
        item = QTableWidgetItem(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
        self.table.setItem(self.row, j, item)
        self.row += 1

        if self.type:
            self.player.setMedia(QUrl.fromLocalFile(self.js))
        else:
            self.player.setMedia(QUrl.fromLocalFile(self.hs))
        self.player.play()

    # 退出时
    def ret(self):
        self.table.clearContents()
        self.row = 0
        self.hide()

    def closeEvent(self, a0: QtGui.QCloseEvent):
        if hasattr(self, 'db'):
            self.c.quit()
            self.cursor.close()
            self.db.close()
