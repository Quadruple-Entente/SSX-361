from tkinter import *
from navHandler import NavigationHandler

from tkinter import ttk, messagebox
import re


class SecondWindow:

    def __init__(self, master):
        self.master = master
        self.nav_handler = NavigationHandler
        self.master.title("WELCOME TO BELGIUM CAMPUS STUDENT!")
        self.master.geometry('400x300')

        self.create_form()

    def create_form(self):
        Label(self.master, text="Please select what you are logging in as:", font=('Arial', 16, 'bold')).pack(pady=20)

        Button(self.master, text="Existing Student", command=self.estudent).pack(pady=20)  # button for lecturer login
        Button(self.master, text="New Student", command=self.nstudent).pack(pady=20)

    def nstudent(self):
        self.nav_handler.nav_to_reg(self.master)

    def estudent(self):
       self.nav_handler.nav_to_login(self.master)


if __name__ == "__main__":
    master = Tk()


