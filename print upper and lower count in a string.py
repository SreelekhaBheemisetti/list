a="PytHoN LANguage"
upper=0
lower=0
i=0
while i<len(a):
    if a[i].isupper():
        upper+=1
    else:
        lower+=1
    i+=1
print("upper:",upper)
print("lower:",lower)
