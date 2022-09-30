import whois
import csv
import sys

#Usages
if len(sys.argv)!= 3:
	print ("usages:")
	print ("python whosisip.py -i <single-ip>")
	print ("python whosisip.py -l <list-of-ip>")
	sys.exit(1)

outfile = csv.writer(open("output.csv", "w"))
outfile.writerow(['IP', 'Registrar', 'Email', 'Name', 'Country', 'City'])

i = 0

#Single IP
if (sys.argv[1] == '-i'):
	ip = sys.argv[2]
	w = whois.whois(ip)
	print (w)

#Multiple IP
elif (sys.argv[1] == '-l'):
	fp = sys.argv[2]
	ip_list = open(fp, "r")
	for ip in ip_list:
		ip = ip.strip('\n') #Removing any new line character from the end of line
		ip = ip.strip('\r')
		w = whois.whois(ip)
#getting the variables to write on csv		 
		registrar, name, country, city, email = w.name, w.country, w.city, w.emails, w.registrar
		outfile.writerow([ip, registrar, email, name, country, city]) 
		i+=1
		print (i)

print ('Done')
