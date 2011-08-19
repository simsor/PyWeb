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
	def variable(self,name,value):
		if value.find("PHP") != 0:
			try:
				int(value)
				ok = True # value is a number
			except ValueError:
				ok = False # value is a string
			if ok:
				self.page += "$"+name+" = "+value+";\n"
			else:
				self.page += "$"+name+" = \""+value+"\";\n"

		else:
			value = value.replace("PHP","",1)
			self.page += "$"+name+" = "+value+";\n"

	############################################

	def outputText(self,text):
		text = text.replace("\n","<br />")
		self.page += "echo \""+text+"\";\n"
	
	############################################

#	def if(self,test):
#		self.page += "if ("+test+")\n{\n"
#	def endif(self):
#		self.page += "}\n"
#	
#	def elif(self,test):
#		self.page += "else if ("+test+")\n{\n"
#	def else(self)
#		self.page += "else\n{\n"
	

	##############    SQLITE MANAGEMENT ########

	def openSQLite(self,filename):
		self.page += "$sqlitedb = new SQLiteDatabase('"+filename+"');\n"
	def SQLiteQuery(self,var,query):
		query = query.replace("\"","\\\"")
		self.page += "$"+var+" = $sqlitedb->query(\""+query+"\");\n"
