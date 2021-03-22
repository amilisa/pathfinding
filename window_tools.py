import pygame
from tkinter import messagebox
import tkinter as tk


def show_message(message):
    root = tk.Tk()
    root.withdraw()
    answer = messagebox.askyesno("Path Finding", f"{message}\nWould you like to restart the program?")
    root.destroy()
    return answer


def create_main_window(width, height, background_color, caption):
    main_window = pygame.display.set_mode((width, height))
    main_window.fill(background_color)
    pygame.display.set_caption(caption)
    return main_window
