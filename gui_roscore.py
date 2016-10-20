import roslaunch
import sys
from multiprocessing import Process

class Roscore():
	def __init__(self):
		self.rc=None

	def launch(self):
		roslaunch.main(['roscore', '--core'] + sys.argv[1:])

	def start(self):
		self.rc = Process(target=self.launch, args=())
		self.rc.start()

	def stop(self):
		self.rc.terminate()
		self.rc = None

	def main(self):
		if self.rc:
			self.stop()
			return False
		else:
			self.start()
			return True