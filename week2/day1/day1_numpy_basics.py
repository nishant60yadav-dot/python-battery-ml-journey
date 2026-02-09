# week 2 - day 1
# Topic: NumPy basics for numerical data 
import numpy as np
capacities_list = [2.50, 2.47, 2.44, 2.40, 2.35]
capacities_array = np.array(capacities_list)
print("Python list:", capacities_list)
print("Numpy array:", capacities_array)

# Try mathematical operation
print("\nMultiply list by 2:")
print(capacities_list * 2)
print("\nMultiply NumPy array by 2:")
print(capacities_array * 2)

print("basic statistics:")
print("mean capacity:", np.mean(capacities_array))
print("min capacity:", np.min(capacities_array))
print("max capacity:", np.max(capacities_array))

print("\nIndexing and slicing:")
print("First capacity:", capacities_array[0])
print("Last capacity:", capacities_array[-1])
print("First three cycles:", capacities_array[:3])

initial_capacity = capacities_array[0]
fade_percent = (initial_capacity - capacities_array)/ initial_capacity * 100
print("\ncapacity fade (%):")
print(np.round(fade_percent, 2))

