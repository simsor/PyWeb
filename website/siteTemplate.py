## @file siteTemplate.py
## @autor Simsor
## @details The template of the site

from PyWeb import *

def siteTemplate(p,subtitle):
	p.newBlock("header")
	p.newBlock("menu")
	p.beginMenu()
	p.menuAddItem(link("Home","index.html",cssclass="first"),cssclass="current_item")
	p.menuAddItem(link("Download","download.html"))
	p.endMenu()
	p.endBlock() #menu
	p.endBlock() #header
	p.newBlock("logo")
	p.addTitle(link("PyWeb","#"))
	p.addParagraph(italic(subtitle))
	p.endBlock() #logo
	p.newBlock("")
	p.newBlock("content")
	p.newBlock("content-bgtop")
	p.newBlock("content-bgbtm")


def endSiteTemplate(p):
	p.endBlock() #content-bgbtm
	p.endBlock() #content-bgtop
	p.endBlock() #content
	p.addText("<div style='clear:both;'></div>")
	p.newBlock("footer")
	p.addParagraph("The design of this site is from "+link("CSS Templates","http://freecsstemplates.org")+".")
	p.addPyWebLogo()
	p.endBlock() #footer
	p.endBlock() #page
