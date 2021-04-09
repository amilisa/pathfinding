import tkinter as tk
from tkinter import messagebox, ttk


class EntryWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.entry_start_point = None
        self.entry_end_point = None
        self.entry_start_row = 0
        self.entry_start_column = 0
        self.entry_end_row = 0
        self.entry_end_column = 0
        self.combobox = ttk.Combobox(master=self, width=18, state='readonly')
        self.selected_algorithm = None
        self.configure_gui()
        self.create_widgets()
        self.position_window()

    def configure_gui(self):
        self.title('Path Finding')
        self.resizable(False, False)

    def create_widgets(self):
        self.create_labels()
        self.create_entry_widgets()
        self.configure_combobox()
        self.create_submit_button()

    def create_labels(self):
        label_start_point = tk.Label(master=self, text="Start point (row,column):")
        label_end_point = tk.Label(master=self, text="End point (row,column):")
        label_selection = tk.Label(master=self, text="Select an algorithm:")
        label_start_point.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        label_end_point.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        label_selection.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)

    def create_entry_widgets(self):
        self.entry_start_point = tk.Entry(master=self, width=18)
        self.entry_end_point = tk.Entry(master=self, width=18)
        self.entry_start_point.grid(row=0, column=1, padx=3, sticky=tk.W)
        self.entry_end_point.grid(row=1, column=1, padx=3, sticky=tk.W)

    def configure_combobox(self):
        algorithms = ("Breadth-first Search", "Dijkstra's Algorithm")
        self.combobox['values'] = algorithms
        self.combobox.current(0)
        self.combobox.grid(row=2, column=1, padx=3, sticky=tk.W)

    def create_submit_button(self):
        button_submit = tk.Button(master=self, text="Submit", command=self.submit)
        button_submit.grid(columnspan=2, row=3, pady=5)

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
            self.selected_algorithm = self.combobox.get()
            self.destroy()
        except ValueError:
            self.show_message()

    @staticmethod
    def show_message():
        messagebox.showinfo("Path Finding", "Please enter the correct start and end values.")
