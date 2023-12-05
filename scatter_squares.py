import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn-v0_8')
ax = plt.subplot()

# add dot on the graph (s - size)
ax.scatter(x_values, y_values, s=10, c=y_values, cmap=plt.cm.Blues)

# Set graff name and name each of axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set fontsize for signature on marking
ax.tick_params(axis='both', labelsize=14)

# Set range for each axis
ax.axis([0, 1100, 0, 1100000])

# plt.show()

# Save to file
plt.savefig('squares_plot.png', bbox_inches='tight')
