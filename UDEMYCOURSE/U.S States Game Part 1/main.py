from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# Label. pack(), place(), grid() nurodo pavadinimo vieta(pvz: virsuje, desineje, kaireje)
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.pack(side="left")
# my_label.place(x=100, y=200)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)


def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


def New_button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

# Button


button = Button(text="Click Me", command=button_clicked)
# button.pack(side="left")
button.grid(column=1, row=1)

New_button = Button(text="Click_me", command=New_button_clicked)
New_button.grid(column=2, row=0)

# Entry
input = Entry(width=30)
print(input.get())
# input.pack(side="left")
input.grid(column=3, row=2)

window.mainloop()
