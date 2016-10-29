import sys
from multiprocessing import Process
from subprocess import call

class RViz():
	def __init__(self):
		self.rviz=None

	def launch(self):
		call('rviz')
		print "----------------ASDASDASDSADSAD---------------------------------"

	def start(self):
		self.rviz = Process(target=self.launch, args=())
		self.rviz.start()

	def stop(self):
		self.rviz.terminate()
		self.rviz = None

	def main(self):
		if self.rviz:
			self.stop()
			return False
		else:
			self.start()
			return True