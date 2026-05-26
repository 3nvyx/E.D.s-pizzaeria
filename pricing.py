# ---------------------------------------------------------
# project: e.d.s's pizza ordering program
# names: eric nguyen & duke caperon
# date: may 19, 2026
#
# details:
# does the math for pricing and formats the text table
# ---------------------------------------------------------

def calculate_pizza(size_val, crust_val, toppings_states):
    price = 0.0

    # size prices
    if size_val == "Small":
        price += 10.99
    elif size_val == "Medium":
        price += 12.99
    elif size_val == "Large":
        price += 14.99

    # every pizza starts with cheese
    toppings_list = ["Cheese"]
    
    # loop through toppings and add prices
    for topping_name, is_selected in toppings_states.items():
        if is_selected:
            if topping_name == "Pineapple":
                price += 50.00  # lol $50 for pineapple
            else:
                price += 1.25
            toppings_list.append(topping_name)

    desc = f"{size_val} {crust_val} ({', '.join(toppings_list)})"
    return desc, price

def compile_receipt(pizzas_list, is_final=False):
    if not pizzas_list:
        return "Your order is empty.\nPlease add items first."

    # header stuff
    title = "Final Receipt...\n\n" if is_final else "Your Order (Preview)...\n\n"
    receipt = title
    
    # columns for the table: items, qty, price (45 chars total)
    receipt += f"{'Items'.ljust(32)}{'QTY'.rjust(4)}{'Price'.rjust(9)}\n"
    receipt += "-" * 45 + "\n"

    subtotal = 0.0
    for item in pizzas_list:
        desc = item["description"]
        qty = item["qty"]
        price_each = item["price_each"]
        total_price = price_each * qty
        subtotal += total_price

        # cut off long names so columns stay aligned
        if len(desc) > 29:
            display_desc = desc[:26] + "..."
        else:
            display_desc = desc

        receipt += f"{display_desc.ljust(32)}{str(qty).rjust(4)}{f'${total_price:.2f}'.rjust(9)}\n"

    receipt += "-" * 45 + "\n"
    
    if is_final:
        tax = subtotal * 0.0875
        total = subtotal + tax
        receipt += f"Subtotal: {''.rjust(25)}{f'${subtotal:.2f}'.rjust(9)}\n"
        receipt += f"Tax (8.75%): {''.rjust(21)}{f'${tax:.2f}'.rjust(9)}\n"
        receipt += f"Total: {''.rjust(28)}{f'${total:.2f}'.rjust(9)}"
    else:
        receipt += f"Subtotal Preview: {''.rjust(18)}{f'${subtotal:.2f}'.rjust(9)}\n\n"
        receipt += "Press 'Submit Order' to finalize."

    return receipt
