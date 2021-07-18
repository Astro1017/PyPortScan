#!/bin/python3
import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translating a hostname to IPv4
else: 
	print("invalid amount of arguments.") 
	print("Syntax: python3 scanner.py <ip>")
	 
#add a pretty banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)

try: 
	for port in range(50,85): #loop from 50-85
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #defining s = IPv4 + Port
		socket.setdefaulttimeout(1) #default timeout 1 second
		result = s.connect_ex((target,port)) #Returns an error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close() #closes the connection
		
except KeyboardInterrupt: #CTRL + C exits the program cleanly
	print("\nExiting program.")
	sys.exit()
	
except socket.gaierror: #If there's no DNS resolution, exit the program
	print("Host name could not be resolved.")
	
except socket.error: #IF we can't connect to specified IP, exit the program
	print("Couldn't connect to server.") 
	sys.exit()
