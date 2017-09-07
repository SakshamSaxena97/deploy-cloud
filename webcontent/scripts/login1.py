#!/usr/bin/python2

import cgi
import json

print "content-type: text/html"

#userName = raw_input("Enter username")
#passWord = raw_input ("Enter password")

userName=cgi.FormContent()['username'][0]
passWord=cgi.FormContent()['password'][0]

input_file=open('data.json', 'r')
json_decode=json.load(input_file)
valid=0
for i in range(len(json_decode['info'])):
	a = json_decode['info'][i]['username']
	b = json_decode['info'][i]['password'] 
	if a == userName and b == passWord:
		print "location: ../menu.html"
		print
		#print("Success")
		valid = 1
		break
	
	else:		
		print "location: ../signup.html"
		print
#auser="saksham"
#apass="saksham"

#if userName==auser and passWord==apass:
#	print "location: ../form.html"
#	print

#else:

#	print "location: ../login.html"
#	print
