import nmap
import sys

#Get IP address
ping [TARGET]
#E.G
ping google.com

#Instantiate a scanner
nm_scan = nmap.PortScanner()

print('\nRunning...\n')

#Dictionary
nm_scanner = nm_scan.scan(sys.argv[1],'80',arguments='-0'

#Variables
host_is_up = "The host is: "nm_scanner['scan'][IP_ADDRESS]['status']['state]+".\n"
port_open ="The port is: "nm_scanner['scan'][IP_ADDRESS]['tcp']['80']['state']+".\n"
method_scan="The method of scanning is: "nm_scanner['scan'][IP_ADDRESS]['tcp']['reason']+".\n"
guessed_os="There is a %s percent chance that the host is running%s: "nm_scanner['scan'][IP_ADDRESS]['osmatch']['accuracy'],nm_scanner['scan'][IP_ADDRESS]['osmatch'][0]['name'])+".\n"

#Automate
with open("%s.txt"%IP_ADDRESS, 'w') as f:
	f.write(host_is_up=port_open+method_scan=guessed_os)
	f.write("\nReport generated"+time.strftime("%Y-%m-%d_%H:%M:%S GMT", 			
	time.gntime()))
print("\nFinished ...."

#Run script
python active_info_part2.py py [IP_ADDRESS]
