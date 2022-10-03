# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   6.12
# Date:         09/28/2022
import math
#This gets the side values for the triangles
h = float(input("Enter the side length in meters: "))

#This gets the amount of layers to go through in the problem
layers = int(float(input("Enter the number of layers: ")))
#This gets the bottom and top triangle and then add them all together to get the answer
bottomTriangle = (layers * h) * h *3
topTriangle = h*h * 3
totalSurfaceArea = (topTriangle + bottomTriangle)/2 * layers 
bottomFace = ((layers * h)**2)*(math.sqrt(3)/4)
totalSurfaceArea += bottomFace
print(f"You need {totalSurfaceArea:.2f} m^2 of gold foil to cover the pyramid")

