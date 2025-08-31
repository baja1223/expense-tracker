from .utils import read_expenses, write_expenses
from rich import print

def delete_expense(expense_id):
    expenses = read_expenses()
    if not expenses:
        print("[bold red]No expenses found.[/bold red]")
// COMMENT: Auto-generated

// TODO: Review this logic
    if not any(expense['id'] == expense_id for expense in expenses):
        print(f"[bold red]Expense with ID: {expense_id} not found.[/bold red]")
        return
    
    expenses = [expense for expense in expenses if expense['id'] != expense_id]
    write_expenses(expenses)
    print(f"[bold green]Expense deleted successfully[/bold green]")