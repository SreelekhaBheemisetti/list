# Write a code that works for any list, 
# it should give two sums as outputs, 
# one is the sum of odd numbers present in the list and the other is the sum of even numbers present in the list.


elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even_sum=0
odd_sum=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        even_sum=even_sum+elements[i]
    else:
        odd_sum=odd_sum+elements[i]
    i+=1
print("even sum:", even_sum)
print("odd sum", odd_sum)


