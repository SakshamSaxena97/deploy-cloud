#!/usr/bin/python2

print "Content-Type: text/html"
print

import commands
import cgi

print "hello"

username=cgi.FormContent()['username'][0]
client_ip=cgi.FormContent()['client_ip'][0]
client_pass=cgi.FormContent()['client_pass'][0]
storage_size=cgi.FormContent()['storage_size'][0]
vg_name="myvg"
storage_ip="192.168.43.163"


string_to_add="""[{0}]
             {1}  ansible_ssh_user=root ansible_ssh_pass={2}
""".format(username,client_ip,client_pass)


block_string="""
- hosts: storage
  tasks:
   - lvol:
       vg: "{0}"
       lv: "{1}"
       size: {2}g 

   - blockinfile: 
       path: "/etc/tgt/targets.conf"
       block: |
           <target {1}>
            backing-store /dev/{0}/{1}
           </target> 

   - service:
       name: tgtd
       state: restarted


- hosts: mysystem
  tasks:
   - blockinfile: 
       path: "/etc/ansible/hosts"
       block: |
             {3} 



- hosts: {1}
  tasks:
   - open_iscsi:
       portal: '{1}'
       login: yes
       discover: yes
   - package:
       name: "iscsi-initiator"
       type: present
       use: yum     
""".format(vg_name,username,storage_size,string_to_add,storage_ip)



fh=open('../ansible/block_create.yml','w')
fh.write(block_string )
fh.close()




print commands.getstatusoutput("sudo ansible-playbook ../ansible/block_create.yml")



























