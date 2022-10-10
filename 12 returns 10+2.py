# You will be given a number and you need to return it as a string in Expanded Form. For example:
# 12  # Should return '10 + 2'
# 42 # Should return '40 + 2'
# 70304  # Should return '70000 + 300 + 4'
n=42
i=0
j="0"
while i<len(str(n)):
    r=n%10
    d=n//10
    v=str(d)+j
    i+=1
print(v,"+",r)