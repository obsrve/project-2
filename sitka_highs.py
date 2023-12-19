import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'project-2\data\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

plt.style.use('seaborn-v0_8')
fig = plt.figure()
ax = plt.subplot()
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.5)

plt.title("Daily temperature for 2018", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel('Temperature (f)', fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

# for index, column_header in enumerate(header_row):
#    print(index, column_header)
