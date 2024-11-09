#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import json

class ExpenseTracker:
    def __init__(self, budget=0.0):
        self.budget = budget
        self.expenses = []  # list to store expense records
        self.categories = {}  # dictionary to store category-wise expenses
    
    def set_budget(self, budget):
        """Set a monthly budget."""
        self.budget = budget
        print(f"Monthly budget set to ${budget:.2f}")
    
    def add_expense(self, description, amount, category):
        """Add an expense to the tracker."""
        expense = {
            'description': description,
            'amount': amount,
            'category': category
        }
        self.expenses.append(expense)
        
        # Track category-wise spending
        if category in self.categories:
            self.categories[category] += amount
        else:
            self.categories[category] = amount
        
        print(f"Expense of ${amount:.2f} added under '{category}' category.")
    
    def view_expenses(self):
        """Display all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
        else:
            print("All Expenses:")
            for expense in self.expenses:
                print(f"{expense['description']} - ${expense['amount']:.2f} - {expense['category']}")
    
    def view_category_expenses(self):
        """Display expenses by category."""
        if not self.categories:
            print("No expenses recorded by category.")
        else:
            print("Expenses by Category:")
            for category, total in self.categories.items():
                print(f"{category}: ${total:.2f}")
    
    def view_budget_status(self):
        """Check if user has exceeded the budget."""
        total_spent = sum(expense['amount'] for expense in self.expenses)
        remaining_budget = self.budget - total_spent
        print(f"Total spent: ${total_spent:.2f}")
        print(f"Remaining budget: ${remaining_budget:.2f}")
        
        if total_spent > self.budget:
            print("Warning: You have exceeded your budget!")
        elif remaining_budget < 0.1 * self.budget:
            print("Alert: You are close to exceeding your budget!")
        else:
            print("You are within your budget.")

    def save_to_file(self, filename):
        """Save expenses and budget to a file."""
        data = {
            'budget': self.budget,
            'expenses': self.expenses
        }
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved to {filename}")
    
    def load_from_file(self, filename):
        """Load expenses and budget from a file."""
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                self.budget = data['budget']
                self.expenses = data['expenses']
                self.categories.clear()
                
                # Rebuild category-wise expenses
                for expense in self.expenses:
                    category = expense['category']
                    amount = expense['amount']
                    if category in self.categories:
                        self.categories[category] += amount
                    else:
                        self.categories[category] = amount
                print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print(f"No previous data found in {filename}. Starting fresh.")
        except json.JSONDecodeError:
            print("Error reading data from file.")

# Menu-driven interface
def display_menu():
    """Display the menu for user input."""
    print("\nPersonal Expense Tracker")
    print("1. Set monthly budget")
    print("2. Add an expense")
    print("3. View all expenses")
    print("4. View expenses by category")
    print("5. View budget status")
    print("6. Save data to file")
    print("7. Load data from file")
    print("8. Exit")

def main():
    tracker = ExpenseTracker()

    while True:
        display_menu()
        choice = input("Enter choice (1-8): ")

        if choice == '1':
            budget = float(input("Enter your monthly budget: $"))
            tracker.set_budget(budget)
        
        elif choice == '2':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: $"))
            category = input("Enter category (e.g., Food, Entertainment): ")
            tracker.add_expense(description, amount, category)
        
        elif choice == '3':
            tracker.view_expenses()
        
        elif choice == '4':
            tracker.view_category_expenses()
        
        elif choice == '5':
            tracker.view_budget_status()
        
        elif choice == '6':
            filename = input("Enter filename to save data (e.g., expenses.json): ")
            tracker.save_to_file(filename)
        
        elif choice == '7':
            filename = input("Enter filename to load data (e.g., expenses.json): ")
            tracker.load_from_file(filename)
        
        elif choice == '8':
            print("Exiting the Expense Tracker.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()


# In[ ]:


pip install nbconvert


# In[ ]:




