#!/usr/bin/python2

import cgi
import commands

print "content-type: text/html"
print

print "hello"

imageName=cgi.FormContent()['image'][0]
print imageName

commands.getstatusoutput("sudo docker run -dit --name saksham-centos-1 {0}".format(imageName))

ipstatus=commands.getstatusoutput("sudo docker inspect saksham-centos-1 | jq '.[].NetworkSettings.Networks.bridge.IPAddress'")

print ipstatus[1].strip('"')

print "<a href= ../docker-shell.html> Click here to get online shell </a>"
print "<a href=docker-stop.py>Stop ur Container</a>"

