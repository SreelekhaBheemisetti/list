# print length of 2 lists
# print student name and how many marks he got

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# i=0
# print(len(students))
# print(len(marks))

# students = ['Rishabh', 'Madhurima', 'Rahul', 'Abhishek', 'Faizal', 'Muskaan']
# marks = [10, 20, 56, 45, 36, 20]
# i=0
# while i<len(students):
#     print(students[i]+str(marks[i]))
#     i+=1

     
a=[2,4,1,7,5,9]
b=[]
c=[]
min=a[0]
i=0
while i<len(a):
    if a[i]<min:
        min=a[i]
        b.append(min)
    i+=1
j=-1
while j>=-len(b):
    c.append(b[j])
    j-=1
    print(c)



