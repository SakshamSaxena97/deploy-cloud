#!/usr/bin/python2

print "content-type: text/html"
print

import commands
import getpass
import cgi 

#server_ip=raw_input("enter ip where you want to setup nfs : ")
#server_pass=getpass.getpass("enter password : ")

server_ip=cgi.FormContent()['server_ip'][0]
server_pass=cgi.FormContent()['server_pass'][0]

vg_status=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} vgdisplay myvg".format(server_pass,server_ip))
if vg_status[0]!= 0:
    print "error ,first create vg manually and then run this again"
    exit()
else:
    print "ok\n"

#username=raw_input("enter username : ")
#part_size=raw_input("enter size of drive : ")
username=cgi.FormContent()['username'][0]
part_size=cgi.FormContent()['part_size'][0]

commands.getoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} lvcreate --size {2}G --name {3} myvg".format(server_pass,server_ip,part_size,username))


commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mkfs.ext4 /dev/myvg/{2}".format(server_pass,server_ip,username))

commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mkdir -p /share/{2}-lv1".format(server_pass,server_ip,username))

mount_status=commands.getstatusoutput("sshpass -p {0} ssh -o stricthostkeychecking=no -l root {1} mount /dev/myvg/{2} /share/{2}-lv1".format(server_pass,server_ip,username))

if mount_status[0] == 0:
   print "drive mounted successfully !!\n"



a=commands.getstatusoutput("sshpass -p {0} scp root@{1}:/etc/fstab /mnt/".format(server_pass,server_ip))


#if a[0] == 0:
#  print "ok"
#else:
#  print "not ok"

fstab_string="/dev/myvg/{0}  /share/{0}-lv1 ext4 defaults 1  2".format(username)

fstabfh=open('/mnt/fstab','a')
fstabfh.write(fstab_string + "\n")
fstabfh.close()

a=commands.getstatusoutput("sshpass -p {0} scp /mnt/fstab root@{1}:/etc/fstab".format(server_pass,server_ip))
print a

fstab_status=commands.getstatusoutput("mount -a")
if int(fstab_status[0]) == 0:
   print "ok"
else:
   print "some error occur please check fstab manually"


#client_ip=raw_input("enter client ip to which you want to share : ")

client_ip=cgi.FormContent()['client_ip'][0]
commands.getstatusoutput("sshpass -p {0} scp root@{1}:/etc/exports /mnt/".format(server_pass,server_ip))

share_location="/share/{0}-lv1  {1}".format(username,client_ip)

nfsfh=open('/mnt/exports','a')
nfsfh.write(share_location + "\n")
nfsfh.close()

a=commands.getstatusoutput("sshpass -p {0} scp /mnt/exports root@{1}:/etc/exports".format(server_pass,server_ip))
#print a

commands.getoutput("sudo systemctl restart nfs")


   
