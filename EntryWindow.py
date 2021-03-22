import tkinter as tk
from tkinter import messagebox


class EntryWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.entry_start_point = None
        self.entry_end_point = None
        self.entry_start_row = 0
        self.entry_start_column = 0
        self.entry_end_row = 0
        self.entry_end_column = 0
        self.configure_gui()
        self.create_widgets()
        self.position_window()

    def configure_gui(self):
        self.title('Path Finding')
        self.resizable(False, False)

    def create_widgets(self):
        self.create_labels()
        self.create_entry_widgets()
        self.create_submit_button()

    def create_labels(self):
        label_start_point = tk.Label(master=self, text="Start point (row,column):")
        label_end_point = tk.Label(master=self, text="End point (row,column):")
        label_start_point.grid(row=0, column=0, padx=5, pady=10)
        label_end_point.grid(row=1, column=0, padx=5, pady=10)

    def create_entry_widgets(self):
        self.entry_start_point = tk.Entry(master=self, width=15)
        self.entry_end_point = tk.Entry(master=self, width=15)
        self.entry_start_point.grid(row=0, column=1, padx=5)
        self.entry_end_point.grid(row=1, column=1, padx=5)

    def create_submit_button(self):
        button_submit = tk.Button(master=self, text="Submit", command=self.submit)
        button_submit.grid(columnspan=2, row=2, pady=5)

    def position_window(self):
        self.update()
        window_width, window_height = [int(item) for item in self.geometry().split("+")[0].split("x")]
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        window_position_x = screen_width / 2 - window_width / 2
        window_position_y = screen_height / 2 - window_height / 2
        self.geometry(f"+{int(window_position_x)}+{int(window_position_y)}")

    def submit(self):
        try:
            self.entry_start_row, self.entry_start_column = [int(item) for item in self.entry_start_point.get().split(',')]
            self.entry_end_row, self.entry_end_column = [int(item) for item in self.entry_end_point.get().split(',')]
            self.destroy()
        except ValueError:
            self.show_message()

    @staticmethod
    def show_message():
        messagebox.showinfo("Path Finding", "Please enter start and end points")
