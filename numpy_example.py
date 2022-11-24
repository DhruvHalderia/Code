# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   12.14
# Date:         111/23/2022
# As a team, we have gone through all required sections of the  
# tutorial, and each team member understands the material 
import numpy as np
#we made all the matrices in the code below
a = np.arange(12).reshape(3,4)
print(f'A = {a}')
print()
b = np.arange(8).reshape(4,2)
print(f'B = {b}')
print()
c = np.arange(6).reshape(2,3)
print(f'C = {c}')
print()
d = a@b@c
print(f'D = {d}')
print()
print(f'D^T = {d.T}')
print()
e = np.sqrt(d)/2
print(f'E = {e}')