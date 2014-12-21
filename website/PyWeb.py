## @file PyWeb.py
## @author Simsor
## @details Contains the main PyWeb definitions

#.############################
#    PYWEB FILE              #
#    UNDER GNU GPL LICENSE   #
#.############################

import sys

PYWEB_HTML4 = 4
PYWEB_HTML5 = 5

PYWEB_JS_INCLUDE = "include"
PYWEB_JS_CODE = "code"

#.###########################################################
#.##########  STYLE    #####################################

## @param txt The text
## @return a bold text
def bold(txt):
	txt = txt.replace("\n","<br />")
	return "<strong>"+txt+"</strong>"

## @param txt The text
## @return an italic text
def italic(txt):
	txt = txt.replace("\n","<br />")
	return "<em>"+txt+"</em>"

## @param txt The text
## @return an underlined text
def underline(txt):
	txt = txt.replace("\n","<br />")
	return "<u>"+txt+"</u>"

## @param txt The text
## @param to the page to link
## @param idd \p facultative the ID of the link
## @param cssclass \p facultative the "class" attribute
## @return a link
def link(txt,to,idd="",cssclass=""):
	txt = txt.replace("\n","<br />") # A little bit stupid, line warps in links...but never mind
	return "<a href='"+to+"' id='"+idd+"' class='"+cssclass+"'>"+txt+"</a>"

## @class PyWeb
## @details The main class of PyWeb
class PyWeb:
	
	## @brief Constructor
	## @details Initialize the page.
	## @param title The name of the page that should be genrated (eg: index.html)
	def __init__(self,title):

		self.page = ""
		self.pagename = title
	
	def createPage(self):
		"""Write the content of the page in the file set in the constructor"""
		htmlfile = open(self.pagename,"w")
		htmlfile.write(self.page)
		htmlfile.close()
		print "Generation completed:\nFile: "+self.pagename+"\nSize: "+str(len(self.page))+" characters"
	
	## Inits the HTML stuff
	## @param htmltype Either PYWEB_HTML5 or PYWEB_HTML4.
	## @return nothing
	def InitHTML(self,htmltype):
		if htmltype == PYWEB_HTML4:
			self.page += """<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" >\n"""

		elif htmltype == PYWEB_HTML5:
			self.page += """<!DOCTYPE html>
			<html>\n"""

		else:
			print "ERROR: Function: InitHTML Error: expected PYWEB_HTML4 or PYWEB_HTML5, found "+str(htmltype)+" instead"
			sys.exit(0)
	
	## @details Adds an image "Made with PyWeb", 'cause propaganda roxx
	## @return more people using PyWeb, why not ?
	def addPyWebLogo(self):
		self.page += "<img src=\"data/pyweb.png\" alt=\"Made with PyWeb\" title=\"A great library\" />"
	
#.###################################################################################################################
#.#########################               CONFIG                                #####################################
#.###################################################################################################################
	
	## @brief Begin config
	## @details Adds a &lt;head&gt; tag
	def beginConfig(self):
		
		self.page += "<head>\n"
	
	## @brief Set the stylesheet (*.css)
	## @param filename The path to the stylesheet
	## @param name \p facultative the name of the stylesheet
	def setStyleSheet(self,filename,name="Design"):

		self.page += '<link rel="stylesheet" name="'+name+'" media="screen" type="text/css" href="'+filename+'" />\n'
	
	## @brief Set page's title
	## @details Set the title viewable in the title bar of the browser
	## @param title the title
	def setTitle(self,title):

		self.page += "<title>"+title+"</title>\n"
	
	## @brief Insert some JavaScript in the page
	## @details You can include an existing file or directly use code
	## @param inserttype Either PYWEB_JS_INCLUDE or PYWEB_JS_CODE
	## @param content The path to the file or the code itself
	def insertJavascript(self,inserttype,content):
		if inserttype == PYWEB_JS_INCLUDE:
			self.page += "<script src=\""+content+"\" />\n"
		elif inserttype == PYWEB_JS_CODE:
			self.page += "<script>"+content+"</script>"
		else:
			print "Error: Function: insertJavascript Error: expected PYWEB_JS_INCLUDE or PYWEB_JS_CODE, found "+str(inserttype)+" instead."
			sys.exit(0)
	
	## @brief Ends the config part
	## @details add a &lt;/head&gt; tag
	def endConfig(self):

		self.page +="</head>\n"

#.###################################################################################################################
#.#############################                CONTENT                               ################################
#.###################################################################################################################
	
	## @brief Starts the content
	## @details Adds a &lt;body&gt; tag
	def beginContent(self):
		self.page += "<body>\n"

	## @brief Adds a paragraph
	## @details Create a &lt;p&gt; tag with text in
	## @param para The paragraph
	## @param cssclass \p facultative the "class" attribute
	## @param idd \p facultative the ID of the paragraph
	def addParagraph(self,para,cssclass="",idd=""):
		para = para.replace("\n","<br />")
		self.page += "<p id='"+idd+"' class='"+cssclass+"'>"+para+"</p>\n"
	## @brief Opens a paragraph
	## @details Create a &lt;p&gt; tag
	## @param cssclass \p facultative the "class" attribute
	## @param idd \p facultative the ID of the paragraph
	def newParagraph(self,cssclass="",idd=""):
		self.page += "<p id='"+idd+"' class='"+cssclass+"'>"
	## @brief Close the paragraph
	def endParagraph(self):
		self.page += "</p>\n"

	## @brief Adds a block
	## @details Create a &lt;div&gt; block and close it (&lt;div&gt;&lt;/div&gt;)
	## @param cssclass \p facultative the "class" attribute
	## @param idd \p facultative the ID of the block
	def addBlock(self,cssclass,idd):
		self.page += "<div id='"+idd+"' class='"+cssclass+"'></div>"
	## @brief Create a block
	## @details Open a &lt;div&gt; block
	def newBlock(self,idd,name="",cssclass=""):
		self.page += "<div id='"+idd+"' class='"+cssclass+"' name='"+name+"'>\n"
	## @brief Ends a block
	## @details Adds a &lt;/div&gt; tag
	def endBlock(self):
		self.page += "</div>\n"
	
	## Add text in the page
	## @param text The text to add (HTML works)
	def addText(self,text):
		text = text.replace("\n","<br />")
		self.page += text
	
	## Adds a title (&lt;h1&gt; tag)
	## @param txt the text of the title
	## @param idd \p facultative the ID of the title
	## @param cssclass \p facultative the "class" attribute
	def addTitle(self,txt,idd="",cssclass=""):
		self.page += "<h1 class=\""+cssclass+"\" id=\""+idd+"\">"+txt+"</h1>"
	
	## Adds a subtitle (&lt;h2&gt; tag)
	## @param txt the text of the title
	## @param idd \p facultative the ID of the title
	## @param cssclass \p facultative the "class" attribute
	def addSubTitle(self,txt,idd="",cssclass=""):
		self.page += "<h2 class=\""+cssclass+"\" id=\""+idd+"\">"+txt+"</h2>"
	
	#.#############    FORMS
	
	## Create a form
	## @param name the name of your form
	## @param action \p facultative the page to send data (usually a PHP page)
	## @param method \p facultative the method to use ("POST" or "GET")
	def beginForm(self,name,action="",method="POST"):
		self.page += "<form name=\""+name+"\" action=\""+action+"\" method=\""+method+"\">\n"
	
	## Adds an input field
	## @param inputtype Either "text","password","whatever"
	## @param name \p facultative the name of this input
	## @param idd \p facultative the ID of this input
	## @param cssclass \p facultative the "class" attribute
	def formAddInput(self,inputtype,name="",cssclass="",idd=""):
		self.page += "<input type=\""+inputtype+"\" name=\""+name+"\" class=\""+cssclass+"\" id=\""+idd+"\"/>\n"
	
	## Adds a submit button
	## @param name the value of the button
	## @param cssclass \p facultative the "class" attribute
	## @param idd \p facultative the ID of this Submit
	def formAddSubmit(self,name,cssclass="",idd=""):
		self.page += "<input type=\"submit\" value=\""+name+"\" class=\""+cssclass+"\" id=\""+idd+"\" />\n"
	
	## @details Ends the form (&lt;/form&gt;)
	def endForm(self):
		self.page += "</form>\n"
	#.###############

	#.############    MENUS
	
	## @details Create a menu (&lt;ul&gt;)
	def beginMenu(self):
		self.page += "<ul>\n\t"

	## Adds an item to the menu (&lt;li&gt;)
	## @param txt The text of the item
	## @param idd \p facultative the ID of the item
	## @param cssclass \p facultative the "class" attribute
	def menuAddItem(self,txt,idd="",cssclass=""):
		self.page += "<li id='"+idd+"' class='"+cssclass+"'>"+txt+"</li>\n\t"

	## @details Ends the menu (&lt;/ul&gt;)
	def endMenu(self):
		self.page += "</ul>\n"
	
	## @details Ends the content (&lt;/body&gt;)
	def endContent(self):
		self.page += "</body>\n"

#.################       TEMPLATES   ##################################################

	def addTemplate(self,function,param=None):
		if param == None:
			function(self)
		else:
			function(self,param)

#.####################################################################################################################

	##  @details End of the HTML part (&lt;/html&gt;)
	def end(self):
		self.page += "</html>"
