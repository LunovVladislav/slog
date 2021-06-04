from datetime import datetime

class Log:
	fileName = ""
	def __init__(self, file):
		self.fileName = file+".log"

	def time(self):
		return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

	def info(self, message):
		self.log("info", message)

	def warning(self, message):
		self.log("warning", message)

	def debug(self, message):
		self.log("debug", message)

	def error(self, message):
		self.log("error", message)

	def log(self, mode, message):
		file = open(self.fileName, "a")
		file.write(mode+" - "+message+" - "+self.time()+"\n")
		file.close()
