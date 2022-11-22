# o/p:-[[a,d,g,j,m],[b,e,h,k],[c,f,i,l]]
a=['a','b','c','d','e','f','g','h','i','j','k','l','m']
i=0
c=[]
while i<3:
    j=i
    b=[]
    while j<len(a):
        b.append(a[j])
        j+=3
    i+=1
    c.append(b)
print(c)
