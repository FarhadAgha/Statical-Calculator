income = float(input("Enter your total monthly income: $"))

rent = float(input("Enter rent: $"))
utilities = float(input("Enter utilities: $"))
other_fixed = float(input("Enter other fixed expenses: $"))
total_fixed = rent + utilities + other_fixed

print("\nEnter your variable expenses (groceries, entertainment, etc.).")
print("Type 0 when you have entered all expenses.")
total_variable = 0.0
while True:
    expense = float(input("Expense amount: $"))
    if expense == 0:
        break
    if expense < 0:
        print("Negative expense ignored. Please enter a positive number.")
        continue
    total_variable += expense

total_expenses = total_fixed + total_variable
remaining = income - total_expenses

if remaining < 0:
    print("\nWarning: Your expenses exceed your income!")
    print(f"Deficit: ${-remaining:.2f}")
else:
    print(f"\nYour remaining monthly budget is: ${remaining:.2f}")
print(f"\n--- Summary ---")
print(f"Total fixed expenses: ${total_fixed:.2f}")
print(f"Total variable expenses: ${total_variable:.2f}")
print(f"Total expenses: ${total_expenses:.2f}")
