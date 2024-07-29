class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = []
        self.categories = set()  # Set to store unique categories

    def add_income(self, amount):
        self.income += amount

    def add_expense(self, category, amount):
        self.expenses.append({'category': category, 'amount': amount})
        self.categories.add(category)

    def calculate_budget(self):
        total_expenses = sum(entry['amount'] for entry in self.expenses)
        remaining_budget = self.income - total_expenses
        return remaining_budget

    def analyze_expenses(self):
        # Implement expense analysis logic (optional)
        pass

    def save_to_file(self, filename):
        # Implement saving data to a file
        pass

    def load_from_file(self, filename):
        # Implement loading data from a file
        pass

# Main program loop
def main():
    budget_tracker = BudgetTracker()

    while True:
        print("\n===== Budget Tracker Menu =====")
        print("1. Add Income")
        print("2. Add Expense")
        print("3. Calculate Budget")
        print("4. Analyze Expenses")
        print("5. Save Data")
        print("6. Load Data")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            budget_tracker.add_income(amount)
        elif choice == '2':
            category = input("Enter expense category: ")
            amount = float(input("Enter expense amount: "))
            budget_tracker.add_expense(category, amount)
        elif choice == '3':
            remaining_budget = budget_tracker.calculate_budget()
            print(f"Remaining budget: {remaining_budget}")
        elif choice == '4':
            budget_tracker.analyze_expenses()
            # Implement display of expense analysis
        elif choice == '5':
            filename = input("Enter filename to save data: ")
            budget_tracker.save_to_file(filename)
        elif choice == '6':
            filename = input("Enter filename to load data: ")
            budget_tracker.load_from_file(filename)
        elif choice == '7':
            print("Exiting Budget Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
