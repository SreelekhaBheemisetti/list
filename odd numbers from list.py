# Write a program to print only odd numbers from the given list using  a while loop .
a= [23, 45, 32, 25, 46, 33, 71, 90]
i=0
b=[]
while i<len(a):
    if a[i]%2!=0:
        b.append(a[i])
    i+=1
print(b)