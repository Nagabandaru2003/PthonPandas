from matplotlib import pyplot as plt
import numpy as np

ypoints = np.array([3,8,1,10])

plt.plot(ypoints,marker= '*',ms= 10,mec = 'r',mfc = 'g')
plt.show()