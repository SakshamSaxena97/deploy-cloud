#!/usr/bin/python

print "content-type: text/html"
print

import cgi
import commands

server_ip=cgi.FormContent()['server_ip'][0]
server_pass=cgi.FormContent()['server_pass'][0]
#iqn=cgi.FormContent()['iqn'][0]
#disk_name=cgi.FormContent()['disk_name'][0]

a=commands.getstatusoutput("sshpass -p {0} scp root@{1}:/etc/tgt/targets.conf  /block_st".format(server_pass,server_ip))
print a
'''
disk_entry="""<target {0}>
              backing-store {1}
              </target> 
           """.format(iqn_name,disk_name)

bsfh=open('/mnt/targets.conf' , 'a')
bsfh.write(disk_entry + "\n")
bsfh.close()
commands.getstatusoutput("sshpass -p {0} scp  /mnt/targets.conf  root@{1}:/etc/tgt/".format(server_pass,server_ip))

commands.getstatusoutput("sudo systemctl restart tgtd")
'''
