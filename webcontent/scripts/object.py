#!/usr/bin/python2

print "Content-Type: text/html"
print

import commands
import cgi

print "hello"

username=cgi.FormContent()['username'][0]
part_size=cgi.FormContent()['part_size'][0]
client_ip=cgi.FormContent()['client_ip'][0]
client_pass=cgi.FormContent()['client_pass'][0]
root_pass=cgi.FormContent()['root_password'][0]

storage_ip = "192.168.43.163"
storage_pass = "redhat"

vg_name="myvg"

'''
#checking vg
vg_status=commands.getstatusoutput("sudo ansible storage -a 'vgdisplay {0}'".format(vg_name))
if vg_status[0] == 0:
   print "hello"
else:
   print "vg is not present,please check manually"
   exit()

#creating lv

yml_string="""
- hosts: storage
  tasks:
    - lvol:
       vg: "{0}"
       lv: "{1}"
       size: {2}g
    - filesystem:
       fstype: ext4
       dev: "/dev/{0}/{1}"
    - file:
       path: "/share/{1}-lv1"
       state: directory              
    - mount:
       path: "/share/{1}-lv1"
       src: "/dev/{0}/{1}"
       fstype: ext4
       state: mounted
    - user:
       name: "{1}"
       password: "{3}"
    
""".format(vg_name,username,part_size,client_pass)

fh=open('/mycode/scripts/object.yml','w')
fh.write(yml_string + "\n")
fh.close()

ansible_status=commands.getstatusoutput("sudo ansible-playbook object.yml")

if ansible_status[0] == 0:
  print "hello"
else:
  print ansible_status
  exit()




#updating /etc/ansible/hosts (adding entry of client)
string_to_add="""[{0}]
              {1}  ansible_ssh_user=root ansible_ssh_pass={2}
""".format(username,client_ip,root_pass)

yml_string="""
- hosts: mysystem
  tasks:
    - blockinfile: 
        path: "/etc/ansible/hosts"
        block: |
              {0} 
""".format(string_to_add)

fh=open('/mycode/scripts/object.yml','w')
fh.write(yml_string + "\n")
fh.close()

print commands.getstatusoutput("sudo ansible-playbook object.yml")

#creating disk/folder on client side

yml_string="""
- hosts: {0}
  tasks:
   - file:
       path: "/media/{0}"
       state: directory
""".format(username,storage_ip)              
    



fh=open('/mycode/scripts/object.yml','w')
fh.write(yml_string + "\n")
fh.close()


commands.getstatusoutput("sudo ansible-playbook object.yml")

'''
a=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} echo 'redhat' | sshfs -t sshfs {4}@:/dev/{5}/{4} /media/{4}".format(root_pass,client_ip,storage_pass,storage_ip,username,myvg))

print a







