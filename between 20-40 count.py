# Write a code, that counts the numbers between 20 and 40 and then print its count.
# list1 = [50, 40, 23, 70, 56, 12, 5, 10, 7]
list1 = [50, 40, 23, 70, 56, 12, 5, 10, 7]
i=0
c=0
while i<len(list1):
    num=list1[i]
    if num>=20 and num<=40:
        c+=1
    i+=1
print(c)

