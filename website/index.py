#!/usr/bin/python

from PyWeb import *

class MyWebPage:

	def __init__(self):

		self.page = PyWeb("index.html")
		self.page.InitHTML(PYWEB_HTML5)

		self.doConfig()
		self.doContent()

		self.page.end()

		self.page.createPage()

	def doConfig(self):

		self.page.beginConfig()
		self.page.setTitle("PyWeb")
		self.page.setStyleSheet("data/design.css")
		self.page.endConfig()

	
	def doContent(self):

		self.page.beginContent()
		self.doMenu()
		
		self.page.newBlock("logo")
		self.page.addTitle(link("PyWeb","#"))
		self.page.addParagraph(italic("A powerful Python Web Library"))
		self.page.endBlock() #logo

		self.page.newBlock("page")
		self.page.newBlock("content")
		self.page.newBlock("content-bgtop")
		self.page.newBlock("content-bgbtm")
		
		self.page.newBlock("post")
		self.page.addSubTitle("Welcome to PyWeb",cssclass="title")
		self.page.newBlock("entry")

		self.page.addParagraph("Welcome to the official website of PyWeb.")
		self.page.addParagraph(bold("What is PyWeb ?")+"\nPyWeb is a very powerful Web library coded in the "+link("Python Programming Language","http://www.python.org")+".")
		
		self.page.addParagraph(bold("What are these features ?")+"\nFeatures are:")
		self.page.beginMenu()
		self.page.menuAddItem("Easy to learn if you already know Python")
		self.page.menuAddItem("Doesn't need a Python web server: all the code is transformed into pure xHTML/PHP code")
		self.page.menuAddItem("Support PHP throught "+italic("PyWebDynamic")+" module.")
		self.page.menuAddItem("PyWebDynamic uses SQLite so it has very high performance.")
		self.page.endMenu()

		self.page.addParagraph(bold("Can I have an example of website using PyWeb ?\n")+"Let me see...here is one: this website is fully coded into PyWeb (I don't use PyWebDynamic because I don't need it) ! And the code is 93 lines long (with a lot of line-warps) !")

		self.page.endBlock() #entry
		self.page.endBlock() #post

		self.page.endBlock() #content-bgbtm
		self.page.endBlock() #content-bgtop
		self.page.endBlock() #content
		
		self.page.addText("<div style='clear:both;'></div>")
		self.page.newBlock("footer")
		self.page.addParagraph("The design of this site is from "+link("CSS Templates","http://freecsstemplates.org")+".")
		self.page.addPyWebLogo()
		self.page.endBlock() #footer

		self.page.endBlock() #page

		self.page.endContent()


	def doMenu(self):
		
		self.page.newBlock("header")
		self.page.newBlock("menu")
		self.page.beginMenu()

		self.page.menuAddItem(link("Home","index.html",cssclass="first"),cssclass="current_page_item")
		self.page.menuAddItem(link("Download","download.html"))

		self.page.endMenu()

		self.page.endBlock() #menu
		self.page.endBlock() #header



if __name__ == "__main__":
	mypage = MyWebPage()
