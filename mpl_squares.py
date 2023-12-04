import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 100]

fig = plt.subplot()
ax = plt.subplot()
ax.plot(input_values, squares, linewidth=3)

# Set graff name and name each of axis
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set fontsize for signature on marking
ax.tick_params(axis='both', labelsize=10)


plt.show()
