
student_1 = [40, 35, 70, 90, 56]

student_2 = [57, 90, 80, 98, 46]

students = {
    "student_1": student_1,
    "student_2": student_2
}

for key in students:
    flag = False
    for value in students[key]:
        if value < 40:
            flag = True
            break

    if flag == False:
        summationOfMarks = sum(students[key])
        lengthOfArr = len(students[key])
        print(summationOfMarks/lengthOfArr)
    else:
      print("FAILED")    
