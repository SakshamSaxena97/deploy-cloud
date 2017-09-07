#!/usr/bin/python2

import commands
import cgi


print "content-type: text/html"
print


imageid=cgi.FormContent()['iid'][0]
imagename=cgi.FormContent()['iname'][0]
ip=cgi.FormContent()['ip'][0]
password=cgi.FormContent()['passw'][0]
print imageid
c=commands.getstatusoutput("sudo docker tag {0} {1}".format(imageid,imagename))
if c[0]!=0:
	print c
d=commands.getstatusoutput("sudo docker save {0} > /tmp/{0}.tar".format(imagename))
om=commands.getstatusoutput("sudo scp /tmp/{0}.tar /root/doc".format(imagename))
if d[0]!=0:
	print d
	
f=commands.getstatusoutput("sudo sshpass -p {0} scp /root/doc/{1}.tar {2}:/".format(password,imagename,ip))
if f[0]==0:
	print "uploaded sucessfully on {}".format(ip)
else:
	print "cannot be uploaded check ssh service"
	


