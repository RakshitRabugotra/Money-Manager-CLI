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

def run_query(query: str) -> list:
    """
    Runs the SQL query in the database
        Parameters:
            query (str): The SQL query to run
        
        Returns:
            the records matching the query
    """
    cursor.execute(query)
    return cursor.fetchall()


def records_with_date(date: str) -> list:
    """
    Returns all the records matching the given date
        Parameters:
            date (str): The date to search for in '%b-%d-%Y' format
        
        Returns:
            the records matching the date
    """
    return run_query(f"""
    SELECT * FROM expenses WHERE expense_date LIKE '{date}'
    """)
    

def load_previous_data() -> list:
    """
    Loads the previous data to a list
        Returns: All the records in the database
    """
    return run_query("""
    SELECT * FROM expenses
    """)


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
