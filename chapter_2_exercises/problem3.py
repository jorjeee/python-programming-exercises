# Exercise No. 3
# Write a program to compute the gross pay of
# a worker named Allie Pomperada given that
# Allie Pomperada worked for 40 hours at the
# rate of P84.50 per hour.

print()
print("\t===== GROSS PAY CALCULATOR ====")
print()

employee_full_name = input("\tEnter employee's name : ")
hours_worked = int(input("\tEnter hours of work : "))
rate_per_hour = float(input("\tEnter rate per hour : "))

gross_pay = hours_worked * rate_per_hour

print()
print("\tEmployee's Name : {0}".format(employee_full_name.upper()))
print("\tGross Salary : \u20B1 {0:.2f}".format(gross_pay))
print()
print("\t==== END OF PROGRAM ====")
print()
