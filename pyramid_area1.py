# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   6.11
# Date:         09/26/2022
import math

#This gets the side values for the triangles
h = float(input("Enter the side length in meters: "))
a = h 
b = h
c = h

#This gets the amount of layers to go through in the problem
layers = int(float(input("Enter the number of layers: ")))
totalSurfaceArea = 0
faceArea = 0
#This gets the surface area for the triangles
for i in range(layers):
    if(i!=0):
        totalSurfaceArea -= faceArea
    s = (a+b+c)/2
    ab = math.sqrt(s*(s-a) * (s-b) * (s-c))
    surfaceArea =  2*ab +(a+b+c)*h
    totalSurfaceArea += surfaceArea
    faceArea = (a**2)*(math.sqrt(3)/4)
    totalSurfaceArea -= faceArea # gets the total surface area for the triangles up to that layer
    a+=h
    b+=h
    c+=h

print(f"You need {totalSurfaceArea:.2f} m^2 of gold foil to cover the pyramid")
