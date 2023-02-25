"""
To store the content in a database
"""
import sqlite3

# Open a connection to the database
conn = sqlite3.connect("./database/expenses.db")

# Create a cursor object
cursor = conn.cursor()

# Create the required table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    expense_date VARCHAR(15) NOT NULL,
    expense_name VARCHAR(255) NOT NULL,
    expenditure INTEGER NOT NULL
)
""")


def load_previous_data() -> list:
    """
    Loads the previous data to a list
    """
    cursor.execute("""
    SELECT * FROM expenses
    """)
    return cursor.fetchall()


def insert_record(expense):
    """
    Inserts the expense in the table
    """
    expense_date, expense_name, expenditure = expense
    # Validate the data
    if not isinstance(expense_date, str):
        raise TypeError(f"Required 'str' type for 'expense_date', got '{expense_date.__class__} instead'")
    if not isinstance(expense_name, str):
        raise TypeError(f"Required 'str' type for 'expense_name', got '{expense_name.__class__} instead'")
    if not isinstance(expenditure, (float, int)):
        raise TypeError(f"Required 'int/float' type for 'expenditure' got '{expenditure.__class__}' instead")

    # Insert the value to the table
    cursor.execute(f"""
    INSERT INTO expenses VALUES ("{expense_date}", "{expense_name}", {expenditure})
    """)

    # If everything went successful, then commit the changes
    conn.commit()
