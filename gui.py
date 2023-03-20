"""
This is the GUI version of budget maker
"""
import tkinter as tk
from main import *

class App:
    def __init__(self, master:tk.Tk):

        self.master = master
    
    def run(self) -> None:
        self.master.mainloop()


if __name__ == '__main__':

    app = App()
    app.run()