from tkinter import *

window = Tk()
window.title("Duke's Practice")
window.geometry("1400x1300")

window.configure(bg="lightblue")


title_label = Label(
    window,
    text="Pizza Ordering Program",
    font=("Arial", 20, "bold"),
    bg="lightyellow"
)
title_label.place(relx=0.7, rely=0.2)


#title_label.pack()


Radiobutton(
    window,
    text="Small - $10.99",
    variable='small',
    value="Small",
    bg="lightyellow"
).place(relx=0.7, rely=0.3)

Radiobutton(
    window,
    text="Medium - $12.99",
    variable='large',
    value="Medium",
    bg="lightyellow"
).pack()




window.mainloop()




