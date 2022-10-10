# a=(1,2),(3,4),(5,6)
# o/p:-[1,2,3,4,5,6]


a=((1,2),(3,4),(5,6))
i=0
d=[]
while i<len(a):
    j=0
    while j<len(a[i]):
        d.append(a[i][j])
        j+=1
    i+=1
print(d)
        