
import csv
import os

FILE = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE):
        with open(FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Type", "Category", "Amount"])

def add_transaction():
    t_type = input("Type (Income/Expense): ").capitalize()
    category = input("Category: ")
    while True:
        try:
            amount = float(input("Amount: "))
            break
        except ValueError:
            print("❌ Enter a valid number.")

    with open(FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([t_type, category, amount])
    print("✅ Transaction added!")

def view_summary():
    total_income = 0
    total_expense = 0
    with open(FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Type"] == "Income":
                total_income += float(row["Amount"])
            elif row["Type"] == "Expense":
                total_expense += float(row["Amount"])

    print(f"\n💰 Total Income: {total_income}")
    print(f"💸 Total Expense: {total_expense}")
    print(f"🏦 Balance: {total_income - total_expense}\n")

def main():
    initialize_file()
    while True:
        print("\n=== Expense Tracker ===")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_transaction()
        elif choice == '2':
            view_summary()
        elif choice == '3':
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, try again.")

if __name__ == "__main__":
    main()

