# week 1 - day 5
# Topic: plotting battery capacity degradation
import csv
import matplotlib.pyplot as plt # matplotlib is plotting library, pyplot- submodule it mimics matlab, plt is short cut name we assign so in future instead of writing matplotlib.pyplot.plot(..) we can write plt.plot(...)etc.
file_path = "data/battery_capacity.csv"
cycles = []
capacities = []
with open(file_path, mode="r") as file:
    csv_reader = csv.reader(file)
    header = next(csv_reader)

    for row in csv_reader:
        cycle = int(row[0])
        capacity = float(row[1])

        cycles.append(cycle)
        capacities.append(capacity)
    
print("Cycles:", cycles)
print("Capacities:", capacities)

import matplotlib.pyplot as plt

plt.figure(figsize=(6, 4)) #creates a canva of 6,4 inches(wide, height)
plt.plot(cycles, capacities, marker="o", linestyle="-") #cycle = x axis, capicities = y axis, marker 0 = experimental data points, linestyles - 
plt.xlabel("Cycle Number")
plt.ylabel("Capacity (Ah)")
plt.title("Battery Capacity Degradation")
plt.grid(True) #helps estimate values, imporves readability, and standard graph 
plt.tight_layout() #it ensures labels dont get cut and fits cleanly
plt.savefig("figures/capacity_vs_cycle.png", dpi=300)
plt.show()
# Capacity decreases with increasing cycle number 
# This indicates degradation due to repeated charge-discharge cycles