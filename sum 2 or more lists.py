# Write a Python program to sum two or more lists, the lengths of the lists may be different. 
# Original list:
# [[1, 2, 4], [2, 4, 4], [1, 2]]
# Sum said lists with different lengths:
# [4, 8, 8]
# Original list:
# [[1], [2, 4, 4], [1, 2], [4]]
# Sum said lists with different lengths:
# [8, 6, 4]


a=[[1, 2, 4], [2, 4, 4], [1, 2]]
b=[]
i=0
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[j][i]
        j+=1
    b.append(sum)
    i+=1
print(b)





# a=[[1,"",""], 
#     [2, 4, 4], 
#     [1, 2,""], 
#     [4,"",""]]
# b=[]
# i=0
# while i<3:
#     j=0
#     sum=0
#     while j<len(a):
#         f=a[j][i]
#         if type(f)==int:
#             sum=sum+f
#         j=j+1
#     b.append(sum)
#     i=i+1
# print(b)
