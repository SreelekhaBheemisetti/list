# Write a Python program to find the list with maximum and minimum length.
# Original list:
# [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# List with maximum length of lists:
# (3, [13, 15, 17])
# List with minimum length of lists:
# (1, [0])

a=[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
i=0
max=a[0]
min=a[0]
c=0
while i<len(a):
    j=0
    while j<len(a[i]):
        if a[i]<min:
            min=a[i]
        else:
            max=a[i]
        j+=1
    i+=1
print((len(max),max))
print((len(min),min))

