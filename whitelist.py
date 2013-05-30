import os
import subprocess


#clear table BELII_SPISOK table
subprocess.Popen('iptables -F BELII_SPISOK', shell=True)

#read list of white sites from file
FILE=open("whitelist.txt", "r")
OneWhiteSite=FILE.readlines()

#congregate rule of iptables
for i in OneWhiteSite:
        i=i.strip() #clear empty characters
        command='iptables -A BELII_SPISOK  -d '+ i + ' -j ACCEPT'
        if i:
                print command
                subprocess.Popen(command, shell=True)
