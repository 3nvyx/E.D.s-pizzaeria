# ---------------------------------------------------------
# project: e.d.s's pizza ordering program
# names: eric nguyen & duke caperon
# date: may 29, 2026
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

    # every pizza starts with cheese, you may not remove it, because that is strange
    toppings_list = ["Cheese"]
    
    # loop through toppings and add prices
    for topping_name, is_selected in toppings_states.items():
        if is_selected:
            if topping_name == "Pineapple":
                price += 50.00  # lol $50 for pineapple # completely deserved
            else:
                price += 1.25
            toppings_list.append(topping_name)

    desc = f"{size_val} {crust_val} ({', '.join(toppings_list)})"
    return desc, price

def wrap_description(desc, first_line_width=29, rest_line_width=27, indent_str="  "):
    if len(desc) <= first_line_width:
        return [desc]
        
    words = desc.split(' ')
    lines = []
    
    # Wrap the first line
    current_line = []
    current_length = 0
    word_idx = 0
    
    while word_idx < len(words):
        word = words[word_idx]
        space_padding = 1 if current_line else 0
        if current_length + len(word) + space_padding <= first_line_width:
            current_line.append(word)
            current_length += len(word) + space_padding
            word_idx += 1
        else:
            break
            
    if current_line:
        lines.append(' '.join(current_line))
    else:
        lines.append(words[0])
        word_idx = 1
        
    # Wrap subsequent lines (with indentation)
    current_line = []
    current_length = 0
    
    while word_idx < len(words):
        word = words[word_idx]
        space_padding = 1 if current_line else 0
        if current_length + len(word) + space_padding <= rest_line_width:
            current_line.append(word)
            current_length += len(word) + space_padding
            word_idx += 1
        else:
            if current_line:
                lines.append(indent_str + ' '.join(current_line))
            current_line = [word]
            current_length = len(word)
            word_idx += 1
            
    if current_line:
        lines.append(indent_str + ' '.join(current_line))
        
    return lines

def compile_receipt(pizzas_list, customer_name_val="", is_final=False):
    if not pizzas_list:
        return "Your order is empty.\nPlease add items first."

    # header stuff
    title = "Final Receipt...\n" if is_final else "Your Order (Preview)...\n"
    receipt = title
    if customer_name_val.strip():
        receipt += f"Customer: {customer_name_val.strip()}\n"
    receipt += "\n"
    
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

        # Wrap long descriptions to make sure all toppings are shown
        desc_lines = wrap_description(desc)
        
        # Add first line of description with QTY and Price aligned
        receipt += f"{desc_lines[0].ljust(32)}{str(qty).rjust(4)}{f'${total_price:.2f}'.rjust(9)}\n"
        
        # Add remaining lines of description with blank QTY and Price columns
        for extra_line in desc_lines[1:]:
            receipt += f"{extra_line.ljust(32)}{''.rjust(4)}{''.rjust(9)}\n"

    receipt += "-" * 45 + "\n"
    
    if is_final:
            tax = subtotal * 0.0875
            total = subtotal + tax
            
            # Right-justify the label to 36 chars, and the price to 9 chars (Total = 45 chars)
            receipt += f"{'Subtotal:':>36}{f'${subtotal:.2f}':>9}\n"
            receipt += f"{'Tax (8.75%):':>36}{f'${tax:.2f}':>9}\n"
            receipt += f"{'Total:':>36}{f'${total:.2f}':>9}\n\n"
            
            # Center the thank you message across the full 45-character width
            receipt += f"{'Thank you for your order!':^45}"
            
    else:
        # We can apply the exact same alignment math to the preview block!
        receipt += f"{'Subtotal Preview:':>36}{f'${subtotal:.2f}':>9}\n\n"
        receipt += "Press 'Submit Order' to finalize.".center(45)

    return receipt
