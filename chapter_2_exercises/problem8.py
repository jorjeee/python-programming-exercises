# Exercise No. 8
# Write a program that will compute and display the area and perimeter of a rectangle.
# Formulae: area = length * width and perimeter = 2 (length + width)

print()
print("\t==== RECTANGLE'S AREA & PERIMETER ====")
print()

length = float(input("\tEnter the length : "))
width = float(input("\tEnter the width : "))

area = length * width
perimeter = 2 * (length + width)

print()
print("\tArea : {0:.2f}".format(area))
print("\tPerimeter : {0:.2f}".format(perimeter))
print()
print("\t==== END OF PROGRAM ====")
print()
