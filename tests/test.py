#!/usr/bin/python

from PyWeb import *
from template import *
#from PyWebDynamic import *

class TEST:

	def __init__(self):

		self.p = PyWeb("test.html")
		self.p.addTemplate(myTemplate)
		
		self.p.createPage()
if __name__ == "__main__":
	ttestsst = TEST()
