from matplotlib import pyplot as plt
import numpy as np

x = np.array([0,1,2,3])
y = np.array([10,20,30,40])

plt.subplot(1,2,2)
plt.plot(x,y)
plt.show()
