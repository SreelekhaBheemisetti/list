
# Count unique values inside a list.
# input_list = [1, 2, 2, 5, 8, 4, 4, 8]
# Count = 5 #because [1,2,5,8,4] are unique values.
a=[1, 2, 2, 5, 8, 4, 4, 8]
b=[]
c=0
for i in a:
    if i not in b:
        b.append(i)
i=0
c=0
while i<len(b):
    c=c+1
    i+=1
print("count:", c)