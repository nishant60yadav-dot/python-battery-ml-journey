#week 1 - day 3
# topic - functions and resuable scentific logic
def calcualate_capacity_loss(initial_capacity, final_capacity):
    """
    calculate absolute capacity loss (Ah)
    """
    loss = initial_capacity - final_capacity
    return loss
def calculate_capacity_fade_percentage(initial_capacity, current_capacity):
    """
    calculate percentage capacity fade
    """
    fade = (initial_capacity - current_capacity)/ initial_capacity * 100
    return fade
fade_percent = calculate_capacity_fade_percentage(2.5, 2.35)
print ("Capacity fade:", round(fade_percent, 2), "%")
batttery_capacities = [2.50, 2.47, 2.44, 2.40, 2.35]
initial_capacity = batttery_capacities[0]
print("\nCapacity fade per cycle:")
for cap in batttery_capacities:
    fade = calculate_capacity_fade_percentage(initial_capacity, cap)
    print("capacity:", cap, "Ah-Fade", round(fade, 2), "%")