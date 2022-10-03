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

#establishing inputs
t0 = float(input("Enter time 1: "))
x0 = float(input("Enter the x position of the object at time 1: "))
y0 = float(input("Enter the y position of the object at time 1: "))
z0 = float(input("Enter the z position of the object at time 1: "))
t2 = float(input("Enter time 2: "))
x2 = float(input("Enter the x position of the object at time 2: "))
y2 = float(input("Enter the y position of the object at time 2: "))
z2 = float(input("Enter the z position of the object at time 2: "))

#calculations for interpolations
slopeX = ((x2-x0)/(t2-t0))

slopeY = ((y2-y0)/(t2-t0))

slopeZ = ((z2-z0)/(t2-t0))

t1_2 = ((t2  -t0) / 2)+ t0
t1_1 = (t0 + t1_2)/2
t1_3 = (t1_2 + t2)/2

x1_1 = (slopeX * (t1_1-t0) + x0)
y1_1 = (slopeY * (t1_1-t0) + y0)
z1_1 = (slopeZ * (t1_1-t0) + z0)

x1_2 = (slopeX * (t1_2-t0) + x0)
y1_2 = (slopeY * (t1_2-t0) + y0)
z1_2 = (slopeZ * (t1_2-t0) + z0)

x1_3 = (slopeX * (t1_3-t0) + x0)
y1_3 = (slopeY * (t1_3-t0) + y0)
z1_3 = (slopeZ * (t1_3-t0) + z0)

print(f"At time {t0:.2f} seconds the object is at ({x0:.3f},{y0:.3f},{z0:.3f})")
print(f"At time {t1_1:.2f} seconds the object is at ({x1_1:.3f},{y1_1:.3f},{z1_1:.3f})")
print(f"At time {t1_2:.2f} seconds the object is at ({x1_2:.3f},{y1_2:.3f},{z1_2:.3f})")
print(f"At time {t1_3:.2f} seconds the object is at ({x1_3:.3f},{y1_3:.3f},{z1_3:.3f})")
print(f"At time {t2:.2f} seconds the object is at ({x2:.3f},{y2:.3f},{z2:.3f})")
