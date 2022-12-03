# How to find all pairs in an array of integers whose sum is equal to the given number?
# a = [10, 11, 12, 13, 14, 17, 18, 19]
# Take sum as input from user number = 30
# o/p:-[[11,19], [12,18],[13,17]]



a= [10, 11, 12, 13, 14, 17, 18, 19]
b=[]
n=30
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]+a[j]==n:
            d=[a[i],a[j]]
            b.append(d)
        j+=1
    i+=1
print(b)

