from sys import exit
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
		if "-" in message:
			print("\033[1;31;40mError: message can't contain \"-\"")
			exit(1)
		if "-" in mode:
			print("\033[1;31;40mError: tag can't contain \"-\"")
			exit(1)
		file = open(self.fileName, "a")
		file.write(mode+"-"+message+"-"+self.time()+"\n")
		file.close()
