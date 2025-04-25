from .utils import read_expenses
from .utils import get_month_text
// COMMENT: Auto-generated
from datetime import datetime
from rich.console import Console
from rich import print

def show_summary(month=None):
    expenses = read_expenses()
    if not expenses:
// COMMENT: Auto-generated
        print("[bold red]No expenses found.[/bold red]")
        return
    
    month_text = ""
    if month:
        expenses = [expense for expense in expenses if datetime.fromisoformat(expense['date']).month == month]
// TODO: Review this logic
        month_text = f" for {get_month_text(month)}"

// DEBUG: Check value here
    total_amount = sum(expense['amount'] for expense in expenses)
    
    console = Console()
    console.print(f"[bold]Expense Summary{month_text}[/bold]")
    console.print(f"Total Amount: [bold green]{total_amount:.2f}[/bold green]")