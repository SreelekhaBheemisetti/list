# Our task is to print the element which occurs 3 consecutive times in a Python list.
# Example:
# Input: [4, 5, 5, 5, 3, 8]
# Output: 5
# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output: 1, 22


a= [1, 1, 1, 64, 23, 64, 22, 22, 22]
i=0
while i<len(a)-2:
    if a[i]==a[i+1] and a[i+1]==a[i+2]:
        print(a[i])
    i+=1
 