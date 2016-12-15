import sys
from multiprocessing import Process
import subprocess, signal, commands, os

class Graph():
	def __init__(self):
		self.g=None
		self.pids = []
		val = commands.getoutput('ps aux | grep "rqt_graph"').split("\n")
		for p in val:
			self.pids.append(int(p.split()[1]))
		if len(val) > 2:
			self.id_core= True
		else:
			self.id_core= False

	def start(self):
		if not self.id_core:
			self.g = subprocess.Popen(['rqt_graph'])
			self.id_core = True

	def status(self):
		if self.id_core:
			return True
		else:
			return False

	def stop(self):
		self.pids = []
		val = commands.getoutput('ps aux | grep "rqt_graph"').split("\n")
		for p in val:
			self.pids.append(int(p.split()[1]))
		for p in self.pids:
			if p != os.getpid():
				try:
					os.kill(p, signal.SIGKILL)
				except:
					pass
		self.id_core = False
		#self.g.kill()
		#self.g = None

	def main(self):
		if self.id_core:
			self.stop()
			return False
		else:
			self.start()
			return True