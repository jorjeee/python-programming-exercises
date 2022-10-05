# Exercise No. 10
# Jacob Samuel deposited his money in time deposit
# at a bank in the amount of Php 25000. The bank gave
# him 12% for a term of 30 days. There is a 10%
# withholding tax to be deducted from the interest.
#
# (A.) Find his withholding tax.
# (B.) Find the net interest he will receive.
# Use the formula:
#       I = PRT;
#           where I - interest,
#           P - principal value,
#           R - rate of interest, and
#           T - time.

# I = 25 000 * 12/100 * 30/365

print()
print("\t==== SIMPLE INTEREST CALCULATOR ====")
print()

client_full_name = input("\tEnter client's full name : ")
deposited_amount = float(input("\tEnter amount to be deposited : "))
rate = float(input("\tEnter the rate of interest : "))
time = int(input("\tEnter the time (in Days): "))

net_interest = deposited_amount * (rate/100) * (time/365)
withholding_tax = net_interest * (10/100)

print()
print("\tClient's Information: ")
print("\tName : {0}".format(client_full_name.upper()))
print("\tDeposited Amount : \u20B1 {0:.2f}".format(deposited_amount))
print("\tRate per year : {0:.2f}%".format(rate))
print("\tWithholding Tax Rate : 10%")
print("\tTime (in years) : {0:.2f}".format(time/365))
print("\t====================")
print("\tNet Interest : \u20B1 {0:.2f}".format(net_interest))
print("\tTax Deduction : \u20B1 {0:.2f}".format(withholding_tax))
print()
print("\tTotal Net Interest : \u20B1 {0:.2f}".format(net_interest - withholding_tax))
print()
print("\t==== END OF PROGRAM ====")
print()

