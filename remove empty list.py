# Remove empty List from List		
# The original list is: [5, 6, [], 3, [], [], 9]
# List after empty list removal: [5, 6, 3, 9]

n=[]
a=[5, 6, [], 3, [], [], 9]
b=[]
i=0
while i<len(a):
    if n!=a[i]:
        b.append(a[i])
    i+=1
print(b)