#!/usr/bin/python

from PyWeb import *
from siteTemplate import *

class Download:

	def __init__(self):
		self.p = PyWeb("download.html")
		self.p.InitHTML(PYWEB_HTML5)

		self.doConfig()
		self.doContent()

		self.p.end()
		self.p.createPage()

	def doConfig(self):
		self.p.beginConfig()
		self.p.setTitle("PyWeb - Download")
		self.p.setStyleSheet("data/design.css")
		self.p.endConfig()

	def doContent(self):

		self.p.beginContent()
		
		self.p.addTemplate(siteTemplate,"download pyweb")

		self.p.newBlock("post")
		self.p.addSubTitle("Download")
		self.p.newBlock("entry")

		self.p.addParagraph("You can download PyWeb from its GitHub repository as a "+link("ZIP archive","http://github.com/simsor/PyWeb/zipball/master")+" or a "+link("TAR archive","http://github.com/simsor/PyWeb/tarball/master")+".")
		self.p.addParagraph("The archive contains: the library in "+bold("lib/")+", the source in "+bold("src/")+", the "+bold("LICENSE")+" and the "+bold("README")+".")
		self.p.addParagraph(italic("PyWebDynamic")+" is included. To use it, you must have a Web HTTP server supporting PHP5 (almost all the Web servers that support PHP supports PHP5, but search first).")

		self.p.endBlock() #entry
		self.p.endBlock() #post

		self.p.addTemplate(endSiteTemplate)
		self.p.endContent()



if __name__ == "__main__":
	down = Download()
