# Write a Python program to check if first digit/character of each element in a given list is same or not.
# Original list:
# [1234, 122, 1984, 19372, 100]
# Check if first digit in each element of the said given list is same or not!
# True
# Original list:
# [1234, 922, 1984, 19372, 100]
# Check if the first digit in each element of the given list is the same or not!
# False
# Original list:
# ['aabc', 'abc', 'ab', 'a']
# Check if first character in each element of the said given list is same or not!
# True
# Original list:
# ['aabc', 'abc', 'ab', 'ha']
# Check if first character in each element of the said given list is same or not!
# False


a=[1234, 122, 1984, 19372, 100]
i=0
result=True
c=str(a[0])
while i<len(a):
    b=str(a[i])
    if b[0]!=c[0]:
        result=False
        break
    i=i+1
print(result)
    

 
      

