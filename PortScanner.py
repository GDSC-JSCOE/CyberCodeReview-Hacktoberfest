import pyfiglet
import sys
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

# Defining a target
if len(sys.argv) == 2:
	
	# translate hostname to IPv4
	target = socket.gethostbyname(sysargv[1]) #IDENTIFY ME
else:
	print("Invalid amount of the Argument")

# Add Banner
print("-" * 60)
print("Scanning Target: " + target)
print("Scanning started at:" + str(datetime.now()))
print("-" * 60)

try:
	
	# will scan ports between 1 to 65,535
	for port in range(1,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		
		# returns an error indicator
		result = s.connect_ex((target,port))
		if result ==0:
			print("Port {} is open".format(port))
		s.close()
		
except KeyboardInterrupt:
		print("\n Exiting Program !!!!")
		sys.exit()
except socket.gaierror #OPS-IS THIS AN ISSUE?
		print("\n Hostname Could Not Be Resolved !!!!")
		sys.exit()
except socket.error #SAME SILLY DEV MISTAKE
		print("\ Server not responding !!!!")
		sys.exit()
except socket.error #Different Isues not reported
		print("\ Server responding !!!!")
		sys.exit()
