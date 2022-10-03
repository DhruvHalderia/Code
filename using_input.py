# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 3.17
# Date:         15 September 2022
#
from math import*
# The code below calculates force
print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
accel = float(input("Please enter the acceleration (m/s^2): "))
force = mass * accel
print(f"Force is {force:.1f} N\n")

#the code below calculates wavelength
print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
wavelength = 2*distance*sin((angle/180)*pi)
print(f"Wavelength is {wavelength:.4f} nm\n")

#the code below calculates Radon-222
print("This program calculates how much Radon-222 is left given time and initial amount")
days = float(input("Please enter the time (days): "))
initialMass = float(input("Please enter the initial amount (g): "))
radLeft = initialMass*(2**(-days/3.8))
print(f"Radon-222 left is {radLeft:.2f} g\n")

#the code below calculates the pressure of an ideal gas
print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): ")) * 1000
temp = float(input("Please enter the temperature (K): "))
pressure = (moles*8.314*temp)/volume
print("Pressure is",int(pressure),"kPa")
#