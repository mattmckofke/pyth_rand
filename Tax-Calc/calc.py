# This will help users calculate their tax based on their income and the tax bracket they fall into
# ALL BASED ON USD
# UPDATED FOR 2025 TAX BRACKETS

import sys

income = float(input("Enter your income: "))
status = input("Enter your status (single, married): ")
brackets = [[0.1, 11925], [0.12, 48475], [0.22, 103350], [0.24, 197300], [0.32, 250525], [0.35, 250526], [0.37, sys.maxsize*2+1]]
if status == "married": brackets = [[0.1, 0], [0.12, 23851], [0.22, 96951], [0.24, 206701], [0.32, 394601], [0.35, 501051], [0.37, 751601]]

# now calculate the tax paid on the income
# how tax works is you pay a certain percentage of income that falls within a certain bracket
# for example, if you make 100k, you pay 10% on the first 11925, 12% on the next 48475, and so on until you have paid up to the 100k

tax = 0
temp = income
for bracket in brackets:
    if income > bracket[1]:
        tax += bracket[1] * bracket[0]
        temp -= bracket[1]
    else:
        tax += temp * bracket[0]
        break
        
print("You will pay $" + f"{tax:.2f}" + " in taxes.")