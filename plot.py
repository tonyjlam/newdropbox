import numpy as np
import pylab as plt

x = np.array([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
y = np.power(x, 2)
e = np.array([148.9, 82.0, 52.3, 38.0, 28.5, 18.9, 14.4, 11.0, 7.9, 5.3])

plt.errorbar(x, y, e, linestyle='None', marker = '^')
plt.show()
