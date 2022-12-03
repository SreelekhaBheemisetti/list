# a="level"
# i=0
# while i<len(a):
#     c=0
#     j=0
#     while j<len(a):
#         if a[i]==a[j]:
#             c+=1
#         if i==2:
#             break
#         j+=1
#     print(a[i],c)
#     i+=1
    

    
n=int(input("enter the num:"))
c=0
i=1
while i<=n:
    a=n%10
    n=n//10
    b=n+a
    if b%i==0:
        c+=1
    i+=1
if c==2:
    print("prime num")
else:
    print("not prime num")
    
    
