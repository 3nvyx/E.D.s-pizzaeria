# ---------------------------------------------------------
# project: e.d.s's pizza ordering program
# names: eric nguyen & duke caperon
# date: may 19, 2026
#
# details:
# sets up the right pane options, customized cards, and buttons
# ---------------------------------------------------------

from tkinter import *
from tkinter.scrolledtext import ScrolledText

class RadioCard(Frame):
    def __init__(self, parent, variable, value, title, subtitle, **kwargs):
        super().__init__(parent, highlightthickness=1.5, relief="flat", padx=12, pady=10, cursor="hand2", **kwargs)
        self.variable = variable
        self.value = value
        
        # border colors for clicking
        self.unselected_bg = "#FAF9F6"       # alabaster paper white
        self.selected_bg = "#FAF9F6"
        self.unselected_border = "#DCD5CA"   # brownish-grey border
        self.selected_border = "#0088FF"     # blue highlight border
        
        self.config(bg=self.unselected_bg, highlightbackground=self.unselected_border)
        
        # left side has the text stack
        self.text_container = Frame(self, bg=self.unselected_bg)
        self.text_container.pack(side=LEFT, fill=BOTH, expand=True)
        
        # title text (small, medium, etc.)
        self.title_label = Label(
            self.text_container,
            text=title,
            font=("Arial", 11, "bold"),
            bg=self.unselected_bg,
            fg="#5C4033", # dark brown
            anchor="w"
        )
        self.title_label.pack(side=TOP, fill=X)
        
        # secondary info (sizes and prices)
        self.subtitle_label = Label(
            self.text_container,
            text=subtitle,
            font=("Arial", 9),
            bg=self.unselected_bg,
            fg="#8B7D6B", # light brown
            anchor="w"
        )
        self.subtitle_label.pack(side=TOP, fill=X, pady=(2, 0))
        
        # small circle thingy on the right
        self.indicator_label = Label(
            self,
            text="○",
            font=("Arial", 14),
            bg=self.unselected_bg,
            fg="#DCD5CA",
            anchor="e"
        )
        self.indicator_label.pack(side=RIGHT, fill=Y)
        
        # bind clicking on everything so it triggers select
        for w in (self, self.text_container, self.title_label, self.subtitle_label, self.indicator_label):
            w.bind("<Button-1>", self.on_click)
            
        # run update state whenever variable changes
        self.trace_id = self.variable.trace_add("write", self.update_state)
        self.update_state()
        
    def on_click(self, event):
        self.variable.set(self.value)
        
    def update_state(self, *args):
        try:
            is_selected = self.variable.get() == self.value
        except Exception:
            is_selected = False
            
        if is_selected:
            bg_color = self.selected_bg
            border_color = self.selected_border
            indicator_char = "◉"
            indicator_color = self.selected_border
        else:
            bg_color = self.unselected_bg
            border_color = self.unselected_border
            indicator_char = "○"
            indicator_color = "#DCD5CA"
            
        self.config(bg=bg_color, highlightbackground=border_color)
        self.text_container.config(bg=bg_color)
        self.title_label.config(bg=bg_color)
        self.subtitle_label.config(bg=bg_color)
        self.indicator_label.config(bg=bg_color, text=indicator_char, fg=indicator_color)

class CheckCard(Frame):
    def __init__(self, parent, variable, title, subtitle, **kwargs):
        super().__init__(parent, highlightthickness=1.5, relief="flat", padx=12, pady=10, cursor="hand2", **kwargs)
        self.variable = variable
        
        self.unselected_bg = "#FAF9F6"
        self.selected_bg = "#FAF9F6"
        self.unselected_border = "#DCD5CA"
        self.selected_border = "#0088FF"
        
        self.config(bg=self.unselected_bg, highlightbackground=self.unselected_border)
        
        # text labels frame
        self.text_container = Frame(self, bg=self.unselected_bg)
        self.text_container.pack(side=LEFT, fill=BOTH, expand=True)
        
        # title
        self.title_label = Label(
            self.text_container,
            text=title,
            font=("Arial", 11, "bold"),
            bg=self.unselected_bg,
            fg="#5C4033",
            anchor="w"
        )
        self.title_label.pack(side=TOP, fill=X)
        
        # info
        self.subtitle_label = Label(
            self.text_container,
            text=subtitle,
            font=("Arial", 9),
            bg=self.unselected_bg,
            fg="#8B7D6B",
            anchor="w"
        )
        self.subtitle_label.pack(side=TOP, fill=X, pady=(2, 0))
        
        # check box symbol
        self.indicator_label = Label(
            self,
            text="☐",
            font=("Arial", 14),
            bg=self.unselected_bg,
            fg="#DCD5CA",
            anchor="e"
        )
        self.indicator_label.pack(side=RIGHT, fill=Y)
        
        # click handlers
        for w in (self, self.text_container, self.title_label, self.subtitle_label, self.indicator_label):
            w.bind("<Button-1>", self.on_click)
            
        # updates border color on change
        self.trace_id = self.variable.trace_add("write", self.update_state)
        self.update_state()
        
    def on_click(self, event):
        current = self.variable.get()
        self.variable.set(0 if current == 1 else 1)
        
    def update_state(self, *args):
        try:
            is_selected = self.variable.get() == 1
        except Exception:
            is_selected = False
            
        if is_selected:
            bg_color = self.selected_bg
            border_color = self.selected_border
            indicator_char = "☑"
            indicator_color = self.selected_border
        else:
            bg_color = self.unselected_bg
            border_color = self.unselected_border
            indicator_char = "☐"
            indicator_color = "#DCD5CA"
            
        self.config(bg=bg_color, highlightbackground=border_color)
        self.text_container.config(bg=bg_color)
        self.title_label.config(bg=bg_color)
        self.subtitle_label.config(bg=bg_color)
        self.indicator_label.config(bg=bg_color, text=indicator_char, fg=indicator_color)

def build_right_pane(parent, variables, add_callback, submit_callback):
    size_var = variables["size"]
    crust_var = variables["crust"]
    toppings_vars = variables["toppings"]

    # giant underlined menu title
    menu_header = Label(
        parent,
        text="Menu",
        font=("Crimson Text", 28, "bold", "underline"),
        bg="#FAF9F6",
        fg="black"
    )
    menu_header.pack(pady=(30, 5))

    # wrapper frame for packing
    container = Frame(parent, bg="#FAF9F6")
    container.pack(fill=BOTH, expand=True, padx=30, pady=10)

    # size options
    size_label = Label(
        container,
        text="Choose Pizza Size:",
        font=("Arial", 13, "bold"),
        bg="#FAF9F6",
        fg="black",
        anchor="w"
    )
    size_label.pack(fill=X, pady=(10, 5))

    size_row = Frame(container, bg="#FAF9F6")
    size_row.pack(fill=X, pady=5)
    size_row.columnconfigure(0, weight=1, uniform="sizes")
    size_row.columnconfigure(1, weight=1, uniform="sizes")
    size_row.columnconfigure(2, weight=1, uniform="sizes")

    sizes_info = [
        ("Small", "10\" - $10.99", "Small"),
        ("Medium", "12\" - $12.99", "Medium"),
        ("Large", "14\" - $14.99", "Large")
    ]

    for col, (title, subtitle, val) in enumerate(sizes_info):
        card = RadioCard(size_row, size_var, val, title, subtitle)
        card.grid(row=0, column=col, padx=4, sticky="nsew")

    # crust options
    crust_label = Label(
        container,
        text="Choose Crust Type:",
        font=("Arial", 13, "bold"),
        bg="#FAF9F6",
        fg="black",
        anchor="w"
    )
    crust_label.pack(fill=X, pady=(15, 5))

    crust_row = Frame(container, bg="#FAF9F6")
    crust_row.pack(fill=X, pady=5)
    crust_row.columnconfigure(0, weight=1, uniform="crusts")
    crust_row.columnconfigure(1, weight=1, uniform="crusts")
    crust_row.columnconfigure(2, weight=1, uniform="crusts")

    crusts_info = [
        ("Hand-Tossed", "Classic crust", "Hand-Tossed"),
        ("Deep-Dish", "Thick pan crust", "Deep-Dish"),
        ("Thin-Crust", "Crispy thin crust", "Thin-Crust")
    ]

    for col, (title, subtitle, val) in enumerate(crusts_info):
        card = RadioCard(crust_row, crust_var, val, title, subtitle)
        card.grid(row=0, column=col, padx=4, sticky="nsew")

    # toppings grid
    toppings_label = Label(
        container,
        text="Choose Toppings ($1.25 each):",
        font=("Arial", 13, "bold"),
        bg="#FAF9F6",
        fg="black",
        anchor="w"
    )
    toppings_label.pack(fill=X, pady=(15, 5))

    toppings_row = Frame(container, bg="#FAF9F6")
    toppings_row.pack(fill=X, pady=5)
    toppings_row.columnconfigure(0, weight=1, uniform="toppings")
    toppings_row.columnconfigure(1, weight=1, uniform="toppings")
    toppings_row.columnconfigure(2, weight=1, uniform="toppings")

    toppings_list = list(toppings_vars.items())
    
    # lay out toppings in a 3-col grid
    for idx, (name, var) in enumerate(toppings_list):
        row = idx // 3
        col = idx % 3
        price_str = "+$50.00" if name == "Pineapple" else "+$1.25"
        
        card = CheckCard(toppings_row, var, name, price_str)
        card.grid(row=row, column=col, padx=4, pady=4, sticky="nsew")

    # order actions and receipt box
    button_row = Frame(container, bg="#FAF9F6")
    button_row.pack(pady=15)

    add_button = Button(
        button_row,
        text="Add to Order",
        font=("Arial", 12, "bold"),
        command=add_callback
    )
    add_button.pack(side=LEFT, padx=10)

    submit_button = Button(
        button_row,
        text="Submit Order",
        font=("Arial", 12, "bold"),
        command=submit_callback
    )
    submit_button.pack(side=LEFT, padx=10)

    receipt_label = ScrolledText(
        container,
        font=("Courier", 11),
        bg="white",
        fg="black",
        width=50,
        height=14,
        relief="solid"
    )
    receipt_label.insert(END, "Your receipt will appear here.")
    receipt_label.config(state=DISABLED)
    receipt_label.pack(pady=5)

    return receipt_label
