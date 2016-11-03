import thread

class rqt_thread_manager():
	def show_std(self, label, fdopen):
		str_ = fdopen.read()
		label.setText(str_)
		print("jiojoiojio")
		return "joijiooijoij"

	def start(self, label, fdopen):
		thread.start_new_thread(self.show_std, (label, fdopen,))