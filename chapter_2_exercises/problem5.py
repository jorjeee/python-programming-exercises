# Exercise No. 5
# Write a program that computes the grade
# of the student based on the three grading
# terms. Prelim is 20%, Midterm is 30%, and
# Endterm is 50%

print()
print("\t==== STUDENT'S GRADE SOLVER ====")
print()

student_full_name = input("\tEnter student's name : ")
prelim = float(input("\tEnter Prelim Grade : "))
midterm = float(input("\tEnter Midterm Grade : "))
endterm = float(input("\tEnter Endterm Grade : "))

final_grade = (prelim * .20) + (midterm * .30) + (endterm * .50)

print()
print("\tStudent Information: ")
print("\tName : {0}".format(student_full_name.upper()))
print("\tFinal Grade : {0}".format(final_grade))
print()
print("\t==== END OF PROGRAM ====")
print()
