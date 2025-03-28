
from matplotlib import pyplot as plt
import numpy as np


girls_grades = [89, 90, 70, 89, 100, 80, 90, 100, 80, 34]
boys_grades = [10, 29, 49, 48, 100, 48, 38, 45, 20, 30]
grades_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
fig = plt.figure()

ax = fig.add_axes([0, 0, 1, 1])

ax.scatter(grades_range, girls_grades, color='r')
ax.scatter(grades_range, boys_grades, color='b')

ax.set_xlabel('Grades Range')
ax.set_ylabel('Grades Scored')

ax.set_title('scatter plot')
plt.show()