##########################
# PyWebDynamic main file #
# Under GNU GPL license  #
##########################

import sys
try:
	from PyWeb import *
except:
	print "Error: PyWebDynamic: You must have PyWeb installed on your computer."
	sys.exit(0)

class PyWeb(PyWeb):

	def beginDynamic(self):
		self.page += "<?php\n"
	def endDynamic(self):
		self.page += "?>\n"
	def addVariable(self,variable):
		variable.setPage(self.page)

	############################################

	def outputText(self,text):
		text = text.replace("\n","<br />")
		self.page += "echo \""+text+"\";"

class Variable:

	def __init__(self,name,value):
		self.name = name
		self.value = value
		

	def setValue(self,new):
		self.value = new
	
	def value(self):
		return self.value

	def setPage(self,page):
		self.page = page
