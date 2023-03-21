"""
This is the GUI version of budget maker
"""
import tkinter as tk
from tkinter import ttk
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
        subWindow = tk.Toplevel(self.master, height=400)
        subWindow.resizable(False, False)
        subWindow.title("View Records")

        infoPanel = tk.Frame(subWindow, width=150)
        infoPanel.pack(side='left', expand='yes')

        recordPanel = tk.Frame(subWindow, width=200)
        recordPanel.pack(side='left', expand='yes')

        recordListBox = tk.Listbox(recordPanel, selectmode='browse')
        recordListBox.pack(side='left')
        # Add a slider for the records box
        recordScroll = ttk.Scrollbar(recordPanel)
        recordScroll.pack(side='left')


        """ Select a date """
        tk.Label(infoPanel, text='Select a date', **GUIstyle['label']) \
        .grid(row=0, column=0, padx=20, pady=20)





if __name__ == '__main__':

    app = App(master=tk.Tk())
    app.run()