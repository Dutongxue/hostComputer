import select
import os, time
# print(os.system('/media/enheng/办公/A_创新创业项目/分拣/fifo/cmake-build-debug/fifo &'))

time.sleep(1)
stohRfd = open("/media/enheng/办公/A_创新创业项目/分拣/fifo/stoh", 'rb')

while True:
    msg = stohRfd.read(4)
    if msg == b'':
        print("写端关闭")
        break
    print(msg)

stohRfd.close()