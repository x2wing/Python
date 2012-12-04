from /usr/lib/python2.7/dist-packages/fabric/api import *
env.hosts = ['magistr@localhost:22']
def backup():
    run("ls>1.txt")