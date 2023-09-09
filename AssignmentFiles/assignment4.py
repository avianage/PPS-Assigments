
# To accept student’s five courses marks and compute his/her result. Student is passing if
# he/she scores marks equal to and above 40 in each course. If student scores aggregate
# greater than 75%, then the grade is distinction. If aggregate is 60>= and <75 then the
# grade if first division. If aggregate is 50>= and <60, then the grade is second division. If
# aggregate is 40>= and <50, then the grade is third division. 

marks= []
fail = False
print("\n")

for i in range(5):
    mark = 0
    mark = int (input("Enter Mark for Course " + str(i+1) +" : "))

    marks.append(mark)
    if (mark < 40):
        fail = True

total_marks = sum(marks) / 5
grade = ""

if fail:
    print ("Student Failed")
    grade='Fail'
else:    
    
    if total_marks >=90:
        grade='Distinction'
    elif total_marks >80:
        grade ='First Division'
    elif total_marks>70:
        grade ="Second Division"
    else:
        grade ="Third Division"

print ('Total Marks: ',total_marks,'Grade: ',grade )

print("\n")
        


