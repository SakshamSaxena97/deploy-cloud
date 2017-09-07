#!/usr/bin/python2

print "Content-Type: text/html"
print

import commands
import cgi

username=cgi.FormContent()['username'][0]
client_ip=cgi.FormContent()['client_ip'][0]
client_pass=cgi.FormContent()['client_pass'][0]
vg_name="myvg"

string_to_add="""[{0}]
             {1}  ansible_ssh_user=root ansible_ssh_pass={2}
""".format(username,client_ip,client_pass)


string_remove="""
- hosts: mysystem
  tasks:
   - blockinfile: 
       path: "/etc/ansible/hosts"
       block: |
             {0} 

- hosts: {1}
  tasks:
   - open_iscsi:
       login: no
       target: "{1}"  
       
- hosts: storage
  tasks:
   - service:
       name: tgtd
       state: stopped
   - lvol: 
       vg: {2}
       lv: {1}
       state: absent       
""".format(string_to_add,username,vg_name)


fh=open('../ansible/block_remove.yml','w')
fh.write(string_remove )
fh.close()


code_status=commands.getstatusoutput("sudo ansible-playbook ../ansible/block_remove.yml")
'''
if code_status[0]==0:
print "<b>DISK REMOVED SUCCESSFULLY !!</b>"
else:
print "<b>ERROR OCCURED DURING LOGOUT!!</b>"
'''
