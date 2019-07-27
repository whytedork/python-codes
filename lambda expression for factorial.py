#practice of basic python programming

f=lambda n : n*f(n-1) if n>0 else 1
n=int(input("Enter no "))
print(f(n))