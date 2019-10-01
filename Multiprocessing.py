from multiprocessing import *
from time import *

def square(numbers):
	for i in numbers:
                sleep(5)
		print("Square :"+str(i*i))

def cube(numbers):
	for i in numbers:
                sleep(5)
		print("Cube :"+str(i*i))
if __name__=="__main__" :
	arr=[1,2,3,4,5]
	p1=Process(target=square,args=(arr,))
	p2=Process(target=cube,args=(arr,))

p1.start()
p2.start()

p1.join()
p2.join()
