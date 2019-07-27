#practice of basic python programming

l=[eval(x) for x in input("Enter list Elements").split(',')]
element=eval(input("Enter element value :"))
index=0
while index<len(l) :
	if l[index]==element :
		print(index,end=' ')
	index+=1
