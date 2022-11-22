a=['S',['R'],['E'],['E']]
e=[]
i=1
c=""
while i<len(a):
    j=0
    while j<len(a[i]):
            b=a[i][j].lower()
            c=c+b
            j+=1
    i=i+1
d=(a[0][0]+c)
e.append(d)
print(e)