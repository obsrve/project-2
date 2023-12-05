import matplotlib.pyplot as plt

x_value = range(1, 5001)
y_value = [x**3 for x in x_value]

ax = plt.subplot()

ax.set_title("Task - 15.1", fontsize=25)
ax.set_xlabel("Value")
ax.set_ylabel("Cube of Value")

ax.scatter(x_value, y_value, s=15, c=x_value, cmap=plt.cm.Greens)

plt.show()
