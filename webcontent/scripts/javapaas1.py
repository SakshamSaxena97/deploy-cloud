#!/usr/bin/python2

import cgi
import commands
import subprocess

print "content-type: text/html"
print


print "<pre>"

code = cgi.FormContent()['code'][0]

fh=open('/webcontent/scripts/code.java','w')
fh.write(code + "\n")
fh.close()

print "<h4>OUTPUT :</h4>\n"
status=commands.getstatusoutput("sudo javac /webcontent/scripts/code.java")
if status[0] == 0:
	a=commands.getstatusoutput("sudo java code")
	print a[1]
else:
	print "<h4>Error:</h4>"
	b=status[1].split("\n")
#	print b	
#	i=0
	for i in b:	
		c=i.split("/webcontent/scripts/code.java")	
		print c[1]
		
print "</pre>"
