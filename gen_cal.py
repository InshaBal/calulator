import tkinter as tk

# Calculation variable
calculation = ""

# Function to add symbols to the calculation field
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Function to evaluate the calculation
def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clear_field()
        text_result.insert(1.0, "Error")

# Function to clear the calculation field
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Root window setup
root = tk.Tk()
root.geometry("400x500")
root.title("Calculator")
root.configure(bg="#222831")  # Dark theme background

# Title Label
label = tk.Label(root, text="Calculator", font=("Arial", 20, "bold"), fg="white", bg="#222831")
label.grid(row=0, column=0, columnspan=5, pady=10)

# Display Field
text_result = tk.Text(root, height=2, width=20, font=("Arial", 24), bg="#393E46", fg="white")
text_result.grid(row=1, column=0, columnspan=5, padx=10, pady=10)

# Button styling
button_bg = "#00ADB5"
button_fg = "white"
button_font = ("Arial", 14, "bold")

# Number buttons
buttons = [
    ("1", 2, 1), ("2", 2, 2), ("3", 2, 3),
    ("4", 3, 1), ("5", 3, 2), ("6", 3, 3),
    ("7", 4, 1), ("8", 4, 2), ("9", 4, 3),
    ("0", 5, 2)
]

for (text, row, col) in buttons:
    tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=button_font,
              bg=button_bg, fg=button_fg).grid(row=row, column=col, pady=5, padx=5)

# Operator buttons
operators = [
    ("+", 2, 4), ("-", 3, 4), ("*", 4, 4), ("/", 5, 4),
    ("(", 5, 1), (")", 5, 3)
]

for (text, row, col) in operators:
    tk.Button(root, text=text, command=lambda t=text: add_to_calculation(t), width=5, font=button_font,
              bg="#F96D00", fg="white").grid(row=row, column=col, pady=5, padx=5)

# Clear and Equal buttons
tk.Button(root, text="C", command=clear_field, width=11, font=button_font,
          bg="#FF2E63", fg="white").grid(row=6, column=1, columnspan=2, pady=5, padx=5)
tk.Button(root, text="=", command=evaluate_calculation, width=11, font=button_font,
          bg="#76ABAE", fg="white").grid(row=6, column=3, columnspan=2, pady=5, padx=5)

# Run the app
root.mainloop()
