import tkinter
from tkinter import ttk


userValid = tkinter.Tk()
userValid.title("MedTrack")

frame = tkinter.Frame(userValid)
frame.pack()

title_Frame = tkinter.LabelFrame(frame, text = "MedTrack Sign-In")
title_Frame.grid(row = 0, column = 0, sticky = "news", padx = 25, pady = 25)

userName_label = tkinter.Label(title_Frame, text = "Username")
userName_label.grid(row = 1, column = 0)

password_label = tkinter.Label(title_Frame, text = "Password")
password_label.grid(row = 3, column = 0)

userName_entry = tkinter.Entry(title_Frame)
userName_entry.grid(row = 2, column = 0)

password_entry = tkinter.Entry(title_Frame)
password_entry.grid(row = 4, column = 0)

for widget in title_Frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)
