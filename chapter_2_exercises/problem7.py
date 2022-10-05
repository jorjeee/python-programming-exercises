# Exercise No. 7
# Write a program, which computes and outputs
# on the screen the time required to travel
# 5400 miles at a speed of 220 mph.

print()
print("\t==== TIME SOLVER ====")
print()

miles = float(input("\tEnter the number of miles : "))
speed = float(input("\tEnter the travelling speed : "))

miles_per_hour = 220

hour = int(miles / miles_per_hour)

# SKIPPED THE MINUTES SECONDS problem 05/09/2022
# remaining_miles = miles % miles_per_hour
# remaining_miles = remaining_miles / miles_per_hour
# remaining_hour = remaining_miles * 60
#
# minutes = remaining_hour / 60
# remaining_minutes = remaining_hour % 60
#
# seconds = remaining_minutes / 60
# remaining_seconds = remaining_minutes % 60
# TRY FLOOR DIVISION AND MODULO

print()
print("\tTime required to travel {0} miles at a speed of "
      "{1} mph is {2} hour(s)".format(miles, speed, hour))
print()
print("\t==== END OF PROGRAM ====")
print()
