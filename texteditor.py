import sys
from tkinter import *
from tkinter.filedialog import asksaveasfilename


# Main Window
root = Tk()
root.title("Text Editor")

# Frame to hold both line numbers and the main text area
frame = Frame(root)
frame.grid(row=0, column=0, sticky="nsew")

# Line Numbers
line_numbers = Text(frame, width=4, padx=5, takefocus=0, border=0, background="lightgrey", state="disabled")
line_numbers.grid(row=0, column=0, sticky="ns")

# Main Text Widget
text = Text(frame, undo=True, wrap="none")
text.grid(row=0, column=1, sticky="nsew")

# Scrollbar
scrollbar = Scrollbar(frame, command=text.yview)
scrollbar.grid(row=0, column=2, sticky="ns")
text.config(yscrollcommand=scrollbar.set)


# Function to update line numbers
def update_line_numbers(event=None):
    line_numbers.config(state="normal")
    line_numbers.delete("1.0", "end")

    line_count = text.index("end-1c").split(".")[0]
    line_numbers_content = "\n".join(str(i) for i in range(1, int(line_count)))
    line_numbers.insert("1.0", line_numbers_content)

    line_numbers.config(state="disabled")


# Save Function
def saveas():
    global text
    t = text.get("1.0", "end-1c")
    savelocation = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if savelocation:  # Only proceed if a location is selected
        with open(savelocation, "w+") as file1:
            file1.write(t)


# Save Button
button = Button(root, text="Save", command=saveas)
button.grid(row=1, column=0, sticky="ew")


# Change Font to Helvetica
def FontHelvetica():
    global text
    text.config(font="Helvetica")


# Change Font to Courier
def FontCourier():
    global text
    text.config(font="Courier")


# Font Menu
font = Menubutton(root, text="Font")
font.grid(row=1, column=1, sticky="ew")
font.menu = Menu(font, tearoff=0)
font["menu"] = font.menu

Courier = IntVar()
Helvetica = IntVar()
font.menu.add_checkbutton(label="Courier", variable=Courier, command=FontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica, command=FontHelvetica)


# Bindings to update line numbers dynamically
text.bind("<KeyRelease>", update_line_numbers)
text.bind("<MouseWheel>", update_line_numbers)
text.bind("<Return>", update_line_numbers)
text.bind("<BackSpace>", update_line_numbers)

# Initialize line numbers on launch
update_line_numbers()

# Run the GUI
root.mainloop()
