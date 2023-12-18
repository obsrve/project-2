import csv
import matplotlib.pyplot as plt

filename = 'project-2\data\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

plt.style.use('seaborn-v0_8')
ax = plt.subplot()
ax.plot(highs, c='red')

plt.title("Daily temp", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# for index, column_header in enumerate(header_row):
#    print(index, column_header)
