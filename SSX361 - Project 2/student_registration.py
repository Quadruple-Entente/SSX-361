from tkinter import *
from tkinter import ttk, messagebox
from navHandler import NavigationHandler
import re
import random  # Add this import
import string  # Add this import





class StudentRegistrationForm:
    def __init__(self, master):
        self.master = master
        self.nav_handler = NavigationHandler
        self.master.title("STUDENT REGISTRATION FORM")
        self.master.geometry('850x700')

        # Variables for storing form data
        self.fname_var = StringVar()
        self.lname_var = StringVar()
        self.email_var = StringVar()
        self.mobile_var = StringVar()
        self.address_var = StringVar()
        self.password_var = StringVar()
        self.gender_var = IntVar()
        self.course_var = IntVar()
        self.day = StringVar()
        self.month = StringVar()
        self.year = StringVar()

        self.create_form()

    def create_form(self):
        # Labels
        Label(self.master, text="FIRST NAME ").grid(row=0, column=0, pady=5, padx=5, sticky="e")
        Label(self.master, text="LAST NAME ").grid(row=1, column=0, pady=5, padx=5, sticky="e")
        Label(self.master, text="DATE OF BIRTH ").grid(row=2, column=0, pady=5, padx=5, sticky="e")
        Label(self.master, text="EMAIL ID ").grid(row=3, column=0, pady=5, padx=5, sticky="e")
        Label(self.master, text="MOBILE NUMBER ").grid(row=4, column=0, pady=5, padx=5, sticky="e")
        Label(self.master, text="GENDER ").grid(row=5, column=0, pady=5, padx=5, sticky="e")
        Label(self.master, text="ADDRESS ").grid(row=7, column=0, pady=5, padx=5, sticky="ne" )
        Label(self.master, text="PASSWORD ").grid(row=8, column=0, pady=5, padx=5, sticky="e")

        Label(self.master, text="COURSES APPLIED FOR ").grid(row=9, column=0, pady=5, padx=5, sticky="e")

        # Entry fields
        Entry(self.master, textvariable=self.fname_var).grid(row=0, column=1, padx=5, pady=5, sticky="w")
        Entry(self.master, textvariable=self.lname_var).grid(row=1, column=1, padx=5, pady=5, sticky="w")

        # Date of Birth Combo boxes
        day_cb = ttk.Combobox(self.master, width=3, textvariable=self.day)
        day_cb.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        day_cb['values'] = tuple(str(i).zfill(2) for i in range(1, 32))


        month_cb = ttk.Combobox(self.master, width=10, textvariable=self.month)
        month_cb.grid(row=2, column=1, padx=5, pady=5, sticky="e")
        month_cb['values'] = ('January', 'February', 'March', 'April', 'May', 'June',
                              'July', 'August', 'September', 'October', 'November', 'December')


        year_cb = ttk.Combobox(self.master, width=5, textvariable=self.year)
        year_cb.grid(row=2, column=1, padx=5, pady=5)
        year_cb['values'] = tuple(range(1990, 2022))


        # Email and Mobile
        Entry(self.master, textvariable=self.email_var).grid(row=3, column=1, padx=5, pady=5, sticky="w")
        mobile_entry = Entry(self.master, textvariable=self.mobile_var)
        mobile_entry.grid(row=4, column=1, sticky="w")
        Label(self.master, text="(10 digit number)").grid(row=4, column=1)

        # Gender Radio Buttons
        Radiobutton(self.master, text="Male", variable=self.gender_var, value=1).grid(row=5, column=1, sticky="w")
        Radiobutton(self.master, text="Female", variable=self.gender_var, value=2).grid(row=6, column=1, sticky="w")

        # Address and Password
        Entry(self.master, textvariable=self.address_var).grid(row=7, column=1, padx=5, pady=5, sticky="w")
        Entry(self.master, textvariable=self.password_var, show="*").grid(row=8, column=1,padx=5, pady=5, sticky="w")

        # Course Selection Radio Buttons
        courses = [
            "Diploma in Information Technology",
            "Bachelor of Computer Science",
            "Bachelor of Information Technology",
            "Diploma in Information Technology (For Deaf Students)",
            "National Certificate: IT System Development",
            "National Certificate: IT Database Development"
        ]

        for i, course in enumerate(courses):
            Radiobutton(self.master, text=course, variable=self.course_var,
                        value=i + 1).grid(row=9 + i, column=1, sticky="w", padx=5, pady=2)

        # Buttons
        Button(self.master, text="SUBMIT", command=self.submit_form).grid(row=32, column=8, pady=20)
        Button(self.master, text="UPDATE", command=self.reset_form).grid(row=32, column=9, pady=20)

    def validate_mobile(self, mobile):
        return len(mobile) == 10 and mobile.isdigit()

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)

    def validate_password(self, password):
        return len(password) == 6

    def submit_form(self):
        # Get all form values
        fname = self.fname_var.get().strip()
        lname = self.lname_var.get().strip()
        email = self.email_var.get().strip()
        mobile = self.mobile_var.get().strip()
        password = self.password_var.get()

        # Validation
        if not all([fname, lname, email, mobile, password, self.day.get(),
                    self.month.get(), self.year.get(), self.gender_var.get(),
                    self.course_var.get()]):
            messagebox.showerror("Error", "All fields are required!")
            return

        if not self.validate_email(email):
            messagebox.showerror("Error", "Invalid email format!")
            return

        if not self.validate_mobile(mobile):
            messagebox.showerror("Error", "Mobile number must be 10 digits!")
            return

        if not self.validate_password(password):
            messagebox.showerror("Error", "Password must be 6 characters!")
            return

        # Generate student ID
        student_id = ''.join(random.choices(string.digits, k=8))

        # Create custom message box
        result = Toplevel(self.master)
        result.title("Registration Successful")
        result.geometry("300x200")
        result.transient(self.master)  # Make window modal
        result.grab_set()  # Make window modal

        # Center the window
        result.geometry("+%d+%d" % (self.master.winfo_rootx() + 50,
                                    self.master.winfo_rooty() + 50))

        # Add messages
        Label(result, text="Registration Successful!", font=('Arial', 12, 'bold')).pack(pady=10)
        Label(result, text=f"Your Student ID: {student_id}").pack(pady=5)
        Label(result, text=f"Your Password: {password}").pack(pady=5)
        Label(result, text="Please save these credentials").pack(pady=5)

        def ok_pressed():
            self.nav_handler.nav_to_login(self.master)

        # Add OK button
        Button(result, text="OK", command=ok_pressed).pack(pady=20)



    def reset_form(self):
        # Clear all form fields
        self.fname_var.set("")
        self.lname_var.set("")
        self.email_var.set("")
        self.mobile_var.set("")
        self.address_var.set("")
        self.password_var.set("")
        self.gender_var.set(0)
        self.course_var.set(0)
        self.day.set("")
        self.month.set("")
        self.year.set("")


if __name__ == "__main__":
    master = Tk()
    app = StudentRegistrationForm(master)
    master.mainloop()
