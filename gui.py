"""
This is the GUI version of budget maker
"""
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import datetime
from main import *
from src.constants import *

class App:
    """
    This is the class to implement money-manager in GUI

    Attributes:
        master (tk.Tk): The master window for all the widgets
    """

    def __init__(self, master:tk.Tk):
        """
        The constructor for the class

        Attributes:
            master (tk.Tk): The master window for all the widgets

        """
        # Tkinter variables

        # Configure the master
        master.title(APP_TITLE)
        master.resizable(*RESIZABLE)

        self.master = master
        self.__layout()
    

    def __layout(self) -> None:
        """
        Contains the layout of the application
        """
        master = self.master

        leftFrame = tk.Frame(master, width=200)
        leftFrame.pack(side='left')

        rightFrame = tk.Frame(master, width=300)
        rightFrame.pack(side='left')

        # Buttons to view and add records
        tk.Button(leftFrame, text='Add Record', command=self.functionAddRecord, **GUIstyle['button'])  \
        .pack(side='top', padx=20, pady=20)

        tk.Button(leftFrame, text='View Records', command=self.functionViewRecords, **GUIstyle['button']) \
        .pack(side='top', padx=20, pady=20)

    
    def run(self) -> None:
        """
        This function initializes the window
        """
        self.master.mainloop()

    
    """
    Our utility functions
    """
    def functionAddRecord(self) -> None:
        pass

    
    def functionViewRecords(self) -> None:
        """
        The function to view previous records
        """
        subWindow = tk.Toplevel(self.master)
        subWindow.resizable(False, False)
        subWindow.title("View Records")

        infoPanel = tk.Frame(subWindow)
        infoPanel.pack(side='left', expand='no')

        recordPanel = tk.Frame(subWindow, width=400)
        recordPanel.pack(side='left')

        recordListBox = tk.Listbox(recordPanel, selectmode='browse')
        recordListBox.pack(side='left', fill='both')
        # Add a slider for the records box
        recordScroll = ttk.Scrollbar(recordPanel)
        recordScroll.pack(side='left', fill='y')


        """ Select a date """
        tk.Label(infoPanel, text='Select a date', **GUIstyle['label-width-small']) \
        .grid(row=0, column=0, padx=10, pady=10)

        # Fetch today's date
        today = datetime.datetime.today()
        # The calendar widget
        self.calendarWidget = Calendar(infoPanel, selectmode='day', 
                                  year=today.year, 
                                  month=today.month, 
                                  day=today.day)
        self.calendarWidget.grid(row=1, column=0, padx=10, pady=10)
        
        # Button to initiate the process
        tk.Button(infoPanel, text='Get information', **GUIstyle['button'], command=self.functionViewDateRecord) \
        .grid(row=2, column=0, padx=10, pady=10)


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
        print(database_formatted_date)

        # Request the data for this date from the database
        date_records = db_handler.records_with_date(database_formatted_date)

        print(date_records)
        


if __name__ == '__main__':

    app = App(master=tk.Tk())
    app.run()