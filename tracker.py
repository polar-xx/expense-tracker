# Project: Expense Tracker | Installment 3
# Author: Almazar, John Leo
# A program that logs expenses, calculates taxes, and checks a budget.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tTrack your daily spending")
print("=" * 40)

name = input("\nEnter your name: ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("\nEnter item 1: ")
amount1 = float(input(f"Enter amount for {item1}: "))

subtotal = 0
subtotal = subtotal + amount1

item2 = input("\nEnter item 2: ")
amount2 = float(input(f"Enter amount for {item2}: "))

subtotal = subtotal + amount2

average = subtotal / 2

tax_percent = float(input("\nEnter tax rate (as a whole number, e.g., 12): "))
tax = subtotal * (tax_percent / 100) 

total = subtotal + tax

budget = float(input("Enter your budget: "))

over_budget = total > budget
left = budget - total

print("\n" + "-" * 40)
print("SUMMARY")
print("-" * 40)
print(f"{item1}:\t\t${amount1:.2f}")
print(f"{item2}:\t\t${amount2:.2f}")
print(f"Subtotal:\t${subtotal:.2f}")
print(f"Average:\t${average:.2f}")
print(f"Tax ({tax_percent:.0f}%):\t${tax:.2f}")
print(f"Grand total:\t${total:.2f}")
print(f"Over budget?:\t{over_budget}")
print(f"Left in budget:\t${left:.2f}")
print("-" * 40)

print(f"Made by: Almazar, John Leo   |   Installment 3")
print("-" * 40)