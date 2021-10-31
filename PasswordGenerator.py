from tkinter import *
import string
import random as r
from tkinter import messagebox


root = Tk()

# TitleBar
root.geometry("360x360")
root.title("Password Generator")
root.iconbitmap("D:/PassGen/padlock.ico")

global selected
selected = False
global txt_strenght
txt_strenght = False
global strenght_color
strenght_color = False
# Functions
def button_gen():
    outputEntry.delete(0.1, END)
    try:
        user_input = int(inputEntry.get())
    except ValueError:
        messagebox.showwarning("Try again", "Don't trick me! Enter a number.")
        inputEntry.delete(0, END)
    else:
        pass_generator(user_input)

def pass_strenght(pas):
    lenght = int(pas)
    if lenght <= 5:
        txt_strenght = "Weak"
        strenght_color = "#C70039"
    elif lenght in range(6,9) :
        txt_strenght= "Medium"
        strenght_color = "#FF5733"
    else:
        txt_strenght = "Strong"
        strenght_color = "#23C461"

    mid2 = Label(root, text=txt_strenght, font="Verdana 9 bold", fg=strenght_color)
    mid2.grid(row=2, column=1, padx=10, pady=10)

def pass_generator(x):
    letters = list(string.ascii_letters)
    digits = list(string.digits)
    symbols = ["!", "@", "#", "$", "&", "*", "?"]
    pas = []
    for j in range(1):
        pas.append(r.choice(symbols))
    for j in range(2):
        pas.append(r.choice(digits))
    while len(pas) < x:
        pas.append(r.choice(letters))
    r.shuffle(pas)
    password = "".join(pas)
    pass_strenght(x)
    outputEntry.delete(1.0,END)
    outputEntry.insert(1.0, password)


def copy_button():
    selected = outputEntry.get(1.0, END)
    outputEntry.clipboard_clear()
    outputEntry.clipboard_append(selected)

# Widgets

head = Label(root, text="Enter password lenght:", font = "Verdana 12 bold", fg ="#4499C8")
head.grid(row=0, columnspan=2, padx=20, pady=10)

inputEntry = Entry(root,font="Verdana 9 bold", width= 10, borderwidth=3.5)
inputEntry.grid(row= 1, padx=20, pady=5)

buttonGenerate = Button(root, text="Generate", command=button_gen, width= 10, font = "Verdana 8 bold", bg="purple", fg="white")
buttonGenerate.grid(row=1, column =1, padx=20, pady=5)

mid = Label(root, text="Strenght: ", font="Verdana 9 bold", fg="darkgrey")
mid.grid(row=2, padx=10, pady=5)

outputEntry = Text(root, font= "Verdana 10 bold", width= 35, height= 5, borderwidth=3.5)
outputEntry.grid(row=3, columnspan=2, padx=20, pady= 5)

buttonCopy = Button(root, text="Copy", command=copy_button, font = "Verdana 8 bold", bg="lightgreen", fg="black")
buttonCopy.grid(row=4, column=1, padx=20, pady=5)


root.mainloop()
