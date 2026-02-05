# Week1 day 4
# Topic - reading csv files using pure python
import csv # import done
file_path = "data/battery_capacity.csv" # told path
cycles = [] # creating empty list because we do not know the values csv will provide it
capacities = []
with open(file_path, mode="r") as file: # opens file path and mode is reading as file file is the object and with is just for after doing it close it
    csv_reader = csv.reader(file) # it creates csv reader now it can read for loop otherwise no loop
    header = next(csv_reader) # skip reader row
    for row in csv_reader:
        cycle = int(row[0]) # it converts string to integer row 0 will be converted to number after skipping header = next(csv_reader)
        capacity = float(row[1]) # it converts to 2.50 to 2.5
        cycles.append(cycle) # append will keep on adding value in list other wise it will stop only after 1 loop and will not include in the list
        capacities.append(capacity)
print("Cycles:", cycles)
print("Capacities:", capacities)
# Apply scientific logic: capacity fade calculation 
initial_capacity = capacities[0]
print("\nCapacity fade per cycle:")
for cycle, cap in zip(cycles, capacities): # zip will pair cycle and capacity position wise like (1,2.5)i
    fade = (initial_capacity - cap)/ initial_capacity*100
    print("Cycle", cycle, "- Fade:", round(fade, 2), "%")
