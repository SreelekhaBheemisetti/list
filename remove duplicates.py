# Remove duplicates from a list.
# List = [1,2,3,1,2,2]
# Output: [1,2,3]

a=[1,2,3,1,2,2]
b=[]
i=0
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i+=1
print(b)
