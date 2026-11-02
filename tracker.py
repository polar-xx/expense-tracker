# Project: Expense Tracker | Installment 2
# Author: Almazar, John Leo
# A program that takes user input to track and summarize expenses.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tTrack your daily spending")
print("=" * 40)

name = input("\nEnter your name: ")
print(f"Welcome, {name}! Let's log two expenses.")

item1 = input("\nEnter item 1: ")
amount1 = float(input(f"Enter amount for {item1}: "))

item2 = input("\nEnter item 2: ")
amount2 = float(input(f"Enter amount for {item2}: "))

total1 = amount1 + amount2
average = total1 / 2

print("\n" + "-" * 40)
print("SUMMARY")
print("-" * 40)
print(f"{item1}:\t\t${amount1:.2f}")
print(f"{item2}:\t\t${amount2:.2f}")
print(f"Total spent:\t${total1:.2f}")
print(f"Average:\t${average:.2f}")
print("-" * 40)

print(f"Made by: Almazar, John Leo   |   Installment 2")
print("-" * 40)