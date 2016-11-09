import thread, os, time, rospy
import subprocess
from os import read
from python_qt_binding.QtGui import *

class rqt_thread_manager():
	def show_std(self, label, fd):
		str_ = fd.read(1)
		while(str_):
			label.setText(str_)
			str_ += fd.read(1)
		print("jiojoiojio")

	def start(self, label, fd):
		thread.start_new_thread(self.show_std, (label, fd,))

	def show_env_vars(self, table):
		while True:
			env_vars = []
			for nom in os.environ:
				if nom.startswith("ROS"):
					env_vars.append([nom, os.environ[nom]])
			table.setRowCount(len(env_vars))
			i=0
			for env_var in env_vars:
				table.setItem(i,0, QTableWidgetItem(env_var[0]))
				table.setItem(i,1, QTableWidgetItem(env_var[1]))
				i+=1
			time.sleep(1)

	def start_env_vars(self, table):
		thread.start_new_thread(self.show_env_vars, (table,))

	def show_params(self, table):
		while True:
			try:
				params = rospy.get_param("/")
				table.setRowCount(len(params))
				i=0
				for param in params:
					table.setItem(i,0, QTableWidgetItem(param))
					table.setItem(i,1, QTableWidgetItem(str(params[param])))
					i+=1
			except:
				pass
			time.sleep(1)

	def start_params(self, table):
		thread.start_new_thread(self.show_params, (table,))

	def show_topics(self, table):
		while True:
			proc = subprocess.Popen(['rostopic', 'list'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
			str_ = proc.stdout.read()
			arr = str_.split("\n")
			table.setRowCount(len(arr) - 1)
			i=0
			for a in arr:
				table.setItem(i,0, QTableWidgetItem(a))
				i+=1
			pass
		time.sleep(1)

	def start_topics(self, table):
		thread.start_new_thread(self.show_topics, (table,))