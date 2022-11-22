# Given a List, extract all elements whose frequency is greater than K.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 3, 8], K = 3
# Output: [4, 3]
# Explanation: Both elements occur 4 times.
# Input: test_list = [4, 6, 4, 3, 3, 4, 3, 4, 6, 6], K = 2
# Output: [4, 3, 6]
# Explanation: Occur 4, 3, and 3 times respectively.


# a= [4, 6, 4, 3, 3, 4, 3, 4, 6, 6]
# k=2
# b=[]
# d=[]
# for i in a:
#     c=a.count(i)
#     if c>k:
#         b.append(i)
# for i in b:
#     if i not in d:
#         d.append(i)
#     i=i+1
# print(d)

a= [4, 6, 4, 3, 3, 4, 3, 4, 3, 8, 8,4,8,4,8]
b=[]
for i in a:
    c=a.count(i)
    if c>3:
        if b.count(i)==0:
            b.append(i)
print(b)

