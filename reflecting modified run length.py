# Write a Python program to create a list reflecting the modified run-length encoding from 
# a given list of integers or a given list of characters. 
# Original list:
# [1, 1, 2, 3, 4, 4, 5, 1]
# List reflecting the modified run-length encoding from the said list:
# [[2, 1], 2, 3, [2, 4], 5, 1]
# Original String:
# aabcddddadnss
# List reflecting the modified run-length encoding from the said string:
# [[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]

a=[1, 1, 2, 3, 4, 4, 5, 1]
b=[]
i=0
while i<len(a)-1:
    count=1
    if a[i]== a[i+1]:
        count+=1
        d=[count,a[i]]
        b.append(d)
        i+=1
    else:
        b.append(a[i])
    i+=1    
b.append(a[-1])
print(b)