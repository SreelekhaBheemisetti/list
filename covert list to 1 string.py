# Convert Character Matrix to single String;
#     The original list is: [ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
# The String after join: gfgisbest
a=[ ['g', 'f', 'g'], ['i', 's'], ['b', 'e', 's', 't'] ]
i=0
b=""
while i<len(a):
    j=0
    while j<len(a[i]):
        b=b+a[i][j]
        j+=1
    i+=1
print(b)