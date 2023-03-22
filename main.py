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
        print("You have unsaved expense modifications, please save changes first...")
        return

    exit(0)

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
        print("No prior records found...")

    print("=-="*21)
    print("NEW-EXPENSES")
    print("=-="*21)

    for date, expense_name, category, expenditure in NEW_EXPENSES:
        print(f"{date} | \t{expense_name} | \t{category} -> ₹{expenditure}")
    # end-for

    if not NEW_EXPENSES:
        # If expenses are empty then let the user know
        print("No prior records found...")

    return

def write_to_csv():
    """To write all the data to a csv file."""

    # If the new-expenses aren't empty, then ask user to save first
    if NEW_EXPENSES:
        print("Expenses are modified, please save expenses first...")
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
        print("Nothing to modify, no new expenses...")
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
    print("All expenses recorded successfully!")
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

def view_commands():
    """Shows all the valid commands and their corresponding functions."""
    global COMMANDS
    for key, command in COMMANDS.items():
        print(f"{key} : {command.__doc__}")
    # end-for

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
    'c': write_to_csv,
    's': save_to_db,
    'i': insert_record,
    'h': view_commands,
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