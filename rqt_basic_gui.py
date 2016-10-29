import sys, os
from python_qt_binding.QtCore import pyqtSlot
from python_qt_binding.QtGui import *
from gui_roscore import Roscore
from rqt_rviz import RViz


# create our window
app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('rqt_basic')
rc = Roscore()
rviz = RViz()
 
# Create a button in the window
btn = QPushButton('Roscore', w)
btn.setStyleSheet('background-color: red; font-weight: bold')
# Create a button in the window
btn2 = QPushButton('Rviz', w)
btn2.move(0, 40)
# Create the actions
@pyqtSlot()
def on_clickRC():
	if rc.main():
		btn.setStyleSheet('background-color: green; font-weight: bold')
	else:
		btn.setStyleSheet('background-color: red; font-weight: bold')
 

@pyqtSlot()
def on_clickRVIZ():
	if rviz.main():
		btn2.setStyleSheet('background-color: green; font-weight: bold')
	else:
		btn2.setStyleSheet('background-color: red; font-weight: bold')
# connect the signals to the slots
btn.clicked.connect(on_clickRC)
btn2.clicked.connect(on_clickRVIZ)
 
# Show the window and run the app
w.show()
app.exec_()


