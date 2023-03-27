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
        infoPanel.pack(side='left', expand='no')

        recordPanel = ctk.CTkFrame(topFrame, width=400)
        recordPanel.pack(side='left', expand='yes')

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

        """ Select a date """
        ctk.CTkLabel(infoPanel, text='Select a date', **GUIstyle['label-width-small']) \
        .grid(row=0, column=0, padx=10, pady=10)

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
        .grid(row=2, column=0, padx=10, pady=10)


        # Bottom frame for more widgets
        bottomFrame = ctk.CTkFrame(self)
        bottomFrame.pack(side='top', fill='both')

        # To add 

    
    """
    Our utility functions
    """
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