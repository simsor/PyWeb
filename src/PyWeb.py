##############################
#    PYWEB FILE              #
#    UNDER GNU GPL LICENSE   #
##############################

import sys

PYWEB_HTML4 = 4
PYWEB_HTML5 = 5

PYWEB_JS_INCLUDE = "include"
PYWEB_JS_CODE = "code"

class PyWeb:

	def __init__(self,title):

		self.page = ""
		self.pagename = title

	def createPage(self):
		htmlfile = open(self.pagename,"w")
		htmlfile.write(self.page)
		htmlfile.close()
		print "Generation completed:\nFile: "+self.pagename+"\nSize: "+str(len(self.page))+" characters"

	def InitHTML(self,htmltype):

		if htmltype == PYWEB_HTML4:
			self.page += """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" >\n"""

		elif htmltype == PYWEB_HTML5:
			self.page += """<!DOCTYPE html>
			<html>\n"""

		else:
			print "ERROR: Function: InitHTML Error: expected PYWEB_HTML4 or PYWEB_HTML5, found "+str(htmltype)+" instead"
			sys.exit(0)

	def addPyWebLogo(self):
		self.page += "<img src=\"data/pyweb.png\" alt=\"Made with PyWeb\" title=\"A great library\" />"
	
#####################################################################################################################
###########################               CONFIG                                #####################################
#####################################################################################################################

	def beginConfig(self):
		
		self.page += "<head>\n"

	def setStyleSheet(self,filename,name="Design"):

		self.page += '<link rel="stylesheet" name="'+name+'" media="screen" type="text/css" href="'+filename+'" />\n'

	def setTitle(self,title):

		self.page += "<title>"+title+"</title>\n"

	def insertJavascript(self,inserttype,content):
		if inserttype == PYWEB_JS_INCLUDE:
			self.page += "<script src=\""+content+"\" />\n"
		elif inserttype == PYWEB_JS_CODE:
			self.page += "<script>"+content+"</script>"
		else:
			print "Error: Function: insertJavascript Error: expected PYWEB_JS_INCLUDE or PYWEB_JS_CODE, found "+str(inserttype)+" instead."
			sys.exit(0)
	
	def endConfig(self):

		self.page +="</head>\n"

#####################################################################################################################
###############################                CONTENT                               ################################
#####################################################################################################################

	def beginContent(self):
		self.page += "<body>\n"


	def addParagraph(self,para,cssclass="",idd=""):
		para = para.replace("\n","<br />")
		self.page += "<p id='"+idd+"' class='"+cssclass+"'>"+para+"</p>\n"
	def newParagraph(self):
		self.page += "<p>"
	def endParagraph(self):
		self.page += "</p>\n"

	
	def addBlock(self,idd,name):
		self.page += "<div id='"+idd+"' name='"+name+"'></div>"
	def newBlock(self,idd,name="",cssclass=""):
		self.page += "<div id='"+idd+"' class='"+cssclass+"' name='"+name+"'>\n"

	def endBlock(self):
		self.page += "</div>\n"

	def addText(self,text):
		text = text.replace("\n","<br />")
		self.page += text

	def addTitle(self,txt,idd="",cssclass=""):
		self.page += "<h1 class=\""+cssclass+"\" id=\""+idd+"\">"+txt+"</h1>"
	
	def addSubTitle(self,txt,idd="",cssclass=""):
		self.page += "<h2 class=\""+cssclass+"\" id=\""+idd+"\">"+txt+"</h2>"
	
	###############    FORMS

	def beginForm(self,name,action="",method="POST"):
		self.page += "<form name=\""+name+"\" action=\""+action+"\" method=\""+method+"\">\n"
	def formAddInput(self,inputtype,name="",cssclass="",idd=""):
		self.page += "<input type=\""+inputtype+"\" name=\""+name+"\" class=\""+cssclass+"\" id=\""+idd+"\"/>\n"
	def formAddSubmit(self,name,cssclass="",idd=""):
		self.page += "<input type=\"submit\" value=\""+name+"\" class=\""+cssclass+"\" id=\""+idd+"\" />\n"
	def endForm(self):
		self.page += "</form>\n"
	#################

	##############    MENUS
	
	def beginMenu(self):
		self.page += "<ul>\n\t"
	def menuAddItem(self,txt,idd="",cssclass=""):
		self.page += "<li id='"+idd+"' class='"+cssclass+"'>"+txt+"</li>\n\t"
	def endMenu(self):
		self.page += "</ul>\n"

	def endContent(self):
		self.page += "</body>\n"


######################################################################################################################
	def end(self):
		self.page += "</html>"


#############################################################
############  STYLE    #####################################

def bold(txt):
	txt = txt.replace("\n","<br />")
	return "<strong>"+txt+"</strong>"
def italic(txt):
	txt = txt.replace("\n","<br />")
	return "<em>"+txt+"</em>"
def underline(txt):
	txt = txt.replace("\n","<br />")
	return "<u>"+txt+"</u>"
def link(txt,to,idd="",cssclass=""):
	txt = txt.replace("\n","<br />") # A little bit stupid, line warps in links...but never mind
	return "<a href='"+to+"' id='"+idd+"' class='"+cssclass+"'>"+txt+"</a>"
