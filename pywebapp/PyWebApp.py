# PyWebApp main file
# Under GNU GPL

appcode = ""

def addBlock(title=""):
	global appcode
	appcode += "<div class='iBlock'><h1>"+title+"</h1>"
def endBlock():
	global appcode
	appcode += "</div>"
	
def addText(text):
	global appcode
	appcode += "<p>"+text+"</p>"
	
def addButton(text,btype,param,color="white"):
	# btype can be: link or alert
	# color can be: white red or black
	global appcode
	if btype == "link":
		appcode += "<a href='"+param+"' class='iPush "
		if color == "white":
			appcode += "iBClassic"
		if color == "red":
			appcode += "iBWarn"
		if color == "black":
			appcode += "iBCancel"
		appcode += "' style='width:100%'>"+text+"</a>"
	
	if btype == "alert":
		appcode += "<a href='javascript:void(0)' class='iPush "
		if color == "white":
			appcode += "iBClassic"
		if color == "red":
			appcode += "iBWarn"
		if color == "black":
			appcode += "iBCancel"
		appcode += "' style='width:100%' onclick='javascript:alert(\""+param+"\")'>"+text+"</a>"
