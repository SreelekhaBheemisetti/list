# Write a Python program to find the dimension of a given matrix.
# Original list:
# [[1, 2], [2, 4]]
# Dimension of the said matrix:
# (2, 2)
# Original list:
# [[0, 1, 2], [2, 4, 5]]
# Dimension of the said matrix:
# (2, 3)
# Original list:
# [[0, 1, 2], [2, 4, 5], [2, 3, 4]]
# Dimension of the said matrix:
# (3, 3)
a=[[0, 1, 2], [2, 4, 5], [2, 3, 4]]
i=0
while i<len(a):
    j=0
    while j<len(a[i]):
        c=(len(a),len(a[i]))
        j+=1
    i+=1
print(c)
