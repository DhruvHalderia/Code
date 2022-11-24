# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Tilman Strickland
#               Dhruv Halderia
#               Logan Stringer
# Section:      503
# Assignment:   12.15
# Date:         11/23/2022
# As a team, we have gone through all required sections of the  
# tutorial, and each team member understands the material 
import matplotlib.pyplot as plt
import numpy as np

# im making the graphs down below using different figures
#below is figure 1 
plt.figure(1)
x = np.linspace(-2, 2)
y = (1/4)*x**2
plt.plot(x,y/2,'r', label = 'f = 2', linewidth = 2)
plt.plot(x,y/6,'b', label = 'f = 6', linewidth = 6 )
plt.legend()
plt.xlabel("x")
plt.ylabel("y")

#below is figure 2
plt.figure(2)
x1 = np.linspace(-4, 4,25)
y1 = 2*x1**3 + 3*x1**2 -11*x1 - 6
plt.scatter(x1,y1,color = 'yellow', marker = '*', edgecolors='black')
plt.xlabel('x values')
plt.ylabel('y values')

#below is figure 3
plt.figure(3)
fig, (ax1, ax2) = plt.subplots(2, sharex = True)
x2 = np.linspace(-2*np.pi, 2*np.pi)
y2 = np.sin(x2)
y3 = np.cos(x2)
ax1.plot(x2, y3, 'r', label = 'cos(x)')
ax2.plot(x2, y2,'grey', label = 'sin(x)')
ax1.legend(loc = 'lower right')
ax2.legend()
ax1.set_ylabel('y = cos(x)')
ax2.set_ylabel('y = sin(x)')
ax1.grid()
ax2.grid()
plt.show()
