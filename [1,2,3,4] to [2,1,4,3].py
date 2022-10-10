# a=[1,2,3,4]
# o/p:-[2,1,4,3]

a=[1,2,3,4]
i=0
d=[]
while i<len(a):
    if i%2==0:
        b=a[i+1]
        d.append(b)
    else:
        c=a[i-1]
        d.append(c)
    i+=1
print(d)

# a=[1,2,3,4]
# i=0
# # d=list()
# while i<len(a):
#     if i%2==0:
#         b=a[i+1]
#         d.append(b)
#     else:
#         c=a[i-1]
#         d.append(c)
#     i+=1
# print(d)


