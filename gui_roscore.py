import sys
from multiprocessing import Process
import subprocess, os, commands, signal

class Roscore():
	def __init__(self):
		self.rc=None
		self.stdout=None
		self.stderr=None
		self.pids = []
		val = commands.getoutput('ps aux | egrep -w "rosmaster|roscore"').split("\n")
		for p in val:
			self.pids.append(int(p.split()[1]))
			#if pid != os.getpid():
			#	os.kill(pid, signal.SIGKILL)
			
		if len(val) > 2:
			self.id_core= True
		else:
			self.id_core= False


	def start(self):
		if not self.id_core:
			self.rc = subprocess.Popen(['roscore'])
			self.id_core = True
		#for c in iter(lambda: self.rc.stdout.read(1), ''):
		#	print(c)
		#self.stdout = self.rc.stdout
		#self.stderr = self.rc.stderr

	def status(self):
		if self.id_core:
			return True
		else:
			return False

	def stop(self):
		self.pids = []
		val = commands.getoutput('ps aux | egrep -w "rosmaster|roscore"').split("\n")
		for p in val:
			self.pids.append(int(p.split()[1]))
		for p in self.pids:
			if p != os.getpid():
				try:
					os.kill(p, signal.SIGKILL)
				except:
					pass
#		else:
#			self.rc.terminate()
#			self.rc = None
#			self.stdout = None
#			self.stderr = None
		self.id_core = False

	def main(self):
		if self.id_core:
			self.stop()
			return False
		else:
			self.start()
			return True