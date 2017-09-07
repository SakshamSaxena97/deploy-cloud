#!/usr/bin/python2

import cgi
import commands
import subprocess

print "content-type: text/html"
print


print "<pre>"

code = cgi.FormContent()['code'][0]

fh=open('/webcontent/scripts/code.py','w')
fh.write(code + "\n")
fh.close()

print "<h4>OUTPUT :</h4>\n"
status=commands.getstatusoutput("sudo python /webcontent/scripts/code.py")
if status[0] == 0:
	print status[1]
else:
	print "<h4>Error:</h4>"
	b=status[1].split("/webcontent/scripts/code.py")
	print b[1]	
#	i=0
#	for i in b:	
#		c=i.split("\n")	
#		print c

print "</pre>"
