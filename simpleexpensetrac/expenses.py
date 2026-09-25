import os, json

def main():

    expenses = load_expenses()

    while True:
        print("\n===== LIST OF ACTIVITIES TO DO =====")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. View total")
        print("4. View category totals")
        print("5. Delete expenses")
        print("6. Save and exit")

        choice = input("Choose an option (1-5): ")
        print()

        if choice == "1":
            add_expenses(expenses)
        
        elif choice == "2":
            display_expenses(expenses)

        elif choice == "3":
            total = (calculate_total(expenses))
            print(f"Total: {total}")

        elif choice == "4":
            totals_by_category(expenses)

        elif choice == "5":
            delete_expenses(expenses)

        elif choice == "6":
            print("see you later")
            break

        else:
            print("Invalid choice.")

        save_expenses(expenses)



def load_expenses():
    if not os.path.exists("expenses.json"):
        print("File does not exist. Starting with an empty expense list.")
        return []

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

            if not isinstance(expenses, list):
                print("Error: expenses.json should contain a list.")
                return []

            return expenses

    except json.JSONDecodeError:
        print("Error: expenses.json contains invalid JSON.")
        print("Starting with an empty expense list.")
        return []


def save_expenses(expenses):
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)


def add_expenses(expenses):
    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Invalid choice. Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("Invalid choice. Please enter a number.")

    category = input("Enter category: ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)

    print("Expense added successfully!")


def display_expenses(expenses):
    if not expenses:
        print("Empty list")
        return

    num = 1
    for expense in expenses:

        print(f"===== ref [{num}]=====")

        for key, value in expense.items():
            print(f"{key:<20}: {value}")
        print()
        num += 1


def calculate_total(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


def delete_expenses(expenses):
    if not expenses:
        print("No expenses to delete.")
        return

    display_expenses(expenses)

    choice = int(input("Enter the number of the expense to delete: "))

    if 1 <= choice <= len(expenses):
        deleted = expenses.pop(choice - 1)
        print(f"Deleted: {deleted['category']} - {deleted['amount']}")
    else:
        print("Invalid expense number.")



def totals_by_category(expenses):
    totals = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in totals:
            totals[category] += amount
        else:
            totals[category] = amount

    for key, value in totals.items():
        print(f"category: {key:<13} Amount: $ {value:.2f}")



if __name__ == "__main__":
    main()