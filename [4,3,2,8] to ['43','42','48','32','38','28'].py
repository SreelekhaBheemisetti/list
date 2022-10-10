# a=[4,3,2,8]
# o/p:-['43','42','48','32','38','28']

a=[4,3,2,8]
b=[]
i=0
while i<len(a)-1:
    j=1
    while j<=len(a)-1:
        c=str(a[i])+str(a[j])
        b.append(c)
        j+=1
    i+=1
print(b)
