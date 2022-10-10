# a=[2,3,4]
# o/p:-['22','23','24','32','33','34','42','43','44']

a=[2,3,4]
i=0
b=[]
while i<len(a):
    j=0
    while j<len(a):
        d=str(a[i])+str(a[j])
        b.append(d)
        j+=1
    i+=1
print(b)