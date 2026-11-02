# Project: Expense Tracker | Installment 5
# Author: Almazar, John Leo
# A program that keeps track of expenses using a menu loop.

print("=" * 40)
print("\tEXPENSE TRACKER")
print("\tTrack your daily spending")
print("=" * 40)

name = input("\nEnter your name: ")
tax_percent = float(input("Enter tax rate (as a whole number, e.g., 12): "))
budget = float(input("Enter your budget: "))
print(f"Welcome, {name}!")

subtotal = 0.0
count = 0

choice = ""
while choice != "4":
    print("\nMAIN MENU")
    print("1. Add an expense")
    print("2. View all expenses      (coming soon)")
    print("3. Show total spent")
    print("4. Exit")
    
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Enter amount: $"))
        
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
            
        subtotal = subtotal + amount
        count = count + 1
        
    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")
        
    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total
        over_budget = total > budget
        
        print("\n  SUMMARY")
        print(f"  Expenses:\t{count}")
        print(f"  Subtotal:\t${subtotal:.2f}")
        print(f"  Tax ({tax_percent:.0f}%):\t${tax:.2f}")
        print(f"  Grand total:\t${total:.2f}")
        
        if over_budget:
            print(f"  Over budget by ${abs(left):.2f}!")
        elif total > (budget * 0.90):
            print(f"  Careful: only ${left:.2f} left.")
        else:
            print(f"  Within budget. ${left:.2f} left.")
            
    elif choice == "4":
        print(f"\nGoodbye, {name}!")
        
    else:
        print("  Please choose 1, 2, 3 or 4.")

print("\n" + "-" * 40)
print(f"Made by: {name}   |   Installment 5")
print("-" * 40)