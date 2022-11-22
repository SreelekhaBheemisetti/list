elements = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
even_sum=0
even_c=0
odd_sum=0
odd_c=0
i=0
while i<len(elements):
    if elements[i]%2==0:
        even_sum=even_sum+elements[i]
        even_c+=1
    else:
        odd_sum=odd_sum+elements[i]
        odd_c+=1
    i+=1
print("even avg:", even_sum/even_c)
print("odd avg", odd_sum/odd_c)