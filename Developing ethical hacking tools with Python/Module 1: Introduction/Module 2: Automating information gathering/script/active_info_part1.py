import nmap
import sys

#Instantiate a scanner
nm_scan = nmap.PortScanner()

#Run scan with additional parameters, scan targets, result in a dictionary
# sys.argv need to be replaced by targeted IP
nmap_scanner = nm_scan.scan(sys.argv[1],'80', arguments='-D')

#Needed from dictionary: state of the host, state of ports,scanning method,operation system it guesses

#Check scan, check state of the host, look at the status and check the state and if host is up
print("The host is:"+nm_scammer['scan'][IP_ADDRESS]['status']['state]'

# State of the port
print("The port 80 is:"+nm_scammer['scan'][IP_ADDRESS]['tcp']['80']['state']

# Scanning method
print("The scanning method is is:"+nm_scammer['scan'][IP_ADDRESS]['tcp']['80']['reason']

# OS match and the name of the operating system
print("There is %s percent chance that the host is running %s"%(nm_scanner['scanner'][IP_ADDRESS]['osmatch'][0]['accuracy'],nm_scannner['scan'][IP_ADDRESS]['osmatch'][0]['name']))
