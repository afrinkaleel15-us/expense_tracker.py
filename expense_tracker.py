import csv
import os

FILE_NAME = "expenses.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Amount"])


def add_expense():
    category = input("Enter expense category: ")
    amount = float(input("Enter amount: "))

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, amount])

    print("Expense added successfully!")


def view_expenses():
    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header

        print("\n--- Expenses ---")
        found = False

        for row in reader:
            print(f"Category: {row[0]}, Amount: ₹{row[1]}")
            found = True

        if not found:
            print("No expenses found.")


def total_expenses():
    total = 0

    with open(FILE_NAME, mode="r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total += float(row[1])

    print(f"\nTotal Expenses: ₹{total}")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_expenses()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
