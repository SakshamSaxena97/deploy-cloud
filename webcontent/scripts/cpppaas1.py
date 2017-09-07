#!/usr/bin/python2

import cgi
import commands
import subprocess

print "content-type: text/html"
print


print "<pre>"

code = cgi.FormContent()['code'][0]

fh=open('/webcontent/scripts/code.cpp','w')
fh.write(code + "\n")
fh.close()

print "<h4>OUTPUT :</h4>\n"
status=commands.getstatusoutput("sudo g++ /webcontent/scripts/code.cpp")
if status[0] == 0:
	a=commands.getstatusoutput("./a.out")
	print a[1]
else:
	print "</h4>Error:</h4>"
	b=status[1].split("\n")
#	print b	
#	i=0
	for i in b:	
		c=i.split("/webcontent/scripts/code.cpp")	
		print c[1]
		
print "</pre>"
