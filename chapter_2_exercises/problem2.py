# Exercise No. 2
# Write a program to calculate the
# volume of a sphere. Then, display
# the result. Use the following
# formula: V = 4/3 PI r^3.

import math

print()
print("\t==== SPHERE CALCULATOR ====")
print()

radius = float(input("\tEnter the radius : "))

volume_sphere = (4 / 3) * math.pi * (radius ** 3)

print()
print("\tVolume of the sphere : {0:.2f}".format(volume_sphere))
print()

print("\t==== END OF PROGRAM ====")
print()
