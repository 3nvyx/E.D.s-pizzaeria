# ---------------------------------------------------------
# Names: Eric Nguyen & Partner Name
# Date: May 19, 2026
# Program: E.D.S's Pizza Ordering Program
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
size = StringVar()
size.set("Medium")  # default value

# Crust type variable
crust = StringVar()
crust.set("Hand-Tossed")  # default value

# Topping variables
pepperoni = IntVar()
sausage = IntVar()
mushrooms = IntVar()
onions = IntVar()

def click():
    subtotal = 0

    # Pizza size pricing
    if size.get() == "Small":
        subtotal += 10.99

    elif size.get() == "Medium":
        subtotal += 12.99

    elif size.get() == "Large":
        subtotal += 14.99

    # -------------------------
    # ADD TOPPING COSTS
    # -------------------------

    toppings_list = ["Cheese"]

    if pepperoni.get() == 1:
        subtotal += 1.25
        toppings_list.append("Pepperoni")

    if sausage.get() == 1:
        subtotal += 1.25
        toppings_list.append("Sausage")

    if mushrooms.get() == 1:
        subtotal += 1.25
        toppings_list.append("Mushrooms")

    if onions.get() == 1:
        subtotal += 1.25
        toppings_list.append("Onions")

    # -------------------------
    # CALCULATE TAX & TOTAL
    # -------------------------

    tax = subtotal * 0.0875
    total = subtotal + tax

    # -------------------------
    # CREATE RECEIPT
    # -------------------------

    receipt = ""
    receipt += "------ PIZZA RECEIPT ------\n\n"
    receipt += f"Pizza Size: {size.get()}\n"
    receipt += f"Crust Type: {crust.get()}\n"
    receipt += f"Toppings: {', '.join(toppings_list)}\n\n"
    receipt += f"Subtotal: ${subtotal:.2f}\n"
    receipt += f"Tax: ${tax:.2f}\n"
    receipt += f"Total: ${total:.2f}"

    # Display receipt
    receipt_label.config(text=receipt)

# -------------------------
# IMAGE
# -------------------------

# Make sure menu.gif is in the SAME folder
photo = PhotoImage(file="menu.gif")

image_label = Label(window, image=photo)
image_label.place(relx=0.6, rely=0.2)

# -------------------------
# TITLE LABEL
# -------------------------

title_label = Label(
    window,
    text="Pizza Ordering Program",
    font=("Arial", 20, "bold"),
    bg="lightyellow"
)
title_label.place(relx=0.1, rely=0.2)
# 1. Create the main horizontal row
menu_frame = Frame(window, bg="lightyellow")
menu_frame.place(relx=0.08, rely=0.32, relwidth=0.84)

# 2. Divide that row into 3 equal columns
menu_frame.columnconfigure(0, weight=1, uniform="group1")
menu_frame.columnconfigure(1, weight=1, uniform="group1")
menu_frame.columnconfigure(2, weight=1, uniform="group1")

# 3. Create the 3 individual "column boxes"
size_frame = Frame(menu_frame, bg="lightyellow")
crust_frame = Frame(menu_frame, bg="lightyellow")
toppings_frame = Frame(menu_frame, bg="lightyellow")

# 4. Lock the boxes into their respective columns (0, 1, and 2)
size_frame.grid(row=0, column=0, sticky="n")
crust_frame.grid(row=0, column=1, sticky="n")
toppings_frame.grid(row=0, column=2, sticky="n")

# -------------------------
# PIZZA SIZE SECTION
# -------------------------

size_label = Label(
    size_frame,  # <-- 1. CHANGED TO THE SIZE FRAME
    text="Choose Pizza Size:",
    font=("Arial", 14, "bold"),
    bg="lightyellow"
)
size_label.pack(anchor="w", pady=(0, 10))  # <-- 2. CHANGED TO PACK (Left-aligned)

Radiobutton(
    size_frame,  # <-- 1. CHANGED TO THE SIZE FRAME
    text="Small - $10.99",
    variable=size,
    value="Small",
    bg="lightyellow",
    font=("Arial", 11)
).pack(anchor="w", pady=3)  # <-- 2. CHANGED TO PACK (Left-aligned)

Radiobutton(
    size_frame,
    text="Small - $10.99",
    variable=size,
    value="Small",
    bg="lightyellow"
).place(relx=0.1, rely=0.55)

Radiobutton(
    size_frame,
    text="Medium - $12.99",
    variable=size,
    value="Medium",
    bg="lightyellow"
).place(relx=0.1, rely=0.58)

Radiobutton(
    size_frame,
    text="Large - $14.99",
    variable=size,
    value="Large",
    bg="lightyellow"
).place(relx=0.1, rely=0.61)

# -------------------------
# CRUST SECTION
# -------------------------

crust_label = Label(
    size_frame,
    text="Choose Crust Type:",
    font=("Arial", 14),
    bg="lightyellow"
)
crust_label.place(relx=0.1, rely=0.65)

Radiobutton(
    size_frame,
    text="Hand-Tossed",
    variable=crust,
    value="Hand-Tossed",
    bg="lightyellow"
).place(relx=0.1, rely=0.7)

Radiobutton(
    size_frame,
    text="Deep-Dish",
    variable=crust,
    value="Deep-Dish",
    bg="lightyellow"
).place(relx=0.1, rely=0.73)

Radiobutton(
    size_frame,
    text="Thin-Crust",
    variable=crust,
    value="Thin-Crust",
    bg="lightyellow"
).place(relx=0.1, rely=0.76)

# -------------------------
# TOPPINGS SECTION
# -------------------------

toppings_label = Label(
    size_frame,
    text="Choose Toppings ($1.25 each):",
    font=("Arial", 14),
    bg="lightyellow"
)
toppings_label.pack(pady=(10, 0))

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
    text="Onions",
    variable=onions,
    bg="lightyellow"
).pack()

# -------------------------
# SUBMIT BUTTON
# -------------------------

submit_button = Button(
    window,
    text="Submit Order",
    font=("Arial", 14),
    command=click
)
submit_button.pack(pady=15)

# -------------------------
# RECEIPT SECTION
# -------------------------

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

# -------------------------
# MAIN LOOP
# -------------------------

window.mainloop()