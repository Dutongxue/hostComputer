import os

for filename in os.listdir('./'):
    if filename.endswith('.ui'):
        os.system('python3 -m PyQt5.uic.pyuic {0}.ui -o {0}_ui.py'.format(filename[:-3]))
