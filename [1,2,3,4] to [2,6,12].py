# a=[1,2,3,4]
# o/p:-[2,6,12]
# and also find the max from the output
a=[1,2,3,4]
i=0
b=[]
while i<len(a)-1:
    if a[i]*a[i+1]:
        b.append(a[i]*a[i+1])
    i+=1
print(b)
j=0
c=0
while j<len(b):
    if c>b[j]:
        b[j]=c
    j+=1
print(b[j])
