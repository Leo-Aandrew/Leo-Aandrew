import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height * height)
        bmi_label.config(text=f"BMI: {bmi:.2f}")
        classify_bmi(bmi)
        store_data(weight, height, bmi)
    except ValueError:
        messagebox.showerror("Error", "Please enter valid weight and height.")

def classify_bmi(bmi):
    if bmi < 18.5:
        classification_label.config(text="Underweight")
    elif 18.5 <= bmi < 25:
        classification_label.config(text="Normal Weight")
    elif 25 <= bmi < 30:
        classification_label.config(text="Overweight")
    else:
        classification_label.config(text="Obese")

def store_data(weight, height, bmi):
    with open("user_data.txt", "a") as file:
        file.write(f"Weight: {weight} kg, Height: {height} m, BMI: {bmi:.2f}\n")

root = tk.Tk()
root.title("BMI Calculator")

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=0, column=0)

weight_entry = tk.Entry(root)
weight_entry.grid(row=0, column=1)

height_label = tk.Label(root, text="Height (m):")
height_label.grid(row=1, column=0)

height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2)

bmi_label = tk.Label(root, text="")
bmi_label.grid(row=3, columnspan=2)

classification_label = tk.Label(root, text="")
classification_label.grid(row=4, columnspan=2)

root.mainloop()
