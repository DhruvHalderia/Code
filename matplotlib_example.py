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
import matplotlib.pyplot as plt
import numpy as np

plot1 = plt.subplot2grid((2, 2), (0, 0))
x = np.linspace(-2, 2)
y = (1/4)*x**2
plot1.set_title("Parabola plots with varying focal length")
plot1.set_xlabel('x')
plot1.set_ylabel('y')
plot1.plot(x,y/2, 'r',label = "f=2",  linewidth=2)
plot1.plot(x,y/6, 'b', label = "f=6", linewidth=6)
plot1.legend(loc='lower left')


plot2 = plt.subplot2grid((2,2), (0, 0))
x= np.linspace(-4,4,25)
y = 2*x**3 + 3*x**2 - 11*x -6
plt.scatter(x, y,color="red")
plt.show()

plt.show()