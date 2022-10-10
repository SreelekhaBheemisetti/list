# a list of marks and we have to find that how many students have marks less than 50.

student_marks = [23, 45, 67, 89, 90, 54, 34, 21, 34, 23, 19, 28, 10, 45, 86, 87, 9]
i=0
less_marks=0
more_marks=0
while i<len(student_marks):
    marks=student_marks[i]
    if marks<50:
        less_marks+=1
    else:
        more_marks+=1
    i = i + 1
print("Marks more than 50: " + str(more_marks))
print("Marks less than 50: " + str(less_marks))
