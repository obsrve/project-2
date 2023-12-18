import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Create random walking
rw = RandomWalk()
rw.fill_walk()

# Paint dot`s on the graph
plt.style.use('classic')
ax = plt.subplot()
ax.plot(rw.x_values, rw.y_values, linewidth=5)
plt.show()
