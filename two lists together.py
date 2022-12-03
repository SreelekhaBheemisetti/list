# print length of 2 lists
# print student name and how many marks he got

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# i=0
# print(len(students))
# print(len(marks))

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# i=0
# while i<len(students):
#     print(students[i]+str(marks[i]))
#     i+=1


# a=[65,98,54,23,87,57]
# max1=0
# max2=0
# max3=0
# i=0
# while i<len(a):
#     if a[i]>max1:
#         max1=a[i]
#     i+=1
# j=0
# while j<len(a):
#     if a[j]>max2 and a[j]!=max1:
#         max2=a[j]
#     j+=1
# k=0
# while k<len(a):
#     if a[k]>max3 and a[k]!=max2 and a[k]!=max1:
#         max3=a[k]
#     k+=1
# print(max1)
# print(max2)
# print(max3)


# a=[21,43,32,54,23,65]
# max1=0
# max2=0
# max3=0
# for i in a:
#     if i>max1:
#         max1=i
#     for j in a:
#         if j>max2 and max2!=max1:
#             max2=j
# print(max1)
# print(max2)

# a=[24,53,25,44,77]
# a=[65,98,54,23,87,57]
# i=0
# max1=a[0]
# max2=a[0]
# max3=a[0]
# while i<len(a):
#     if a[i]>max1:
#         max1=a[i]
#     elif a[i]>max2 and max1!=max2:
#         max2=a[i]
#     elif a[i]>max3 and max1!=max3 and max2!=max3:
#         max3=a[i]
#     i+=1
# print(max1)
# print(max2)
# print(max3)

# a=[65,98,54,23,87,57]
# a=[24,53,25,44,77]
# max1=a[0]
# max2=a[0]
# max3=a[0]
# for i in range(1,5):
#     if a[i]>max1:
#         max1=a[i]
#     elif a[i]>max2 and max1!=max2:
#         max2=a[i]
#     elif a[i]>max3 and max1!=max3 and max2!=max3:
#         max3=a[i]
# print(max1)
# print(max2)
# print(max3)

# def add(a,b):
#     sum=a+b
#     return sum
# # a=int(input("enter the num:"))
# # b=int(input("enter the num2:"))
# res=add(5,8)
# print("total=",res)

def greet(name):
    print("Hello, "". Good morning!")
