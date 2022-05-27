from datetime import datetime
from os.path import exists

class Log:
	def __init__(self, path, force=False):
		add = '.log'
		if path.split('.')[-1] == 'log':
			add = ''
		self.file_name = path+add
		
		if exists(self.file_name) == False or force:
			with open(self.file_name, 'w') as file:
				file.write('')
		else:
			raise ValueError('\033[1;31;40mFile with suggested name already exists, choose force=True to overwrite it')

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
			raise ValueError("\033[1;31;40mError: message can not contain \"-\"")
		if "-" in mode:
			raise ValueError("\033[1;31;40mError: tag can not contain \"-\"")

		with open(self.file_name, 'a') as file:
			file.write(mode+"-"+message+"-"+self.time()+"\n")
