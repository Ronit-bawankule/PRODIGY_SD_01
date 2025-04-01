import tkinter as tk
from tkinter import ttk

# Function to convert temperature
def convert_temperature():
    try:
        value = float(entry_temp.get())
        unit = unit_var.get()

        if unit == "Celsius":
            fahrenheit = (value * 9/5) + 32
            kelvin = value + 273.15
            result_var.set(f"{value}°C = {fahrenheit:.2f}°F, {kelvin:.2f}K")
        
        elif unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
            kelvin = celsius + 273.15
            result_var.set(f"{value}°F = {celsius:.2f}°C, {kelvin:.2f}K")

        elif unit == "Kelvin":
            celsius = value - 273.15
            fahrenheit = (celsius * 9/5) + 32
            result_var.set(f"{value}K = {celsius:.2f}°C, {fahrenheit:.2f}°F")
    
    except ValueError:
        result_var.set("⚠️ Invalid input! Please enter a number.")

# Hover effect for button
def on_enter(e):
    convert_btn.config(bg="#2980B9")

def on_leave(e):
    convert_btn.config(bg="#3498DB")

# Create GUI Window
root = tk.Tk()
root.title("Temperature Converter")
root.geometry("450x350")
root.configure(bg="#2C3E50")  # Dark gradient background

# Styling
font_main = ("Arial", 14, "bold")
font_result = ("Arial", 12)

# Title Label
title_label = tk.Label(root, text="🌡 Temperature Converter", font=("Arial", 18, "bold"), fg="white", bg="#2C3E50")
title_label.pack(pady=15)

# Temperature Input
entry_temp = tk.Entry(root, font=font_main, width=10, justify="center", bg="#ECF0F1", bd=3, relief="ridge")
entry_temp.pack(pady=5)

# Unit Selection
unit_var = tk.StringVar(value="Celsius")
unit_menu = ttk.Combobox(root, textvariable=unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], font=("Arial", 12), state="readonly")
unit_menu.pack(pady=5)

# Convert Button
convert_btn = tk.Button(root, text="Convert", font=font_main, bg="#3498DB", fg="white", relief="flat", padx=10, pady=5, cursor="hand2", bd=3)
convert_btn.pack(pady=15)
convert_btn.bind("<Enter>", on_enter)  # Hover effect
convert_btn.bind("<Leave>", on_leave)
convert_btn.config(command=convert_temperature)  # Assign function

# Result Display
result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=font_result, fg="white", bg="#2C3E50")
result_label.pack(pady=10)

# Run GUI
root.mainloop()
