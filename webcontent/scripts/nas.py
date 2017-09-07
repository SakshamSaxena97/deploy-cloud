#!/usr/bin/python2

print "content-type: text/html"
print


import commands
import cgi


count=cgi.FormContent()['count'][0]

username=cgi.FormContent()['username'][0]

client_ip=cgi.FormContent()['client_ip'][0]

client_pass=cgi.FormContent()['client_pass'][0]

string_to_add="""[{0}]
             {1}  ansible_ssh_user=root ansible_ssh_pass={2}
""".format(username,client_ip,client_pass)

print "hello"


i=1
while i <= int(count):
   string="""
- hosts: mysystem
  tasks:
   - blockinfile: 
       path: "/etc/ansible/hosts"
       block: |
             {0} 

- hosts: {1}
  tasks:
   - openvswitch_bridge:
       bridge: "{1}-br{2}"
       state: present

   - file:
       path: "/etc/docker/{1}-br{2}.jason"
       state: touch
       mode: 0644

   - lineinfile: 
       path: "/etc/docker/{1}-br{2}.jason"
       line: '"bridge" : "{1}-br{2}.jason"'
             
          """.format(string_to_add,username,i)
   f=open('../ansible/nas.yml','w')
   f.write(string)
   f.close()
   print commands.getstatusoutput("sudo ansible-playbook ../ansible/nas.yml")
   i=i+1




 

	
