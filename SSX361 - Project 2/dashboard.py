from tkinter import *
from tkinter import ttk, messagebox
from navHandler import NavigationHandler




class StudentDashboard:
    def __init__(self, master):
        self.master = master
        self.nav_handler = NavigationHandler
        self.master.title("STUDENT DASHBOARD")
        self.master.geometry('1000x600')
        self.main_frame = Frame(master)
        self.main_frame.pack(fill=BOTH, expand=True, padx=20, pady=20)


        title = Label(self.main_frame, text="STUDENT DASHBOARD", font=('Arial', 20, 'bold'))
        title.pack(pady=20)


        self.button_frame = Frame(self.main_frame)
        self.button_frame.pack(pady=20)


        self.create_buttons()


        self.table_frame = Frame(self.main_frame)
        self.table_frame.pack(fill=BOTH, expand=True)


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

        self.clear_frames()


        self.marks_frame = Frame(self.table_frame)
        self.marks_frame.pack(fill=BOTH, expand=True)


        columns = ('Module Code', 'Module Name', 'Lecturer', 'Marks')
        tree = ttk.Treeview(self.marks_frame, columns=columns, show='headings')


        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)


        sample_data = [
            ('CSC101', 'Introduction to Programming', 'Dr. Smith', '85'),
            ('MAT201', 'Advanced Mathematics', 'Prof. Johnson', '78'),
            ('PHY301', 'Physics Fundamentals', 'Dr. Brown', '92'),
            ('ENG401', 'Technical Writing', 'Ms. Davis', '88'),
        ]

        for item in sample_data:
            tree.insert('', END, values=item)



        scrollbar = ttk.Scrollbar(self.marks_frame, orient=VERTICAL, command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)


        tree.pack(side=LEFT, fill=BOTH, expand=True)
        scrollbar.pack(side=RIGHT, fill=Y)

    def show_add_module(self):

        self.clear_frames()


        self.add_module_frame = Frame(self.table_frame)
        self.add_module_frame.pack(fill=BOTH, expand=True, pady=20)


        Label(self.add_module_frame, text="Add New Module", font=('Arial', 14, 'bold')).pack(pady=10)


        Label(self.add_module_frame, text="Module Code:").pack()
        code_entry = Entry(self.add_module_frame)
        code_entry.pack(pady=5)


        Label(self.add_module_frame, text="Module Name:").pack()
        name_entry = Entry(self.add_module_frame)
        name_entry.pack(pady=5)


        Label(self.add_module_frame, text="Lecturer:").pack()
        lecturer_entry = Entry(self.add_module_frame)
        lecturer_entry.pack(pady=5)


        submit_btn = Button(self.add_module_frame, text="Add Module",
                            command=lambda: self.submit_module(code_entry.get(), name_entry.get(),
                                                               lecturer_entry.get()),
                            bg='#2196F3', fg='white')
        submit_btn.pack(pady=20)

    def update_info(self):
        self.nav_handler.nav_to_reg(self.master)



    def delete_module(self):
        messagebox.showwarning("Delete Module",
                               "Please contact the administration office to delete modules.\n\n" +
                               "Email: admin@belgiumcampus.com\nPhone: (123) 456-7890")

    def submit_module(self, code, name, lecturer):
        if not all([code, name, lecturer]):
            messagebox.showerror("Error", "All fields are required!")
            return

        messagebox.showinfo("Success", f"Module {code} has been added successfully!")
        self.show_marks()  # Refresh the marks view

    def clear_frames(self):

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
