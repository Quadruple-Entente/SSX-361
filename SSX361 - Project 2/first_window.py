
from tkinter import *
from navHandler import NavigationHandler
from tkinter import ttk, messagebox
import re



class FirstWindow:

    def __init__(self, master):
        self.master = master
        self.nav_handler = NavigationHandler
        self.master.title("WELCOME TO BELGIUM CAMPUS STUDENT & LECTURER MANAGEMENT SYSTEM")
        self.master.geometry('400x300')

        self.create_form()

    def create_form(self):
        Label(self.master, text="Please select what you are logging in as:" , font =('Arial', 16, 'bold' )).pack(pady=20)

        Button(self.master, text="Lecturer", command=self.lecturer).pack(pady=20) #button for lecturer login
        Button(self.master, text="Student", command=self.student).pack(pady=20)



    def student(self):
       self.nav_handler.nav_to_second_window(self.master)



    def lecturer(self):
        messagebox.showinfo("Login", "Login functionality to be implemented")

if __name__ == "__main__":
   master =Tk()









