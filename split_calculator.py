# This program calculates the total bill w/ tip and calculates how much each # person has to pay.

# Input : int value of your bill + tip
# Output: int value of your total bill / number of people

# Welcome user
print("Welcome to the tip Calculator.")

# Ask for the bill total
total_bill = float(input("What was the total bill? "))
# print(f"total bill = {total_bill}")

#Ask for how much to tip
tip_percentage = int(input("What percentage tip do you want to give? 10%, 12%, or 15%? "))
#print(f"tip percent = {tip_percentage}")

# Ask for the number of people to split the bill with
num_of_people = int( input("How many people to split the bill? ") )
#print(f"number of people = {num_of_people}")

# Calculate total cost w/ the tip
total_cost = total_bill * (1.0 + (tip_percentage/100))
#print(f"total_cost = {total_cost}")

# Split the total
split_cost = total_cost / num_of_people
print(f"split cost {split_cost}")

# Round the result to two decimal places
split_cost_rounded = ("%.2f" % split_cost)
print(f"split cost rounded = {split_cost_rounded}")

# Print the result
print(f"Each person should pay $ {split_cost_rounded}")
