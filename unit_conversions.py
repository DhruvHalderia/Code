# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   Team Lab 3
# Date:         07 09 2022
#
#
UserInput = float(input("Please enter the quantity to be converted: "))
#Conversions
NewtonConversion = 4.448222
FeetConversion = 3.2808399
KilopascalsConversion = 101.325
BTUPerHourConversion = 3.412141633
USGallonsPerMinuteConversion = 15.8503231
DFahrenheitConversion = 1.8
#print statements
print(f"{UserInput:.2f} pounds force is equivalent to {UserInput*NewtonConversion:.2f} Newtons")
print(f"{UserInput:.2f} meters is equivalent to {UserInput*FeetConversion:.2f} feet")
print(f"{UserInput:.2f} atmospheres is equivalent to {UserInput*KilopascalsConversion:.2f} kilopascals")
print(f"{UserInput:.2f} watts is equivalent to {UserInput*BTUPerHourConversion:.2f} BTU per hour")
print(f"{UserInput:.2f} liters per second is equivalent to {UserInput*USGallonsPerMinuteConversion:.2f} US gallons per minute")
print(f"{UserInput:.2f} degrees Celsius is equivalent to {UserInput*DFahrenheitConversion+32:.2f} degrees Fahrenheit")
