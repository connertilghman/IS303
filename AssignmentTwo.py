# Road Trip Planner
# IS 303 - Hilton
# This program asks the user for trip details, calculates the cost
# of the trip, and displays a trip-cost summary.

# Collect user input
name = input("What is your name? ")
destination = input("Where are you traveling? ")
one_way_miles = float(input("How many miles is the trip one way? "))
miles_per_gallon = float(input("What is your vehicle's miles per gallon? "))
gas_price_per_gallon = float(input("What is the gas price per gallon? "))
num_travelers = int(input("How many travelers are going? "))

# Perform calculations
round_trip_miles = one_way_miles * 2
gallons_needed = round_trip_miles / miles_per_gallon
total_gas_cost = gallons_needed * gas_price_per_gallon
cost_per_traveler = total_gas_cost / num_travelers

# Display trip summary
print(f"Traveler: {name.upper()}")
print(f"Destination: {destination}")
print(f"Gallons of Gas: {gallons_needed:.1f}")
print(f"Gas cost: ${total_gas_cost:.2f}")
print(f"Cost per traveler: ${cost_per_traveler:.2f}")
