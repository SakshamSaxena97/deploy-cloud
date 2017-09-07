#!/usr/bin/python2

print "content-type: text/html"

import cgi

user_choice=cgi.FormContent()['setup'][0]

if user_choice == "create":
   print "location:../block_create.html"
   print
elif user_choice == "extend":
   print "location:../block_extend.html"
   print
elif user_choice == "reduce":
   print "location:../block_reduce.html"
   print
elif user_choice == "remove":
   print "location:../block_remove.html"
   print 
 



