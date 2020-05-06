# Module 3
#   Programming Assignment 4
#     Prob-2.py

# <Garrett>

'''
#Inputs: Asks user for name, hourly wage, and hours
#Process: Calculates tax, insurance, and overtime wages, if applicable, along with total take-home paycheck.
#Outputs: Completed paycheck
'''

def main():
    employeeName = input("\nEnter Name: ")
    print()
    hourlyWages = int(input("Input Hourly Wages: "))
    print()
    workHours = int(input("Input Weekly Hours: "))
    print()

    if workHours > 40:
        overtimeWages = (workHours - 40) * (hourlyWages * 1.5)
    else: overtimeWages = 0
    normalWages = (hourlyWages * workHours) #Should print like ("$", normalWages), etc
    taxWithholding = normalWages / 5
    insuranceWithholding = normalWages / 10
    totalWages = overtimeWages + normalWages
    totalPay = totalWages - (taxWithholding + insuranceWithholding)

    print("Name:", employeeName)
    print("Regular Wages:", normalWages)
    print("Overtime Wages:", overtimeWages)
    print("Total Wages:", totalWages)
    print("Tax Withholding:", taxWithholding)
    print("Insurance Withholding:", insuranceWithholding)
    print("Total Pay:", totalPay)
    

main()