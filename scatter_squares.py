import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn-v0_8')
ax = plt.subplot()

# add dot on the graph (s - size)
ax.scatter(x_values, y_values, s=100)

# Set graff name and name each of axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set fontsize for signature on marking
ax.tick_params(axis='both', labelsize=14)

plt.show()
