from tkinter import *
from tkinter import ttk, messagebox

class NavigationHandler:
    def __init__(self):
        self.curr_Window = None
        self.user_data = {}

    def start(self):
        root = Tk()
        from first_window import FirstWindow
        self.curr_Window = FirstWindow(root)
        root.mainloop()

    def nav_to_second_window(self, current_master):
        current_master.destroy()
        from second_window import SecondWindow
        new_master = Tk()
        self.curr_Window = SecondWindow(new_master)
        new_master.mainloop()

    def nav_to_reg(self, current_master):
        current_master.destroy()
        from student_registration import StudentRegistrationForm
        new_master =Tk()
        self.curr_Window = StudentRegistrationForm(new_master)
        new_master.mainloop()

    def nav_to_login(self, current_master):
        current_master.destroy()
        from student_login import LoginForm
        new_master = Tk()
        self.curr_Window = LoginForm(new_master)
        new_master.mainloop()

    def nav_to_dash(self, current_master):
        current_master.destroy()
        from dashboard import StudentDashboard
        new_master =Tk()
        self.curr_Window = StudentDashboard(new_master)
        new_master.mainloop()

    def return_to_first_window(self, current_master):
        current_master.destroy()
        from first_window import FirstWindow
        new_master = Tk()
        self.curr_Window = FirstWindow(new_master)
        new_master.mainloop()


if __name__ == "__main__":
    NavigationHandler()



