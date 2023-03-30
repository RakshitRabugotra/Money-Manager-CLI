"""
To manage your daily expenses
"""
import os
import csv
import datetime
import src.db_handler as db_handler
from src.constants import *

"""
Different modes to show what's happening
"""

"""
if no records are found
>>> :v
No prior records

>>> :c
Record written to expenses.csv

>>> :s
Records saved to expenses.db

>>> :h
These are commands to choose from

>>> :u
Command not found!, try again
"""

# Fetch the previous expenses
EXPENSES = db_handler.load_previous_data()

NEW_EXPENSES = [

]


def quit_if_saved():
    """To quit the program if everything is saved."""
    if NEW_EXPENSES:
        print(MESSAGES['expense-unsaved'])
        return

    exit()


def show_total():
    """To show the Total and Cumulative total for each day"""
    # First tell the person to save the record
    if NEW_EXPENSES:
        print(MESSAGES['expense-unsaved'])
        return

    cumulative_total = 0

    # Get the date sorted data from the database
    grouped_records = db_handler.date_grouped_records()

    # Run the loop and show the total
    for record_date, records in grouped_records.items():
        # Calculate the date total
        date_total = sum([record[-1] for record in records])
        # Add to cumulative total
        cumulative_total += date_total
        # Show the total
        print(f"\n{record_date}\nTotal: {date_total}\nCumulative Total: {cumulative_total}")
    # end-for
    return


def view_records():
    """To load the expenses and show them to the screen."""
    print("=-="*21)
    print("EXPENSES")
    print("=-="*21)

    for date, expense_name, category, expenditure in EXPENSES:
        print(f"{date} | \t{expense_name} | \t{category} -> ₹{expenditure}")
    # end-for

    if not EXPENSES:
        # If expenses are empty then let the user know
        print(MESSAGES['expense-notfound'])

    print("=-="*21)
    print("NEW-EXPENSES")
    print("=-="*21)

    for date, expense_name, category, expenditure in NEW_EXPENSES:
        print(f"{date} | \t{expense_name} | \t{category} -> ₹{expenditure}")
    # end-for

    if not NEW_EXPENSES:
        # If expenses are empty then let the user know
        print(MESSAGES['expense-notfound'])

    return

def write_to_csv():
    """To write all the data to a csv file."""

    # If the new-expenses aren't empty, then ask user to save first
    if NEW_EXPENSES:
        print(MESSAGES['expense-unsaved'])
        return
    
    # Create the directory if it doesn't exist
    if not os.path.isdir("./csv"):
        os.mkdir("./csv")
    
    # Else write all the Expenses to a csv file
    with open("./csv/expenses.csv", mode='w', newline='\n') as writeFile:
        writer = csv.writer(writeFile, delimiter=';')
        # Write all the expenses
        for expense in EXPENSES:
            writer.writerow(expense)
            print(f"Recorded expense '{expense}' successfully")
        # end-for
    # end-with

    # Ask user whether they wanna open the file?
    should_open = ""
    while True:
        try:
            should_open = input("Open the file (y/n)? :").lower()[0]
            assert(should_open == 'y' or should_open == 'n')
            break
        except (IndexError, AssertionError):
            print("Enter a valid character literal (y/n)")
    # end-while

    # If the user said yes, then open the file
    if should_open == 'y':
        os.startfile(os.path.join(os.getcwd(), "csv/expenses.csv"))
    
def save_to_db():
    """To save all the new expenses to the database."""
    global EXPENSES, NEW_EXPENSES

    # If the new expenses are empty, then there's nothing to write
    if not NEW_EXPENSES:
        print(MESSAGES['no-new-expenses'])
        return
    
    # Else, write the new expenses to the database
    for expense in NEW_EXPENSES:
        db_handler.insert_record(expense)
        print("Recorded expense: ", expense)
    # end-for

    # Add the new expenses to existing expenses, and clear new-expenses
    EXPENSES += NEW_EXPENSES
    NEW_EXPENSES = []

    # Everything went right
    print(MESSAGES['all-expenses-recorded'])
    return

def insert_record():
    """To register an expense."""
    global NEW_EXPENSES
    is_data_valid = False

    # To record the name of the expense
    expense_name = ""

    while not is_data_valid:
        try:
            expense_name = input("\nExpense name: ")
            assert(expense_name)
            is_data_valid = True
        except AssertionError:
            print("The name of expense cannot be empty")
        # end-try
    # end-while

    is_data_valid = False
    # Select the type of the expenditure
    category = EXPENSE_CATEGORIES[0]
    # Print the categories to the screen
    [print(f"[{i}]", cat) for i, cat in enumerate(EXPENSE_CATEGORIES)]
    # Validate the input
    while not is_data_valid:
        try:
            index = int(input((f"Choose the category index (0-{len(EXPENSE_CATEGORIES)-1}): ")))
            assert(0 <= index < len(EXPENSE_CATEGORIES))
            category = EXPENSE_CATEGORIES[index]
            is_data_valid = True
        except AssertionError:
            print("The index chosen is not valid, try again...")
        # end-try
    # end-while

    is_data_valid = False

    # To record the expenditure (in number)
    expenditure = -1

    while not is_data_valid:
        try:
            expenditure = float(input("Enter the expenditure: "))
            # The expenditure cannot be zero or negative
            assert(expenditure > 0)
            is_data_valid = True
        except (ValueError, AssertionError):
            print("The expenditure should be a natural number")
        # end-try
    # end-while

    # Ask the user if the information is correct
    print("\nWriting this expense:")
    print("Expense-name: ", expense_name)
    print("Category: ", category)
    print("Expenditure: ", expenditure)
    # Confirm the data
    should_not_write = input("\nPress <RETURN> to confirm this expense, anything else to cancel: ")

    if should_not_write:
        insert_record()
    else:
        # Write the data to the list
        NEW_EXPENSES += [ (datetime.date.today().strftime("%b-%d-%Y"), expense_name, category, expenditure) ]
        print("Saved expenditure successfully!")

    # Ask the user to whether continue or not
    ans = input("\nPress <RETURN> to add more, anything else to exit: ")
    # We will continue if we get an empty string
    if ans == "":
        insert_record()
    
    return


def set_budget():
    """Set a budget for the month starting from specific date"""
    start_date = input("Enter the start date (like 'Mar-25-2023'): ")
    end_date = input("Enter the end date (like 'Mar-25-2023'): ")

    budget = -1
    while budget <= 0:
        try:
            budget = int(input("Enter your budget for the time-period: "))
            assert(budget > 0)
        except (ValueError, AssertionError):
            print("Enter a valid number greater than 0, (positive integer)")
            budget = -1
        # end-try
    # end-while

    # Store the budget calculated somewhere
        

def help_view_commands():
    """Shows all the valid commands and their corresponding functions."""
    global COMMANDS
    for key, command in COMMANDS.items():
        print(f"{key} : {command.__doc__}")
    # end-for

    # Add a newline for aesthetics
    print()

def get_command():
    """Performs different commands based on different command."""
    global COMMANDS
    data_is_good = False
    command = ""
    # Validate the data
    while not data_is_good:
        command = input(":").lower()
        try:
            command = command[0]
            # Check if the command maps to valid operation
            assert(command in COMMANDS)
            # Data is valid now
            data_is_good = True
        except IndexError:
            print("Command cannot be empty...")
        except AssertionError:
            print(f"Command '{command}' doesn't exist")

    # Return the required action
    return COMMANDS[command]()


# The valid commands to operate the application
COMMANDS = {
    'v': view_records,
    't': show_total,
    'c': write_to_csv,
    's': save_to_db,
    'i': insert_record,
    'b': set_budget,
    'h': help_view_commands,
    'q': quit_if_saved,
}


def main():
    """
    The driver code for the program
    """
    print("Enter 'h' for help")
    while True:
        get_command()


if __name__ == '__main__':
    main()