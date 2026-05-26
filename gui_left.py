# ---------------------------------------------------------
# project: e.d.s's pizza ordering program
# names: eric nguyen & duke caperon
# date: may 19, 2026
#
# details:
# sets up the left side of the window (logo, title, and bio)
# ---------------------------------------------------------

from tkinter import *

def build_left_pane(parent):
    # load the pizza gif image
    photo = PhotoImage(file="menu.gif")
    image_label = Label(parent, image=photo, bg="#FAF9F6")
    image_label.pack(pady=(60, 20))
    image_label.image = photo  # need this reference so tkinter doesnt garbage collect it

    # centered title label
    title_label = Label(
        parent,
        text="E.D.S's Pizzeria",
        font=("Crimson Text", 36, "bold"),
        bg="#FAF9F6",
        fg="black"
    )
    title_label.pack(pady=10)

    # tiny section header
    about_title = Label(
        parent,
        text="About Us",
        font=("Crimson Text", 18, "bold", "underline"),
        bg="#FAF9F6",
        fg="black"
    )
    about_title.pack(pady=(20, 5))

    # short write up about the shop
    about_text = (
        "Welcome to E.D.S's Pizzeria!\n\n"
        "Established in 2026 by Eric Nguyen and Duke Caperon, "
        "we serve the finest hand-crafted pizzas made with fresh "
        "ingredients and lots of love. Craft your perfect slice today!"
    )
    about_label = Label(
        parent,
        text=about_text,
        font=("Arial", 12),
        bg="#FAF9F6",
        fg="black",
        wraplength=400,
        justify=CENTER
    )
    about_label.pack(pady=10, padx=20)
