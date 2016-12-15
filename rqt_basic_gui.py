import sys, rospy, os, subprocess
from python_qt_binding.QtCore import *
from python_qt_binding.QtGui import *
from gui_roscore import Roscore
from rqt_rviz import RViz
from rqt_loggerlevel import LoggerLevel
from rqt_basic_graph import Graph
from rqt_thread_manager import rqt_thread_manager


# create our window
app = QApplication(sys.argv)
w = QWidget()
w.resize(930, 730)
w.setWindowTitle('rqt_basic')
rc = Roscore()
rviz = RViz()
ll = LoggerLevel()
gr = Graph()
tm = rqt_thread_manager()

#------ Tabs in std out --------
#------console-----------------
console_container = QWidget(w)
console_container.move(5, 387)
console_container.resize(486, 318)
console_process = QProcess()
console_box = QVBoxLayout()
console_box.setMargin(0)
console_box.addWidget(console_container)
console_process.start(
        'xterm',['-into', str(console_container.winId())])

#-------table env vars-------------
table_env_vars 	= QTableWidget()
table_env_vars.resize(390, 200)
table_env_vars.setColumnCount(2)
table_env_vars.setColumnWidth(1, 250)
table_env_vars.setHorizontalHeaderLabels(["ENV NAME", "VALUE"])
#-scroller
scroller_env_vars = QScrollArea(w)
scroller_env_vars.move(515, 45)
scroller_env_vars.setWidget(table_env_vars)
tm.start_env_vars(table_env_vars)

#-------table params-------------
table_params 	= QTableWidget()
table_params.resize(390, 200)
table_params.setColumnCount(2)
table_params.setColumnWidth(1, 250)
table_params.setHorizontalHeaderLabels(["PARAM NAME", "VALUE"])
#-scroller
scroller_params = QScrollArea(w)
scroller_params.move(515, 295)
scroller_params.setWidget(table_params)
tm.start_params(table_params)

#-------table active topics-------------
table_act_tops 	= QTableWidget()
table_act_tops.resize(390, 200)
table_act_tops.setColumnCount(2)
table_act_tops.setColumnWidth(1, 250)
table_act_tops.setHorizontalHeaderLabels(["TOPIC NAME", "TOPIC TYPE"])
#-scroller
scroller_act_tops = QScrollArea(w)
scroller_act_tops.move(515, 505)
scroller_act_tops.setWidget(table_act_tops)
tm.start_topics(table_act_tops)

#-------search env variable-------------
labelEnv = QLabel('Env. variable', w)
labelEnv.move(515, 10)
textboxEnv = QLineEdit(w)
textboxEnv.move(605, 10)
btnSearchEnv = QPushButton('Search', w)
btnSearchEnv.setStyleSheet('background-color: white; font-weight: bold')
btnSearchEnv.move(745, 10)

#-------search parameter-------------
labelParam = QLabel('Parameter', w)
labelParam.move(515, 260)
textboxParam = QLineEdit(w)
textboxParam.move(605, 260)
btnSearchParam = QPushButton('Search', w)
btnSearchParam.setStyleSheet('background-color: white; font-weight: bold')
btnSearchParam.move(745, 260)

#-------Standard output--------------
std_out = QLabel("")
std_out.setTextFormat(1)
std_out.resize(476,300)
#std_out.setStyleSheet('font-weight: bold')
#-scroller
scroller = QScrollArea(w)
scroller.resize(486,310)
scroller.move(5, 45)
scroller.setStyleSheet('background-color: black')
scroller.setWidget(std_out)

#-------Standard error--------------
std_err = QLabel("")

#std_err.resize(620,80)
#std_err.setStyleSheet('background-color: grey; color: red; font-weight: bold')
#-scroller
#scroller2 = QScrollArea(w)
#scroller2.resize(630,90)
#scroller2.move(5, 300)
#scroller2.setStyleSheet('background-color: grey')
#scroller2.setWidget(std_err)
 
# Create a button in the window
btn = QPushButton('Roscore', w)
btn.resize(100,30)
if rc.status():
	btn.setStyleSheet('background-color: rgb(60,179,113); font: italic; font-weight: bold')
else:
	btn.setStyleSheet('background-color: rgb(255,99,71); font: italic; font-weight: bold')
btn.move(5, 5)

btn2 = QPushButton('Rviz', w)
btn2.resize(100,30)
if rviz.status():
	btn2.setStyleSheet('background-color: rgb(60,179,113); font: italic; font-weight: bold')
else:
	btn2.setStyleSheet('background-color: rgb(255,99,71); font: italic; font-weight: bold')
btn2.move(133, 5)

btn3 = QPushButton('Logger Level', w)
btn3.resize(100,30)
if ll.status():
	btn3.setStyleSheet('background-color: rgb(60,179,113); font: italic; font-weight: bold')
else:
	btn3.setStyleSheet('background-color: rgb(255,99,71); font: italic; font-weight: bold')
btn3.move(261, 5)

btn4 = QPushButton('Rqt_graph', w)
btn4.resize(100,30)
if gr.status():
	btn4.setStyleSheet('background-color: rgb(60,179,113); font: italic; font-weight: bold')
else:
	btn4.setStyleSheet('background-color: rgb(255,99,71); font: italic; font-weight: bold')
btn4.move(389, 5)

# Create the actions
@pyqtSlot()
def on_clickRC():
	if rc.main():
		#tm.start(std_out, rc.stdout)
		#tm.start(std_err, rc.stderr)
		btn.setStyleSheet('background-color: rgb(60,179,113); font-weight: bold')
	else:
		btn.setStyleSheet('background-color: rgb(255,99,71); font-weight: bold')
 

@pyqtSlot()
def on_clickRVIZ():
	if rc.status():
		if rviz.main():
			btn2.setStyleSheet('background-color: rgb(60,179,113); font-weight: bold')
		else:
			btn2.setStyleSheet('background-color: rgb(255,99,71); font-weight: bold')
	else:
		result = QMessageBox.question(w, 'Message', "Can't initialize Rviz without Roscore launched")

@pyqtSlot()
def on_clickLL():
	if rc.status():
		if ll.main():
			btn3.setStyleSheet('background-color: rgb(60,179,113); font-weight: bold')
		else:
			btn3.setStyleSheet('background-color: rgb(255,99,71); font-weight: bold')
	else:
		result = QMessageBox.question(w, 'Message', "Can't initialize Logger Level without Roscore launched")

@pyqtSlot()
def on_clickG():
	if rc.status():
		if gr.main():
			btn4.setStyleSheet('background-color: rgb(60,179,113); font-weight: bold')
		else:
			btn4.setStyleSheet('background-color: rgb(255,99,71); font-weight: bold')
	else:
		result = QMessageBox.question(w, 'Message', "Can't initialize Rqt_Graph without Roscore launched")


@pyqtSlot()
def on_clickSearchEnv():
	try:
		rich_text = "<span style=\"color:white;font-weight:bold;\">"+str(os.environ[textboxEnv.text()])+"</span><br>"
		std_out.setText(std_out.text().replace('font-weight:bold;', '') + rich_text)
		std_out.adjustSize()
	except:
		rich_text = "<span style=\"color:red;font-weight:bold;\">Variable not found</span><br>"
		std_out.setText(std_out.text().replace('font-weight:bold;', '') + rich_text)
		std_out.adjustSize()

@pyqtSlot()
def on_clickSearchParam():
	try:
		rich_text = "<span style=\"color:white;font-weight:bold;\">"+str(rospy.get_param(textboxParam.text()))+"</span><br>"
		std_out.setText(std_out.text().replace('font-weight:bold;', '') + rich_text)
		std_out.adjustSize()
	except:
		rich_text = "<span style=\"color:red;font-weight:bold;\">Parameter not found</span><br>"
		std_out.setText(std_out.text().replace('font-weight:bold;', '') + rich_text)
		std_out.adjustSize()

def cellClick(row,col):
	if col == 1:
		str_ = table_act_tops.item(row, col).text()
		proc = subprocess.Popen(['rosmsg', 'show', str_[:-1]], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		rich_text = "<span style=\"color:white;font-weight:bold;\">"+proc.stdout.read()+"</span><br>"
		std_out.setText(std_out.text().replace('font-weight:bold;', '') + rich_text)
		std_out.adjustSize()

# connect the signals to the slots
btn.clicked.connect(on_clickRC)
btn2.clicked.connect(on_clickRVIZ)
btn3.clicked.connect(on_clickLL)
btn4.clicked.connect(on_clickG) 
btnSearchParam.clicked.connect(on_clickSearchParam) 
btnSearchEnv.clicked.connect(on_clickSearchEnv) 

table_act_tops.cellClicked.connect(cellClick)

# Show the window and run the app
w.setMinimumSize(930, 730)
w.show()
app.exec_()


