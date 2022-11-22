a=["hello", "take"]
b=["dear", "sir"]
d=[]
i=0
while i<len(a):
    j=0
    while j<len(b):
        c=a[i]+b[j]
        d.append(c)
        j+=1
    i+=1
print(d)