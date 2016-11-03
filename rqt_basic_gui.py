import sys, os
from python_qt_binding.QtCore import pyqtSlot
from python_qt_binding.QtGui import *
from gui_roscore import Roscore
from rqt_rviz import RViz
from rqt_loggerlevel import LoggerLevel
from rqt_basic_graph import Graph
from rqt_thread_manager import rqt_thread_manager


# create our window
app = QApplication(sys.argv)
w = QWidget()
w.resize(640, 480)
w.setWindowTitle('rqt_basic')
rc = Roscore()
rviz = RViz()
ll = LoggerLevel()
gr = Graph()
tm = rqt_thread_manager()


std_out = QLabel(w)
std_out.resize(630,90)
std_out.move(5, 160)
std_out.setStyleSheet('background-color: grey; font-weight: bold')

std_err = QLabel(w)
std_err.resize(630,90)
std_err.move(5, 300)
std_err.setStyleSheet('background-color: grey; color: red; font-weight: bold')

 
# Create a button in the window
btn = QPushButton('Roscore', w)
btn.setStyleSheet('background-color: red; font-weight: bold')
btn.move(5, 0)

btn2 = QPushButton('Rviz', w)
btn2.setStyleSheet('background-color: red; font-weight: bold')
btn2.move(5, 40)

btn3 = QPushButton('Logger Level', w)
btn3.setStyleSheet('background-color: red; font-weight: bold')
btn3.move(5, 80)

btn4 = QPushButton('Rqt_graph', w)
btn4.setStyleSheet('background-color: red; font-weight: bold')
btn4.move(5, 120)

# Create the actions
@pyqtSlot()
def on_clickRC():
	if rc.main():
		tm.start(std_out, rc.stdout)
		tm.start(std_err, rc.stderr)
		btn.setStyleSheet('background-color: green; font-weight: bold')
	else:
		btn.setStyleSheet('background-color: red; font-weight: bold')
 

@pyqtSlot()
def on_clickRVIZ():
	if rviz.main():
		btn2.setStyleSheet('background-color: green; font-weight: bold')
	else:
		btn2.setStyleSheet('background-color: red; font-weight: bold')

@pyqtSlot()
def on_clickLL():
	if ll.main():
		btn3.setStyleSheet('background-color: green; font-weight: bold')
	else:
		btn3.setStyleSheet('background-color: red; font-weight: bold')

@pyqtSlot()
def on_clickG():
	if gr.main():
		btn4.setStyleSheet('background-color: green; font-weight: bold')
	else:
		btn4.setStyleSheet('background-color: red; font-weight: bold')


# connect the signals to the slots
btn.clicked.connect(on_clickRC)
btn2.clicked.connect(on_clickRVIZ)
btn3.clicked.connect(on_clickLL)
btn4.clicked.connect(on_clickG) 

# Show the window and run the app
w.show()
app.exec_()


