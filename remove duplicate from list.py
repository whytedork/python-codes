#practice of basic python programming
names=[]
n=int(input("how many names ?"))
for i in range(n) :
	print(i+1,"Enter name")
	names.append(input())
s=set(names)
names=list(s)
for x in names :
	print(x)
