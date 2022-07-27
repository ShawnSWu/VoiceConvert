import convert
import tkinter as tk
from tkinter import ttk
import os
from os import listdir
from os.path import isfile, isdir, join

window = tk.Tk()
window.title("change voice")
window.geometry("900x500")


labelTop = tk.Label(window, text="Choose your file that you want to convert")
labelTop.pack()


all_files = listdir(os.getcwd())
file_list = []
i = 0
for f in all_files:
    fullpath = join(os.getcwd(), f)

    if isfile(fullpath):
        if ".wav" in f:
            file_list.append(f)

    i = i + 1
comboExample = ttk.Combobox(window, values=file_list, width=50)
# comboExample.current(0)
comboExample.pack()


var = tk.StringVar()


label_voice = tk.Label(window, text="Choose voice that you want to convert")
label_voice.pack()

radiobutton_Mac_To_Women = tk.Radiobutton(window, text="Man", variable=var, value="Man")
radiobutton_Women_To_Man = tk.Radiobutton(window, text="Female", variable=var, value="Female")
radiobutton_Mac_To_Women.place(x=320, y=80)
radiobutton_Women_To_Man.place(x=520, y=80)

l = tk.Label(window, bg='yellow', width=20, text='empty')
l.place()


def submit():
    box_value = "/videoplayback.mp4"
    select = "Female"

    if select == "Man":
        result = convert.women_to_man_chinese(box_value)
        var.set(result)
    elif select == "Female":
        result = convert.man_to_women_english(box_value)
        var.set(result)
    else:
        var.set("you didn't select yet.")



submit()

# b1 = tk.Button(window, bg="red", text="Submit", width=15, height=2, command=submit)
# b1.place(x=380, y=130)
#
#
# label_select = tk.Label(window, text="You select:")
# label_select.place(x=150, y=200)
# label_status = tk.Label(window, bg="red", text="", textvariable=var)
# label_status.place(x=230, y=200)
#
#
# window.mainloop()