import tkinter
from tkinter import ttk


def enter_data():
    nameLast = nameLast_entry.get()
    nameFirst = nameFirst_entry.get()


mainWindow = tkinter.Tk()
mainWindow.title("MedTrack")


# Main window frame
frame = tkinter.Frame(mainWindow)
frame.pack()

# Frame 1
title_frame = tkinter.LabelFrame(frame, text = "MedTrack")
title_frame.grid(row = 0, column = 0, sticky = "news", padx = 25, pady = 25)

purpose_label = tkinter.Label(title_frame, text = "MedTrack is used to keep track of your or someone else's medications.")
purpose_label.grid(row = 1, column = 0)

for widget in title_frame.winfo_children():
    widget.grid_configure(padx = 15, pady = 15)

# Frame 2

user_info_frame = tkinter.LabelFrame(frame, text = "User Information")
user_info_frame.grid(row = 2, column = 0, padx = 25, pady = 25)

nameLast_label = tkinter.Label(user_info_frame, text = "Last Name")
nameLast_label.grid(row = 2, column = 0)       
nameFirst_label = tkinter.Label(user_info_frame, text = "First Name")
nameFirst_label.grid(row = 2, column = 1) 

nameLast_entry = tkinter.Entry(user_info_frame)
nameFirst_entry = tkinter.Entry(user_info_frame) 
nameLast_entry.grid(row = 3, column = 0)
nameFirst_entry.grid(row = 3, column = 1)  

date_label = tkinter.Label(user_info_frame, text = "Date")
date_label.grid(row = 4, column = 0)

dateMonth_label = tkinter.Label(user_info_frame, text = "Month")
dateMonth_label.grid(row = 5, column = 0)
dateMonth_spinbox = tkinter.Spinbox(user_info_frame, from_ = 1, to = 12)
dateMonth_spinbox.grid(row = 6, column =0)

dateDay_label = tkinter.Label(user_info_frame, text = "Day")
dateDay_label.grid(row = 5, column = 1)
dateDay_spinbox = tkinter.Spinbox(user_info_frame, from_ = 1, to = 31)
dateDay_spinbox.grid(row = 6, column = 1)

dateYear_label = tkinter.Label(user_info_frame, text = "Year")
dateYear_label.grid(row = 5, column = 2)
dateYear_spinbox = tkinter.Spinbox(user_info_frame, from_ = 1930, to = 2060)
dateYear_spinbox.grid(row = 6, column = 2)



for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx = 10, pady = 5)


button = tkinter.Button(frame, text = "Continue", command = enter_data)
button.grid(row = 6, column = 0, sticky = "news", padx = 70, pady = 10)










mainWindow.mainloop()
