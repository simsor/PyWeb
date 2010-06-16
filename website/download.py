#!/usr/bin/python

from PyWeb import *

class Download:

	def __init__(self):
		self.page = PyWeb("download.html")
		self.page.InitHTML(PYWEB_HTML5)

		self.doConfig()
		self.doContent()

		self.page.end()
		self.page.createPage()

	def doConfig(self):
		self.page.beginConfig()
		self.page.setTitle("PyWeb - Download")
		self.page.setStyleSheet("data/design.css")
		self.page.endConfig()

	def doContent(self):

		self.page.beginContent()
		self.doMenu()

		self.page.newBlock("logo")
		self.page.addTitle(link("pyweb","#"))
		self.page.addParagraph("Download PyWeb")
		self.page.endBlock() # logo

		self.page.newBlock("page")
		self.page.newBlock("content")
		self.page.newBlock("content-bgtop")
		self.page.newBlock("content-bgbtm")

		self.page.newBlock("post")
		self.page.addSubTitle("Download")
		self.page.newBlock("entry")

		self.page.addParagraph("You can download PyWeb from its GitHub repository as a "+link("ZIP archive","#")+" or a "+link("TAR archive","#")+".")
		self.page.addParagraph("The archive contains: the library in "+bold("lib/")+", the source in "+bold("src/")+", the "+bold("LICENSE")+" and the "+bold("README")+".")
		self.page.addParagraph(italic("PyWebDynamic")+" is included. To use it, you must have a Web HTTP server supporting PHP (almost all the Web servers support PHP).")

		self.page.endBlock() #entry
		self.page.endBlock() #post

		self.page.endBlock() #content-bgbtm
		self.page.endBlock() #content-bgtop
		self.page.endBlock() #content

		self.page.addText("<div style=\"clear:both;\"></div>")
		self.page.newBlock("footer")
		self.page.addParagraph("The design of this site is from "+link("CSS Templates","http://www.freecsstemplates.org")+".")
		self.page.addPyWebLogo()
		self.page.endBlock() #footer

		self.page.endBlock() #page

		self.page.endContent()


	def doMenu(self):

		self.page.newBlock("header")
		self.page.newBlock("menu")
		self.page.beginMenu()
		self.page.menuAddItem(link("Home","index.html",cssclass="first"))
		self.page.menuAddItem(link("Download","download.html"),cssclass="current_page_item")
		self.page.endMenu()
		
		self.page.endBlock() #menu
		self.page.endBlock() #header



if __name__ == "__main__":
	down = Download()
