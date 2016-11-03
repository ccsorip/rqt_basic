import sys
from multiprocessing import Process
import subprocess

class Roscore():
	def __init__(self):
		self.rc=None
		self.stdout=None
		self.stderr=None

	def start(self):
		self.rc = subprocess.Popen(['roscore'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		self.stdout = self.rc.stdout
		self.stderr = self.rc.stderr

	def stop(self):
		self.rc.terminate()
		self.rc = None
		self.stdout = None
		self.stderr = None

	def main(self):
		if self.rc:
			self.stop()
			return False
		else:
			self.start()
			return True