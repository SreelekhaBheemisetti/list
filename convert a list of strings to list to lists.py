# Write a Python program to convert a given list of strings into list of lists. 
# Original list of strings:
# ['Red', 'Maroon', 'Yellow', 'Olive']
# Convert the said list of strings into list of lists:
# [['R', 'e', 'd'], ['M', 'a', 'r', 'o', 'o', 'n'], ['Y', 'e', 'l', 'l', 'o', 'w'], ['O', 'l', 'i', 'v', 'e']]
a=['Red', 'Maroon', 'Yellow', 'Olive']
c=""
i=0
d=[]
while i<len(a):
    j=0
    b=[]
    while j<len(a[i]):
        c=a[i][j]
        b.append(c)
        j+=1
    d.append(b)
    i+=1
print(d)