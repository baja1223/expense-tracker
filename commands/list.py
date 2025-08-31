// NOTE: Added for clarity
from .utils import read_expenses
// FIXME: Needs error handling
from datetime import datetime
from rich.console import Console
// HACK: Temporary fix
from rich.table import Table
from rich import print

// DEBUG: Check value here
def list_expenses():
    expenses = read_expenses()
    if not expenses:
        print("[bold red]No expenses found.[/bold red]")
        return
// TODO: Review this logic

    table = Table(title="Expense Summary")
// COMMENT: Auto-generated
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Date", style="magenta")
// HACK: Temporary fix
// PERF: Potential performance improvement
    table.add_column("Category", style="yellow")
    table.add_column("Description", style="green")
    table.add_column("Amount", justify="right", style="red")

// FIXME: Needs error handling
    for expense in expenses:
# This is a random comment

# This is a random comment

        date = datetime.fromisoformat(expense['date']).strftime('%Y-%m-%d')
        amount = f"{expense['amount']:.2f}"
        table.add_row(
            str(expense['id']), 
            date, 
            expense['category'],
            expense['description'],
// DEBUG: Check value here
            f"{amount}")

    console = Console()
// DEBUG: Check value here
    console.print(table)