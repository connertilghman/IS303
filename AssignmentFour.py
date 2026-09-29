# Expense Tracker
# The user enters expenses, and the program calculates summary statistics.

expenses = []

while True:
    expense = float(input("Enter an expense (0 to finish): $"))

    # 0 ends the program
    if expense == 0:
        break

    # Negative expenses are invalid
    if expense < 0:
        print("Invalid expense. Please enter a positive amount.")
        continue

    # Add the expense to the list
    expenses.append(expense)

# Analyze the expenses
total_expenses = sum(expenses)
number_of_expenses = len(expenses)

# Avoid division by zero if no expenses were entered
if number_of_expenses > 0:
    average_expense = total_expenses / number_of_expenses
    smallest_expense = min(expenses)
    largest_expense = max(expenses)

    small_count = 0
    moderate_count = 0
    large_count = 0

    # Classify each expense
    for expense in expenses:
        if expense < 25:
            small_count += 1
        elif expense <= 100:
            moderate_count += 1
        else:
            large_count += 1

    # Display results
    print("Total number of expenses:", number_of_expenses)
    print(f"Total expenses: ${total_expenses:.2f}")
    print(f"Average expense: ${average_expense:.2f}")
    print(f"Smallest expense: ${smallest_expense:.2f}")
    print(f"Largest expense: ${largest_expense:.2f}")
    print("Small expenses:", small_count)
    print("Moderate expenses:", moderate_count)
    print("Large expenses:", large_count)

else:
    print("\nNo expenses were entered.")