#practice of basic python programming
n=int(input("enter any no :"))
if n<2 :
	print("Not a prime no")
else :
	for i in range(2,n) :
		if n%i==0 :
			print("Not a prime no")
			break
	else :
		print("No is prime")