from matplotlib import pyplot as plt
import numpy as np

collectn_1 = np.random.normal(100,10,200)
collectn_2 = np.random.normal(80,30,200)
collectn_3 =np.random.normal(90,20,200)
collectn_4 = np.random.normal(70,25,200)

data_to_plot = [collectn_1,collectn_2,collectn_3,collectn_4]
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])

bp =ax.violinplot(data_to_plot)
plt.show()