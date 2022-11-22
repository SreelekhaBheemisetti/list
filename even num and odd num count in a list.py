# how many odd numbers and how many even numbers are there in a given list.


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even_c=0
odd_c=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        even_c+=1
    else:
        odd_c+=1
    i+=1
print("even numbers:",even_c)
print("odd numbers:",odd_c)