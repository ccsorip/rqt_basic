import sys
from multiprocessing import Process
import subprocess

class LoggerLevel():
	def __init__(self):
		self.ll=None

	def start(self):
		self.ll = subprocess.Popen(['rqt_logger_level'])

	def stop(self):
		self.ll.kill()
		self.ll = None

	def main(self):
		if self.ll:
			self.stop()
			return False
		else:
			self.start()
			return True