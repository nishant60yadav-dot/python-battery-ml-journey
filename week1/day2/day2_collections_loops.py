# Week 1 - day 2
# Topic: lists, loops, and basic logic 
# list of battery capacititew (Ah) over cycles 
capacities = [2.50, 2.47, 2.44, 2.40, 2.35]
print("All capacitiets:", capacities)
# access individual values 
print("Initial capacity:", capacities[0])
print("Capacitiy after 5 cycles:", capacities[-1])
print("\nLooping over capacitites:\n")
for cap in capacities:
    print(cap)
print("\nChecking capacities fade:")
for cap in capacities:
    if cap < 2.45:
        print (cap, "Ah - capacity is degrading")
    else:
        print(cap, "Ah - capacity s healthy")
# Dictionary: cycle number - capacity
battery_data = {1:2.50, 2:2.47, 3:2.44, 4:2.40, 5:2.35}
print("\nBattery data dictionary:", battery_data)
print("\nCapacity at cycle 3:", battery_data[3])
print("\nLooping through battery data")
for cycle, cap in battery_data.items():
    print("cycle:", cycle, "|Capacity:", cap)
#calculate percetage capacity fade
initial_capacity = battery_data[1]
print("\nPercentage capacity fade:")
for cycle, cap in battery_data.items():
    fade = (initial_capacity - cap)/ initial_capacity * 100
    print("cycle", cycle, "- fade:", round(fade, 2), "%")