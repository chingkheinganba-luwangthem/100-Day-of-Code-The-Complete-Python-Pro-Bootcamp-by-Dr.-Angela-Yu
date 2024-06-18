# Printing a welcome message to the user
print("Welcome to the Tip Calculator!")

# Prompt the user to input the total bill amount
bill = float(input("What was the total bill: $"))

# Prompt the user to input the tip percentage they want to give (10, 12, or 15)
tip = int(input("How much tip would you like to give? 10, 12, or 15: "))

# Prompt the user to input the number of people splitting the bill
people = int(input("How many people to split the bill? : "))

# Calculate the tip amount as a percentage of the bill
tip_as_percent = tip / 100 

# Calculate the total tip amount by multiplying the bill by the tip percentage
total_tip_amount = bill * tip_as_percent

# Calculate the total bill amount by adding the original bill and the total tip amount
total_bill = bill + total_tip_amount

# Calculate the amount each person should pay by dividing the total bill by the number of people
bill_per_person = total_bill / people

# Round the final amount to two decimal places
final_amount = round(bill_per_person, 2)

# Format the final amount as a string with two decimal places for proper currency display
final_amount_str = "{:.2f}".format(final_amount)

# Print the amount each person should pay
print(f"Each person should pay: ${final_amount_str}")
