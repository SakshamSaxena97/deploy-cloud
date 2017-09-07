#!/usr/bin/python2

print "content-type: text/html"

import cgi
import json

#userName = raw_input("Enter username")
#passWord = raw_input ("Enter password")

userName=cgi.FormContent()['username'][0]
passWord=cgi.FormContent()['password'][0]

input_file=open('data.json', 'r')
json_decode=json.load(input_file)

json_decode['info'].append({'username':userName,'password':passWord})

with open ('data.json','w') as f:
	v=json.dumps(json_decode)
	f.write(v)

print "location: ../login1.html"
print 


