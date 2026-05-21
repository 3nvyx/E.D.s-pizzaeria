# ---------------------------------------------------------
# Project Name: E.D.S's Pizza Ordering Program
# Names: Eric Nguyen & Duke Cameron
# Date: May 19, 2026
#
# Description:
# This program allows users to order a pizza by selecting
# a size, crust type, and toppings using a Tkinter GUI.
# The program calculates subtotal, tax, and total cost,
# then displays a receipt on the screen.
# ---------------------------------------------------------

from tkinter import *

#window set-up
window = Tk()
window.title("Pizza Ordering Program")
window.geometry("1000x800")
window.config(bg="lightyellow")

# Pizza size variable
# StringVar() is a special Tkinter variable that can be used with widgets
size = StringVar()
size.set("Medium")  # default value

# Crust type variable
crust = StringVar()
crust.set("Hand-Tossed")  # default value

# Topping variables
extra_cheese = IntVar()
pineapple = IntVar()
pepperoni = IntVar()
sausage = IntVar()
mushrooms = IntVar()

def click():
    subtotal = 0

    # Pizza size pricing
    if size.get() == "Small":
        subtotal += 10.99

    elif size.get() == "Medium":
        subtotal += 12.99

    elif size.get() == "Large":
        subtotal += 14.99

    #toppings list starts with cheese
    toppings_list = ["Cheese"]
    if extra_cheese.get() == 1:
        subtotal += 1.25
        toppings_list.append("Extra Cheese")
    
    if pineapple.get() == 1:
        subtotal += 50
        toppings_list.append("Pineapple")

    if pepperoni.get() == 1:
        subtotal += 1.25
        toppings_list.append("Pepperoni")

    if sausage.get() == 1:
        subtotal += 1.25
        toppings_list.append("Sausage")

    if mushrooms.get() == 1:
        subtotal += 1.25
        toppings_list.append("Mushrooms")
    
    # calculate total
    tax = subtotal * 0.0875
    total = subtotal + tax

    #make receipt

    receipt = ""
    receipt += "Your Reciept...\n\n"
    receipt += f"Size: {size.get()}\n"
    receipt += f"Crust: {crust.get()}\n"
    receipt += f"Toppings: {', '.join(toppings_list)}\n\n"
    receipt += f"Subtotal: ${subtotal:.2f}\n"
    receipt += f"Tax: ${tax:.2f}\n"
    receipt += f"Total: ${total:.2f}"

    # Display receipt
    receipt_label.config(text=receipt)

#menu
photo = PhotoImage(file="menu.gif")

image_label = Label(window, image=photo)
image_label.pack(pady=10)

#title
title_label = Label(
    window,
    text="E.D.S's Pizzeria",
    font=("Arial", 20, "bold"), #can change font later
    bg="lightyellow"
)
title_label.pack()

size_label = Label(
    window,
    text="Choose Pizza Size:",
    font=("Arial", 14),
    bg="lightyellow"
)
size_label.pack()

Radiobutton(
    window,
    text="Small - $10.99",
    variable=size,
    value="Small",
    bg="lightyellow"
).pack()

Radiobutton(
    window,
    text="Medium - $12.99",
    variable=size,
    value="Medium",
    bg="lightyellow"
).pack()

Radiobutton(
    window,
    text="Large - $14.99",
    variable=size,
    value="Large",
    bg="lightyellow"
).pack()

# -------------------------
# CRUST SECTION
# -------------------------

crust_label = Label(
    window,
    text="Choose Crust Type:",
    font=("Arial", 14),
    bg="lightyellow"
)
crust_label.pack(pady=(10, 0))

Radiobutton(
    window,
    text="Hand-Tossed",
    variable=crust,
    value="Hand-Tossed",
    bg="lightyellow"
).pack()

Radiobutton(
    window,
    text="Deep-Dish",
    variable=crust,
    value="Deep-Dish",
    bg="lightyellow"
).pack()

Radiobutton(
    window,
    text="Thin-Crust",
    variable=crust,
    value="Thin-Crust",
    bg="lightyellow"
).pack()

# -------------------------
# TOPPINGS SECTION
# -------------------------

toppings_label = Label(
    window,
    text="Choose Toppings ($1.25 each):",
    font=("Arial", 14),
    bg="lightyellow"
)
toppings_label.pack(pady=(10, 0))

Checkbutton(
    window,
    text="Extra Cheese",
    variable=extra_cheese,
    bg="lightyellow"
).pack()

Checkbutton(
    window,
    text="Pepperoni",
    variable=pepperoni,
    bg="lightyellow"
).pack()

Checkbutton(
    window,
    text="Sausage",
    variable=sausage,
    bg="lightyellow"
).pack()

Checkbutton(
    window,
    text="Mushrooms",
    variable=mushrooms,
    bg="lightyellow"
).pack()

Checkbutton(
    window,
    text="Pineapple",
    variable=pineapple,
    bg="lightyellow"
).pack()


submit_button = Button(
    window,
    text="Submit Order",
    font=("Arial", 14),
    command=click
)
submit_button.pack(pady=15)


receipt_label = Label(
    window,
    text="Your receipt will appear here.",
    font=("Courier", 12),
    bg="white",
    width=40,
    height=12,
    justify=LEFT,
    anchor="nw",
    relief="solid"
)
receipt_label.pack(pady=10)

window.mainloop()