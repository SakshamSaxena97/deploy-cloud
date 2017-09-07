#!/usr/bin/python2

import commands
import cgi


print "content-type: text/html"
print

print"<form action='/scripts/caasfinal2.py'>"
g="ok"
h="ok"
f="ok"

if cgi.FormContent()['extension'][0]=="simple":
	simple=cgi.FormContent()['extension'][0]
elif cgi.FormContent()['extension'][0]=="ssh":
	g=cgi.FormContent()['extension'][0]
	if cgi.FormContent()['extension'][1]=="simple":		
		simple=cgi.FormContent()['extension'][1]
	elif cgi.FormContent()['extension'][1]=="httpd":
		h=cgi.FormContent()['extension'][1]
		if cgi.FormContent()['extension'][2]=="simple":
			simple=cgi.FormContent()['extension'][2]
		elif cgi.FormContent()['extension'][2]=="nfs":
			f=cgi.FormContent()['extension'][2]
	elif cgi.FormContent()['extension'][1]=="nfs":
		f=cgi.FormContent()['extension'][1]

elif cgi.FormContent()['extension'][0]=="httpd":
	h=cgi.FormContent()['extension'][0]
	if cgi.FormContent()['extension'][1]=="simple":
		simple=cgi.FormContent()['extension'][1]
	elif cgi.FormContent()['extension'][1]=="nfs":
		f=cgi.FormContent()['extension'][1]
elif cgi.FormContent()['extension'][0]=="nfs":
		f=cgi.FormContent()['extension'][0]
	




def hello(a,b,c):

	if 0==0:
		print "ok"			
		dest=commands.getstatusoutput("sudo scp /root/doc/Dockerfile /tmp/Dockerfile.txt")
		x=commands.getstatusoutput("sudo chown apache /tmp/Dockerfile.txt")
		f=open("/tmp/Dockerfile.txt",'w')
		f.write("FROM experiment:v1\n")
		f.close()
		dest=commands.getstatusoutput("sudo scp /tmp/Dockerfile.txt /root/doc/Dockerfile")
	
	
	if a=="ssh":
		print "ok"
		run="RUN yum install"		
		dest=commands.getstatusoutput("sudo scp /root/doc/Dockerfile /tmp/Dockerfile.txt")
		f=open("/tmp/Dockerfile.txt",'a')
		execu="echo /usr/sbin/sshd"
		ok="RUN {} >> /root/.bashrc".format(execu)
		s="fuse-sshfs.x86_64","libssh2.x86_64","openssh.x86_64","openssh-clients.x86_64","openssh-server.x86_64","sshpass.x86_64"
		f.write("\n{0} {1} -y\n{0} {2} -y\n{0} {3} -y\n{0} {4} -y\n{0} {5} -y\n{0} {6} -y\n{7}".format(run,s[0],s[1],s[2],s[3],s[4],s[5],ok))
		f.close()
		dest=commands.getstatusoutput("sudo scp /tmp/Dockerfile.txt /root/doc/Dockerfile")
		

			
	if b=='httpd':
		run="RUN yum install"		
		dest=commands.getstatusoutput("sudo scp /root/doc/Dockerfile /tmp/Dockerfile.txt")
		f=open("/tmp/Dockerfile.txt",'a')
		execu="echo /usr/sbin/httpd"
		ok="RUN {} >> /root/.bashrc".format(execu)
		s="httpd.x86_64"
		f.write("\n{0} {1} -y\n{2}".format(run,s,ok))
		f.close()
		dest=commands.getstatusoutput("sudo scp /tmp/Dockerfile.txt /root/doc/Dockerfile")
	
			
	if c=='nfs':
		run="RUN yum install"		
		dest=commands.getstatusoutput("sudo scp /root/doc/Dockerfile /tmp/Dockerfile.txt")
		f=open("/tmp/Dockerfile.txt",'a')
		execu="echo /usr/sbin/rpc.nfsd $RPCNFSDARGS"
		ok="RUN {} >> /root/.bashrc".format(execu)
		s="nfs-utils"
		f.write("\n{0} {1} -y\n{2}".format(run,s,ok))
		f.close()
		dest=commands.getstatusoutput("sudo scp /tmp/Dockerfile.txt /root/doc/Dockerfile")
		build=commands.getstatusoutput("sudo docker build /root/doc")
			
	

	if 0==0:
		build=commands.getstatusoutput("sudo docker build /root/doc")
		if build[0]==0:
			a=build[1].split('\n')
			b=a[-1].split(" ")
			print b[-1]
			print "image is ready\n"
			print "<br/>"
			print "<input type='hidden' name='iid' value={}>".format(b[-1])
			print "Enter image name :  <input type='text' name='iname'>"
			print "<br/>"
			print "Enter the ip :  <input type='text' name='ip'>"
			print "<br/>"
			print "Enter the password :  <input type='password' name='passw' >"
			print "<br/>"
			print "<input type='submit' />"
		else:
			pingStatus=commands.getstatusoutput("sudo -c 7 ping google.com")
			if pingStatus[0]==0:
				print "epel configuratiion problem in docker"
			else :
				print "internet connectivity problem "
			


ds=commands.getstatusoutput("sudo systemctl restart docker")

if ds[0]==0:	
	hello(g,h,f)
else:
	print "docker is not configured\n"
	print "installing docker......"
	f=open("/tmp/docker.repo",'w')
	f.write("[docker]\nbaseurl=https://yum.dockerproject.org/repo/main/centos/7/\ngpgcheck=0")
	f.close()
	ole=commands.getstatusoutput("sudo scp /tmp/Docker.repo /etc/yum.repos.d/docker.repo")
	a=commands.getstatusoutput("sudo yum install docker")
	if a[0]== 0:
		print "docker is installed"
	else :
		print "internet connectivity problem"
print "</form>"


