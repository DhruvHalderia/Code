from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
x = [4,5,6,7]
y = [3,2,5,7]
plt.xlim(0, 7)
plt.ylim(0, 7)
plt.grid()
plt.plot(x, y,'r')
plt.show()