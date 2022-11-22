#  Write a Python program to iterate a given list cyclically on specific index position. 
# Original list:
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# Iterate the said list cyclically on specific index position 3 :
# ['d', 'e', 'f', 'g', 'h', 'a', 'b', 'c']
# Iterate the said list cyclically on specific index position 5 :
# ['f', 'g', 'h', 'a', 'b', 'c', 'd', 'e']


a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
n=int(input("enter the num:"))
b=[]
e=[]
i=0
while i<len(a):
    if i>=n:
        b.append(a[i])
    else:
        e.append(a[i])
    i+=1
f=b+e
print(f)