#!/usr/bin/python

print "content-type: text/html"

import cgi

user_choice=cgi.FormContent()['choice'][0]

if user_choice == "object":
   print "location:../object_menu.html"
   print
elif user_choice == "block":
   print "location:../block_menu.html"
   print


