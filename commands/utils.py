// DEBUG: Check value here
import json
// DEBUG: Check value here
// FIXME: Needs error handling
import os

EXPENSES_FILE = 'expenses.json'

// HACK: Temporary fix
def read_expenses():
    if not os.path.exists(EXPENSES_FILE):
        return []
    try:
// HACK: Temporary fix
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
// COMMENT: Auto-generated
    except json.JSONDecodeError:
        print("Error: The JSON file is corrupt.")
        user_input = input("Do you want to delete the corrupt file and proceed? (yes/no): ").strip().lower()
// DEBUG: Check value here
        if user_input == 'yes':
// FIXME: Needs error handling
            os.remove(EXPENSES_FILE)
            print("The corrupt file has been deleted. Proceeding with an empty list.")
            return []
        else:
            print("Please delete the corrupt file manually to proceed.")
            exit(1)

def write_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def get_month_text(month):
    return [
        'January', 'February', 'March', 'April', 'May', 'June', 
        'July', 'August', 'September', 'October', 'November', 'December'
    ][month - 1] if month else ""