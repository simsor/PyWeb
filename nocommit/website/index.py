#!/usr/bin/python

from PyWeb import *
from siteTemplate import *

class MyWebPage(PyWeb):

	def __init__(self):

		self.p = PyWeb("index.html")
		self.p.InitHTML(PYWEB_HTML5)

		self.doConfig()
		self.doContent()

		self.p.end()

		self.p.createPage()

	def doConfig(self):

		self.p.beginConfig()
		self.p.setTitle("PyWeb")
		self.p.setStyleSheet("data/design.css")
		self.p.endConfig()

	
	def doContent(self):

		self.p.beginContent()
		self.p.addTemplate(siteTemplate,"A powerful web library.")
		
		self.p.newBlock("post")
		self.p.addSubTitle("Welcome to PyWeb",cssclass="title")
		self.p.newBlock("entry")

		self.p.addParagraph("Welcome to the official website of PyWeb.")
		self.p.addParagraph(bold("What is PyWeb ?")+"\nPyWeb is a very powerful Web library coded in the "+link("Python Programming Language","http://www.python.org")+".")
		
		self.p.addParagraph(bold("What are these features ?")+"\nFeatures are:")
		self.p.beginMenu()
		self.p.menuAddItem("Easy to learn if you already know Python")
		self.p.menuAddItem("Doesn't need a Python web server: all the code is transformed into pure xHTML/PHP code")
		self.p.menuAddItem("Support PHP throught "+italic("PyWebDynamic")+" module.")
		self.p.menuAddItem("PyWebDynamic uses SQLite so you doesn't need to rely on a limited number of MySQL databases.")
		self.p.endMenu()

		self.p.addParagraph(bold("Can I have an example of website using PyWeb ?\n")+"Let me see...here is one: this website is fully coded into PyWeb (I don't use PyWebDynamic because I don't need it) ! And the code is 59 lines long (with a lot of line-warps) !")

		self.p.endBlock() #entry
		self.p.endBlock() #post

		self.p.addTemplate(endSiteTemplate)

		self.p.endContent()


if __name__ == "__main__":
	m = MyWebPage()
