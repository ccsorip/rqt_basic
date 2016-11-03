import sys
from multiprocessing import Process
import subprocess

class Graph():
	def __init__(self):
		self.g=None

	def start(self):
		self.g = subprocess.Popen(['rqt_graph'])

	def stop(self):
		self.g.kill()
		self.g = None

	def main(self):
		if self.g:
			self.stop()
			return False
		else:
			self.start()
			return True