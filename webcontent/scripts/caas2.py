#!/usr/bin/python2

import cgi

print "content-type: text/html"


a=cgi.FormContent()['caas'][0]

if a == "confi":
        print "location: ../caas2.html"
        print

elif a == "manage":
        print "location: ../caas1.html"
        print

else:
	print "Not Supprted"
