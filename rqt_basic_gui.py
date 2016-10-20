import sys, os
from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import *
from multiprocessing import Process
from gui_roscore import Roscore


# create our window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('rqt_basic')
rc = Roscore()
 
# Create a button in the window
btn = QPushButton('Roscore', w)
btn.setStyleSheet('background-color: red; font-weight: bold')
# Create a button in the window
btn2 = QPushButton('DSASADSAF', w)
btn2.move(0, 40)
 
# Create the actions
@pyqtSlot()
def on_click():
	if rc.main():
		btn.setStyleSheet('background-color: green; font-weight: bold')
	else:
		btn.setStyleSheet('background-color: red; font-weight: bold')
 
# connect the signals to the slots
btn.clicked.connect(on_click)

btn2.clicked.connect(on_click)
 
# Show the window and run the app
w.show()
app.exec_()


