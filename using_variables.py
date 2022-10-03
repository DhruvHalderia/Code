# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 2.9
# Date:         2 September 2022
#
#
from math import*
# In the code following I am calculating the assigned variables with the information given
# I am also assigning variables for the individual numbers
mass = 3
acceleration = 5.5
print("Force is",mass*acceleration, "N")
DegreeToRad = 25/180 * pi
crystal_lattice = .025
print("Wavelength is",2*crystal_lattice*sin(DegreeToRad),"nm")
half_life = 3.8
days = 3
mass = 5
print("Radon-222 left is", mass*2**(-days/half_life),"g" )
moles = 5
volume = 250
kTemp = 415
gas_constant = 8.314
print("Pressure is",(moles*gas_constant*kTemp)/volume, "kPa")
#
#