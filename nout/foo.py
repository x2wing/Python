#import sys
#import max
#L=[]
#sys.path.insert(0,"/etc")
#print(sys.path)
#print ((15300+7000)*0.87)

print 234271*4*1000/1024/1024

#sudo iptables -I PREROUTING -i ppp0 -p tcp -m udp --dport 33389 -j DNAT --to-destination 192.168.0.220:3389

#sudo iptables -I POSTROUTING -d 192.168.0.220/32 -o ppp0 -p tcp -m tcp --dport 3389 -j SNAT --to-source 192.168.0.226 -t nat