from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
import os, time, serial

class comm(QThread):

    type = True
    book_sig = pyqtSignal(list)

    def __init__(self, db, cursor):
        super(comm, self).__init__()
        self.db = db
        self.cursor = cursor

    def dbcmd(self, cmd):
        try:
            self.cursor.execute(cmd)
            self.db.commit()
            return self.cursor.fetchall()
        except:
            self.db.rollback()
            print("db Select error")

    def settype(self, type):
        self.type = type

    def run(self):
        # card = [b'\x97\x77\xc0\xeb', b'\xe9\x18\x5e\x7b', b'\x75\xb3\x56\x25']

        # os.system("rfid/test &")
        # time.sleep(1)
        stohRfd = open("/media/enheng/办公/A_创新创业项目/分拣/fifo/stoh", 'rb')
        port = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

        while True:
            rec = stohRfd.read(4)
            if rec == b'':
                print("写端关闭")
                break
            else:
                sql = "select Name, class from book where Rfid = '{0}'".format(''.join([str(hex(i)[2:]) for i in list(rec)]))
                ret = self.dbcmd(sql)
                self.book_sig.emit([ret[0][0], ret[0][1]])
                if not self.type:
                    port.write(bytes((ret[0][1], )))
                # else:
                #     port.write(bytes((2,)))

        stohRfd.close()
        port.close()