"""
This is the GUI version of budget maker
"""
import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import datetime
from main import *
from src.constants import *

class App(ctk.CTk):
    """
    This is the class to implement money-manager in GUI

    Attributes:
        master (tk.Tk): The master window for all the widgets
    """

    def __init__(self):
        """
        The constructor for the class

        Attributes:
            master (tk.Tk): The master window for all the widgets

        """
        # Initialize the window
        super().__init__()

        # Tkinter variables

        # Configure the master
        self.title(APP_TITLE)
        self.resizable(*RESIZABLE)
    
        """
        Contains the layout of the application
        """
        topFrame = ctk.CTkFrame(self)
        topFrame.pack(side='top', fill='both')

        infoPanel = ctk.CTkFrame(topFrame)
        infoPanel.pack(side='left')

        recordPanel = ctk.CTkFrame(topFrame, width=400)
        recordPanel.pack(side='left')

        # Add a treeview
        recordTreeviewWidget = ttk.Treeview(recordPanel)
        recordTreeviewWidget['columns'] = ("Name", "Category", "Expenditure")

        # Configure the columns
        recordTreeviewWidget.column("#0", width=120, minwidth=25)
        recordTreeviewWidget.column("Name", anchor=tk.W, minwidth=75)
        recordTreeviewWidget.column("Category", anchor=tk.CENTER, minwidth=75)
        recordTreeviewWidget.column("Expenditure", anchor=tk.W, minwidth=75)

        # Configure the headings
        recordTreeviewWidget.heading("#0", text="0", anchor=tk.W)
        recordTreeviewWidget.heading("Name", text="Expense Name", anchor=tk.CENTER)
        recordTreeviewWidget.heading("Category", text="Expense Category", anchor=tk.CENTER)
        recordTreeviewWidget.heading("Expenditure", text="Expenditure", anchor=tk.CENTER)
        recordTreeviewWidget.pack(side='left', fill='both', expand='yes')

        # Add a slider for the records box
        recordScroll = ctk.CTkScrollbar(recordPanel)
        recordScroll.pack(side='left', fill='y')

        # For managing the row and column 
        __row = 0; __column = 0

        """ Select a date """
        ctk.CTkLabel(infoPanel, text='Select a date', **GUIstyle['label-width-small']) \
        .grid(row=__row, column=__column, padx=10, pady=10); __row += 1

        # Fetch today's date
        today = datetime.datetime.today()
        # The calendar widget
        # self.calendarWidget = Calendar(infoPanel, selectmode='day', 
        #                           year=today.year, 
        #                           month=today.month, 
        #                           day=today.day)
        # self.calendarWidget.grid(row=1, column=0, padx=10, pady=10)
        
        # Button to initiate the process
        ctk.CTkButton(infoPanel, text='Get information', **GUIstyle['button'], command=self.functionViewDateRecord) \
        .grid(row=__row, column=0, padx=10, pady=10); __row += 1

        # Button to view all the records
        ctk.CTkButton(infoPanel, text='View all records', **GUIstyle['button'], command=self.functionViewAllRecords) \
        .grid(row=__row, column=0, padx=10, pady=10); __row += 1


    
    """
    Our utility functions
    """
    def functionViewAllRecords(self) -> None:
        """
        The function to view all the records
        """

        # Fetch all the previous records and sort them by date
        expense_record = db_handler.date_grouped_records()

        topLevel = ctk.CTkToplevel(self)
        topLevel.title("Expense History")

        # Add scrollable frame
        frame = ctk.CTkScrollableFrame(topLevel, label_text="Expense History")
        frame.pack(side='top', expand='yes', fill='both')
        # Add new frames containing the information on expense

        for record_date in expense_record:

            # Add specific frame for the expenses
            recordFrame = ctk.CTkFrame(frame, **GUIstyle['bordered-frame'])
            recordFrame.pack(side='top', padx=10, pady=20, fill='both')

            # Fetch the record detail for that day
            date_record = expense_record[record_date]
            record_field_num = len(date_record[0])

            # Add a title to the frame
            ctk.CTkLabel(recordFrame, text=record_date, font=ctk.CTkFont(size=20, weight="bold")) \
            .grid(row=0, columnspan=record_field_num, padx=2, pady=5)

            # Add records using grid manager
            for i, record in enumerate(date_record):
                # This all information will be in same row
                for j, record_field in enumerate(record):
                    # Skip adding the date again
                    if j == 0: continue
                    # Add everything else on the screen  
                    ctk.CTkLabel(recordFrame, text=str(record_field), font=ctk.CTkFont(family="Gotham", size=12)) \
                    .grid(row=i+1, column=j, padx=5, pady=3)

            


            


    def functionAddRecord(self) -> None:
        pass

    
    def functionViewRecords(self) -> None:
        """
        The function to view previous records
        """
        

    def functionViewDateRecord(self) -> None:
        """
        Fetches today's date and show the expenses for the day in listbox
        """
        # Fetch the date from the calendar
        date = datetime.datetime.strptime(
            self.calendarWidget.get_date(),
            "%m/%d/%y"
        )
        # Change the format of the date to match the one in database
        database_formatted_date = datetime.datetime.strftime(date, "%b-%d-%Y")
    
        # Request the data for this date from the database
        date_records = db_handler.records_with_date(database_formatted_date)

        print(date_records)
        


if __name__ == '__main__':

    app = App()
    app.mainloop()