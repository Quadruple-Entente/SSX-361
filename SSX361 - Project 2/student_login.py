from tkinter import *
from navHandler import NavigationHandler




from tkinter import ttk, messagebox
import re

class LoginForm:
    def __init__(self, master):
        self.master = master
        self.nav_handler = NavigationHandler
        self.master.title("Student Login")
        self.master.geometry('400x300')

        # Variables
        self.student_id_var = StringVar()
        self.password_var = StringVar()

        # Create form
        self.create_form()

    def create_form(self):
        # Title
        Label(self.master, text="STUDENT LOGIN", font=('Arial', 16, 'bold')).pack(pady=20)

        # Student ID
        Label(self.master, text="Student ID:").pack(pady=5)
        Entry(self.master, textvariable=self.student_id_var).pack(pady=5)

        # Password
        Label(self.master, text="Password:").pack(pady=5)
        Entry(self.master, textvariable=self.password_var, show="*").pack(pady=5)

        # Login Button
        Button(self.master, text="Login", command=self.login).pack(pady=20)

    def login(self):
        self.nav_handler.nav_to_dash(self.master)

if __name__ == "__main__":
    master = Tk()
    app = LoginForm(master)
    master.mainloop()