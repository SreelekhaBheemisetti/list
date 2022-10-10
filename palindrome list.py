# palindrome list

a=["m","o","m"]
i=-1
b=""
d=[]
while i>=-len(a):
    j=i
    while j>=i:
        b=a[i]
        j-=1
    d.append(b)
    i-=1
if d==a:
    print("palindrome")
else:
    print("not a palindrome")
