# ---------------------------------------------------------
# project: e.d.s's pizza ordering program
# names: eric nguyen & duke caperon
# date: may 19, 2026
#
# details:
# main script to run the window, variables, and glue everything together
# ---------------------------------------------------------

from tkinter import *
from gui_left import build_left_pane
from gui_right import build_right_pane
from pricing import calculate_pizza, compile_receipt

# window setup stuff
window = Tk()
window.title("Pizza Ordering Program")

# get screen size dynamically
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# figure out 80% screen size
width = int(screen_width * 0.8)
height = int(screen_height * 0.8)

# math to center the window
x = int((screen_width - width) / 2)
y = int((screen_height - height) / 2)

window.geometry(f"{width}x{height}+{x}+{y}")
window.config(bg="#FAF9F6")

# variables for pizza choices
size = StringVar()
size.set("Medium")  # default value

crust = StringVar()
crust.set("Hand-Tossed")  # default value

toppings = {
    "Pepperoni": IntVar(),
    "Sausage": IntVar(),
    "Mushrooms": IntVar(),
    "Onions": IntVar(),
    "Extra Cheese": IntVar(),
    "Pineapple": IntVar()   #do NOT pick pineapple
}

# text field for customer name
customer_name = StringVar()

# list to keep track of added pizzas
current_order = []

# helper to write text to the scrollable box
def update_receipt_display(text):
    receipt_label.config(state=NORMAL)
    receipt_label.delete("1.0", END)
    receipt_label.insert(END, text)
    receipt_label.config(state=DISABLED)

# what happens when you click add
def add_to_order():
    # get dictionary of what is checked
    toppings_states = {name: var.get() == 1 for name, var in toppings.items()}
    
    # do math for this specific pizza
    desc, price = calculate_pizza(size.get(), crust.get(), toppings_states)
    
    # unique signature to find duplicates
    selected_toppings = tuple(sorted(name for name, is_sel in toppings_states.items() if is_sel))
    signature = (size.get(), crust.get(), selected_toppings)
    
    # see if we already added this exact pizza
    found = False
    for item in current_order:
        if item["signature"] == signature:
            item["qty"] += 1
            found = True
            break
            
    if not found:
        current_order.append({
            "description": desc,
            "price_each": price,
            "qty": 1,
            "signature": signature
        })
        
    # update receipt box with preview
    receipt_text = compile_receipt(current_order, customer_name.get(), is_final=False)
    update_receipt_display(receipt_text)

# click() function called when the user submits their order
def click():
    receipt_text = compile_receipt(current_order, customer_name.get(), is_final=True)
    update_receipt_display(receipt_text)
    
    # wipe order clean for next customer
    if current_order:
        current_order.clear()
    customer_name.set("")

# frames for left and right columns
left_pane = Frame(window, bg="#FAF9F6")
left_pane.place(relx=0.0, rely=0.0, relwidth=0.5, relheight=1.0)

right_pane = Frame(window, bg="#FAF9F6")
right_pane.place(relx=0.5, rely=0.0, relwidth=0.5, relheight=1.0)

# vertical line down the middle (80% height)
divider = Frame(window, bg="grey", width=2)
divider.place(relx=0.5, rely=0.1, relheight=0.8, anchor="n")

# load left side widgets
build_left_pane(left_pane)

# load right side widgets
variables = {
    "size": size,
    "crust": crust,
    "toppings": toppings,
    "customer_name": customer_name
}
receipt_label = build_right_pane(right_pane, variables, add_to_order, click)

# run the main event loop
window.mainloop()