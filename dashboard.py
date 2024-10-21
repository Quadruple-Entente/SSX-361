from tkinter import *
from tkinter import ttk, messagebox





class StudentDashboard:
    def __init__(self, window):
        self.window = window
        self.window.title("STUDENT DASHBOARD")

        self.window.geometry('1000x600')

        # Create main frame
        self.main_frame = Frame(window)
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)

        # Title
        title = Label(self.main_frame, text="STUDENT DASHBOARD", font=('Arial', 20, 'bold'))
        title.pack(pady=20)

        # Buttons frame
        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(pady=20)

        # Create buttons
        self.create_buttons()

        # Create table frame
        self.table_frame = Frame(self.main_frame)
        self.table_frame.pack(fill=BOTH, expand=True)

        # Initially hide all frames
        self.marks_frame = None
        self.add_module_frame = None

    def create_buttons(self):
        # View Marks Button
        view_btn = Button(self.button_frame, text="View Marks", command=self.show_marks,
                          width=15, height=2, bg='#4CAF50', fg='white')
        view_btn.pack(side=LEFT, padx=10)

        # Add Module Button
        add_btn = Button(self.button_frame, text="Add Module", command=self.show_add_module,
                         width=15, height=2, bg='#2196F3', fg='white')
        add_btn.pack(side=LEFT, padx=10)

        # Update Info Button
        update_btn = Button(self.button_frame, text="Update Information", command=self.update_info,
                            width=15, height=2, bg='#FFC107', fg='black')
        update_btn.pack(side=LEFT, padx=10)

        # Delete Module Button
        delete_btn = Button(self.button_frame, text="Delete Module", command=self.delete_module,
                            width=15, height=2, bg='#f44336', fg='white')
        delete_btn.pack(side=LEFT, padx=10)

    def show_marks(self):
        # Clear any existing frames
        self.clear_frames()

        # Create marks frame
        self.marks_frame = Frame(self.table_frame)
        self.marks_frame.pack(fill=BOTH, expand=True)

        # Create Treeview
        columns = ('Module Code', 'Module Name', 'Lecturer', 'Marks')
        tree = ttk.Treeview(self.marks_frame, columns=columns, show='headings')

        # Set column headings
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)

        # Sample data - in real application, this would come from a database
        sample_data = [
            ('CSC101', 'Introduction to Programming', 'Dr. Smith', '85'),
            ('MAT201', 'Advanced Mathematics', 'Prof. Johnson', '78'),
            ('PHY301', 'Physics Fundamentals', 'Dr. Brown', '92'),
            ('ENG401', 'Technical Writing', 'Ms. Davis', '88'),
        ]

        # Insert sample data
        for item in sample_data:
            tree.insert('', END, values=item)

        # Add scrollbar
        scrollbar = ttk.Scrollbar(self.marks_frame, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        # Pack the treeview and scrollbar
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

    def show_add_module(self):
        # Clear any existing frames
        self.clear_frames()

        # Create add module frame
        self.add_module_frame = Frame(self.table_frame)
        self.add_module_frame.pack(fill=BOTH, expand=True, pady=20)

        # Add module form
        Label(self.add_module_frame, text="Add New Module", font=('Arial', 14, 'bold')).pack(pady=10)

        # Module Code
        Label(self.add_module_frame, text="Module Code:").pack()
        code_entry = Entry(self.add_module_frame)
        code_entry.pack(pady=5)

        # Module Name
        Label(self.add_module_frame, text="Module Name:").pack()
        name_entry = Entry(self.add_module_frame)
        name_entry.pack(pady=5)

        # Lecturer
        Label(self.add_module_frame, text="Lecturer:").pack()
        lecturer_entry = Entry(self.add_module_frame)
        lecturer_entry.pack(pady=5)

        # Submit button
        submit_btn = Button(self.add_module_frame, text="Add Module",
                            command=lambda: self.submit_module(code_entry.get(), name_entry.get(),
                                                               lecturer_entry.get()),
                            bg='#2196F3', fg='white')
        submit_btn.pack(pady=20)

    def update_info(self):
        # Create a new top-level window
        update_window = Toplevel(self.window)
        # Create the registration form in the new window
        registration_form = StudentRegistrationForm(update_window)




    def delete_module(self):
        messagebox.showwarning("Delete Module",
                               "Please contact the administration office to delete modules.\n\n" +
                               "Email: admin@university.com\nPhone: (123) 456-7890")

    def submit_module(self, code, name, lecturer):
        if not all([code, name, lecturer]):
            messagebox.showerror("Error", "All fields are required!")
            return

        messagebox.showinfo("Success", f"Module {code} has been added successfully!")
        self.show_marks()  # Refresh the marks view

    def clear_frames(self):
        # Clear any existing frames in table_frame
        if self.marks_frame:
            self.marks_frame.destroy()
        if self.add_module_frame:
            self.add_module_frame.destroy()


def main():
    window = Tk()
    dashboard = StudentDashboard(window)
    window.mainloop()


if __name__ == "__main__":
    main()
