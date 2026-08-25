import json

filename = "expenses.json"


def load_expenses():
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses):
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    description = input("\nenter expense description: ").strip()
    category = input("enter category: ").strip()

    try:
        amount = float(input("enter amount: "))

        if amount <= 0:
            print("amount must be greater than 0.")
            return

    except ValueError:
        print("please enter a valid amount.")
        return

    expense = {
        "description": description,
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("expense added! ")


def view_expenses(expenses):
    if not expenses:
        print("\nno expenses recorded! ")
        return

    print("\n===== EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. {expense['description']} | "
            f"{expense['category']} | "
            f"₹{expense['amount']:.2f}"
        )


def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)

    print(f"\ntotal spending: ₹{total:.2f} ")


def category_summary(expenses):
    if not expenses:
        print("\nno expenses recorded!")
        return

    categories = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in categories:
            categories[category] += amount
        else:
            categories[category] = amount

    print("\n===== CATEGORY SUMMARY =====")

    for category, amount in categories.items():
        print(f"{category}: ₹{amount:.2f}")


def delete_expense(expenses):
    view_expenses(expenses)

    if not expenses:
        return

    try:
        number = int(input("\nenter the expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)
            save_expenses(expenses)

            print(
                f"deleted: {deleted['description']} "
                f"₹{deleted['amount']:.2f} ️"
            )
        else:
            print("invalid expense number.")

    except ValueError:
        print("please enter a valid number.")


expenses = load_expenses()

while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. add expense")
    print("2. view expenses")
    print("3. show total spending")
    print("4. category summary")
    print("5. delete expense")
    print("6. exit")

    choice = input("\nchoose an option: ").strip()

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        view_expenses(expenses)

    elif choice == "3":
        show_total(expenses)

    elif choice == "4":
        category_summary(expenses)

    elif choice == "5":
        delete_expense(expenses)

    elif choice == "6":
        print("goodbye! ")
        break

    else:
        print("invalid choice. please try again.")
