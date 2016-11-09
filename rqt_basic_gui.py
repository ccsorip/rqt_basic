import sys, rospy, os
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
w.resize(1000, 700)
w.setWindowTitle('rqt_basic')
rc = Roscore()
rviz = RViz()
ll = LoggerLevel()
gr = Graph()
tm = rqt_thread_manager()


#-------table env vars-------------
table_env_vars 	= QTableWidget()
table_env_vars.resize(300, 200)
table_env_vars.setColumnCount(2)
table_env_vars.setHorizontalHeaderLabels(["ENV NAME", "VALUE"])
#-scroller
scroller_env_vars = QScrollArea(w)
scroller_env_vars.resize(300, 200)
scroller_env_vars.move(670, 25)
scroller_env_vars.setWidget(table_env_vars)
tm.start_env_vars(table_env_vars)

#-------table params-------------
table_params 	= QTableWidget()
table_params.resize(300, 200)
table_params.setColumnCount(2)
table_params.setHorizontalHeaderLabels(["PARAM NAME", "VALUE"])
#-scroller
scroller_params = QScrollArea(w)
scroller_params.resize(300, 200)
scroller_params.move(670, 250)
scroller_params.setWidget(table_params)
tm.start_params(table_params)

#-------table active topics-------------
table_act_tops 	= QTableWidget()
table_act_tops.resize(300, 200)
table_act_tops.setColumnCount(1)
table_act_tops.setHorizontalHeaderLabels(["TOPIC NAME"])
#-scroller
scroller_act_tops = QScrollArea(w)
scroller_act_tops.resize(300, 200)
scroller_act_tops.move(670, 475)
scroller_act_tops.setWidget(table_act_tops)
tm.start_topics(table_act_tops)

#-------search parameter-------------
labelParam = QLabel('Parameter', w)
labelParam.move(5, 50)
textboxParam = QLineEdit(w)
textboxParam.move(95, 50)
btnSearchParam = QPushButton('Search', w)
btnSearchParam.setStyleSheet('background-color: white; font-weight: bold')
btnSearchParam.move(235, 50)

#-------search env variable-------------
labelEnv = QLabel('Env. variable', w)
labelEnv.move(5, 95)
textboxEnv = QLineEdit(w)
textboxEnv.move(95, 95)
btnSearchEnv = QPushButton('Search', w)
btnSearchEnv.setStyleSheet('background-color: white; font-weight: bold')
btnSearchEnv.move(235, 95)

#-------Standard output--------------
std_out = QLabel("")
std_out.resize(620,80)
std_out.setStyleSheet('font-weight: bold')
#-scroller
scroller = QScrollArea(w)
scroller.resize(630,90)
scroller.move(5, 160)
scroller.setStyleSheet('background-color: grey')
scroller.setWidget(std_out)

#-------Standard error--------------
std_err = QLabel("")
std_err.resize(620,80)
std_err.setStyleSheet('background-color: grey; color: red; font-weight: bold')
#-scroller
scroller2 = QScrollArea(w)
scroller2.resize(630,90)
scroller2.move(5, 300)
scroller2.setStyleSheet('background-color: grey')
scroller2.setWidget(std_err)
 
# Create a button in the window
btn = QPushButton('Roscore', w)
btn.setStyleSheet('background-color: red; font-weight: bold')
btn.move(5, 5)

btn2 = QPushButton('Rviz', w)
btn2.setStyleSheet('background-color: red; font-weight: bold')
btn2.move(95, 5)

btn3 = QPushButton('Logger Level', w)
btn3.setStyleSheet('background-color: red; font-weight: bold')
btn3.move(185, 5)

btn4 = QPushButton('Rqt_graph', w)
btn4.setStyleSheet('background-color: red; font-weight: bold')
btn4.move(305, 5)

# Create the actions
@pyqtSlot()
def on_clickRC():
	if rc.main():
		#tm.start(std_out, rc.stdout)
		#tm.start(std_err, rc.stderr)
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

@pyqtSlot()
def on_clickSearchParam():
	try:
		std_out.setText(std_out.text() + str(rospy.get_param(textboxParam.text()))  + "\n")
		std_out.adjustSize()
	except:
		std_err.setText(std_err.text() + "Parameter not found"  + "\n")
		std_err.adjustSize()

@pyqtSlot()
def on_clickSearchEnv():
	try:
		std_out.setText(std_out.text() + str(os.environ[textboxEnv.text()])  + "\n")
		for nom in os.environ:
			if nom.startswith("ROS"):
				print(nom + ':\t' + os.environ[nom])
		std_out.adjustSize()
	except:
		std_err.setText(std_err.text() + "Varabiable not found"  + "\n")
		std_err.adjustSize()

# connect the signals to the slots
btn.clicked.connect(on_clickRC)
btn2.clicked.connect(on_clickRVIZ)
btn3.clicked.connect(on_clickLL)
btn4.clicked.connect(on_clickG) 
btnSearchParam.clicked.connect(on_clickSearchParam) 
btnSearchEnv.clicked.connect(on_clickSearchEnv) 

# Show the window and run the app
w.setMinimumSize(910, 610)
w.show()
app.exec_()


