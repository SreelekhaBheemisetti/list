# Given 3 digits a, b, and c. The task is to find all the possible combinations from these digits.
# Examples:
# Input: [1, 2, 3]
# Output:
# 1 2 3
# 1 3 2
# 2 1 3
# 2 3 1
# 3 1 2
# 3 2 1

# Input: [0, 9, 5]
# Output:
# 0 9 5
# 0 5 9
# 9 0 5
# 9 5 0
# 5 0 9
# 5 9 0

# a=[1,2,3]
# for i in range(3):
#     for j in range(3):
#         for k in range(3):
#             if i!=j and j!=k and k!=i:
#                 print(a[i],a[j],a[k])

# a=[1,2,3]
# i=0
# while i<len(a):
#     j=0
#     while j<len(a):
#         k=0
#         while k<len(a):
#             if i!=j and j!=k and k!=i:
#                 print(a[i],a[j],a[k])
#             k+=1
#         j+=1
#     i+=1            