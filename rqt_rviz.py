import sys
from multiprocessing import Process
import subprocess

class RViz():
	def __init__(self):
		self.rviz=None

	def start(self):
		self.rviz = subprocess.Popen(['rviz'])

	def stop(self):
		self.rviz.kill()
		self.rviz = None

	def main(self):
		if self.rviz:
			self.stop()
			return False
		else:
			self.start()
			return True