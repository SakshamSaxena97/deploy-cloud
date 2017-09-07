#!/usr/bin/python2

import cgi

print "content-type: text/html"


menuCh=cgi.FormContent()['setup'][0]

if menuCh == "staas":
	print "location: ../mainstorage.html"
	print

elif menuCh == "iaas":
	print "location: ../iaas.html"
	print

elif menuCh == "caas":
        print "location: ../caas.html"
        print

elif menuCh == "paas":
        print "location: ../paas_manage.html"
        print

elif menuCh == "naas":
        print "location: ../naas.html"
        print

else:

	print "Not Supported"

