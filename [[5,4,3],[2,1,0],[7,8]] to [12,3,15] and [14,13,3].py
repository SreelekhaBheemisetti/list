# b=[[5,4,3],[2,1,0],[7,8]]
# o/p:-[12,3,15]
# o/p:-[14,13,3]

b=[[5,4,3],[2,1,0],[7,8]]
i=0
a=[]
while i<len(b):
    j=0
    sum=0
    while j<len(b[i]):
        sum=sum+b[i][j]
        j+=1
    i+=1
    a.append(sum)
print(a)

b=[[5,4,3],[2,1,0],[7,8]]
i=0
a=[]
while i<len(b):
    j=0
    sum=0
    while j<len(b[i]):
        sum=sum+b[j][i]
        j+=1
    i+=1
    a.append(sum)
print(a)