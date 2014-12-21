appTitle = "HELLO WORLDZ"
backButton_text = "Back"     # Change this to accord your language
pages = [ "page1.py" ]


















































pagecode = '<!DOCTYPE html5>\n<html>\n<head>\n<title>'+appTitle+'</title>\n<meta name="viewport" content="width=device-width; initial-scale=1.0; maximum-scale=1.0; user-scalable=0;" />\n<link rel="stylesheet" href="WebApp/Design/Render.css" />\n<script type="text/javascript" src="WebApp/Action/Logic.js"></script>\n</head><body>\n<div id="WebApp">'

import imp

data = imp.load_source("data","index.py")

pagecode += "<div id='iHeader'><a href='#' id='waBackButton'>"+backButton_text+"</a><span id='waHeadTitle'>"+appTitle+"</span></div>"
pagecode += "<div id='iGroup'>"
pagecode += "<div class='iLayer' id='wa"+data.pageid+"' title='"+data.title+"'>"
pagecode += data.PWA.appcode
pagecode += "</div>"

i = 0
while i <= len(pages)-1:
	data.PWA.appcode = ""
	data = imp.load_source("data",pages[i])
	
	pagecode += "<div class='iLayer' id='wa"+data.pageid+"' title='"+data.title+"'>"
	pagecode += data.PWA.appcode
	pagecode += "</div>"
	
	i += 1



pagecode += "</div></div></body></html>"

indexHTML = open("index.html","w")
indexHTML.write(pagecode)
indexHTML.close()
