#!/usr/bin/python

print "content-type: text/html"

import cgi

choice=cgi.FormContent()['choice'][0]
if choice == "object":
   print "location:../object_storage.html"
   print
elif choice == "block":
   print "location:../block.html"
   print
else:
   print "Service not supported"

