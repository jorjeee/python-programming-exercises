# Exercise No. 1
# Write a program to convert the US Dollar ($)
# into Philippine Peso. Assume that on US Dollar
# is equivalent to Php 50.74. Then, display the
# result on the screen

#\u20B1 - Philippine Peso Symbol
#\u0024 - US Dollar Symbol

print()
print("\t==== USD to PHP CONVERTER ====")
print()

dollar = float(input("\tEnter the USD Amount : "))

dollar_to_peso = dollar * 50.74

print()
print("\t\u0024 {0:.2f} >>>>>>>>>> \u20B1 {1:.2f}".format(dollar, dollar_to_peso))
print()

print("\t==== END OF PROGRAM ====")
print()


