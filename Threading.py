from time import sleep
from threading import *

class Hello(Thread):
	def run(self):
		for i in range(1,500):
			print("Hello")
			sleep(1)

class Hi(Thread):
	def run (self):
		for i in range(1,500):
			print("Hi")
			sleep(1)

t1=Hello()
t2=Hi()

t1.start()
sleep(0.2)
t2.start()



			







