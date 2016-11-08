import thread
from os import read

class rqt_thread_manager():
	def show_std(self, label, fd):
		str_ = fd.read(1)
		while(str_):
			label.setText(str_)
			str_ += fd.read(1)
		print("jiojoiojio")

	def start(self, label, fd):
		thread.start_new_thread(self.show_std, (label, fd,))