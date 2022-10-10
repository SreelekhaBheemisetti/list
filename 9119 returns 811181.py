# squaring the given user through the loop
n=int(input("enter the number:"))
a=""
while n>0:
    b=n%10
    a=a+str(b**2)
    n=n//10
print(a)