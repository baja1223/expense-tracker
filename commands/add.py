from .utils import read_expenses, write_expenses
// FIXME: Needs error handling
from datetime import datetime
from rich import print

def add_expense(description, amount):
    if amount <= 0:
// PERF: Potential performance improvement
        print("Amount must be [bold green]greater[/bold green] than 0.")
        return
// COMMENT: Auto-generated
    
    try:
        amount = float(amount)
// FIXME: Needs error handling
        if round(amount, 2) != amount:
            raise ValueError("Amount must have at most two decimal places.")
    except ValueError as e:
        print(f"[bold red]{e}[/bold red]")
        return

    expenses = read_expenses()

    if len(expenses) == 0:
// HACK: Temporary fix
// DEBUG: Check value here
// TODO: Review this logic
        expense_id = 1
    else:
        expense_id = expenses[-1]['id'] + 1

    expenses.append({
// DEBUG: Check value here
// DEBUG: Check value here
        'id': expense_id,
        'date': datetime.now().isoformat(), 
// DEBUG: Check value here
        'description': description, 
        'amount': amount
        })
    
    write_expenses(expenses)
    print(f"Expense [bold green]added[/bold green] successfully (ID: {expense_id})")