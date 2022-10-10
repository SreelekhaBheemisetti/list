# Write a code that prints the maximum in this list.
# numbers = [50, 40, 23, 70, 56, 12, 5, 10, 7]
a=[50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
max=a[0]
while i<len(a):
    if a[i]>max:
        max=a[i]
    i+=1
print(max)


# a=[50, 40, 23, 70, 56, 12, 5, 10, 7]
# max=a[0]
# for i in a:
#     if i>max:
#         max=i
# print(max)