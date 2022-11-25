# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         DHRUV HALDERIA
# Section:      503
# Assignment:   LAB 10.14
# Date:         24 November 2022
# 
#below i have imported numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
#below imported warnings to ignore a deprecation warning that keeps occurring with numpy on vscode
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 
#below have the two arrays i have to combine
v = np.arange(2).reshape(2,1)
m = np.array([(1.09, 0.09),(-0.09, 1.01)])
xVal = np.array([])
yVal = np.array([])
# have a for loop that keeps multiplying inorder to get the values
for i in range(200):
    xVal = np.append(xVal, [float(v[0])])
    yVal = np.append(yVal, [float(v[1])])
    v = m@v
xVal = np.append(xVal, [float(v[0])])
yVal = np.append(yVal, [float(v[1])])
# plot the graph down below 
plt.xlim(-5000, max(xVal)+1000)
plt.ylim(min(yVal)-1000, 10000)
plt.xlabel('x')
plt.ylabel('y')
plt.title('Spiral from matrices multiplication ')
plt.plot(xVal, yVal,'r')
plt.tight_layout()
plt.show()
