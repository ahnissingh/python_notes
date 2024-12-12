import tkinter as tk
from tkinter import ttk, messagebox

def submit_form():
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_var.get()
    hobbies = ', '.join([hobby for hobby in hobbies_list if hobbies_vars[hobby].get()])
    country = country_var.get()
    if not name or not age or not gender or country == "Select Country":
        messagebox.showerror("Error", "Please fill out all required fields!")
        return
    try:
        age = int(age)
    except ValueError:
        messagebox.showerror("Error", "Age must be a number!")
        return

    result = f"Name: {name}\nAge: {age}\nGender: {gender}\nHobbies: {hobbies}\nCountry: {country}"
    messagebox.showinfo("Form Submitted", result)

def reset_form():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    gender_var.set("None")
    for var in hobbies_vars.values():
        var.set(False)
    country_var.set("Select Country")

root = tk.Tk()
root.title("Simplified Form")
root.geometry("300x400")

# Name field
tk.Label(root, text="Name:").pack(anchor=tk.W, padx=10, pady=5)
name_entry = tk.Entry(root)
name_entry.pack(padx=10, pady=5)

# Age field
tk.Label(root, text="Age:").pack(anchor=tk.W, padx=10, pady=5)
age_entry = tk.Entry(root)
age_entry.pack(padx=10, pady=5)

# Gender selection
tk.Label(root, text="Gender:").pack(anchor=tk.W, padx=10, pady=5)
gender_var = tk.StringVar(value="None")
tk.Radiobutton(root, text="Male", variable=gender_var, value="Male").pack(anchor=tk.W, padx=20)
tk.Radiobutton(root, text="Female", variable=gender_var, value="Female").pack(anchor=tk.W, padx=20)

# Hobbies
tk.Label(root, text="Hobbies:").pack(anchor=tk.W, padx=10, pady=5)
hobbies_list = ["Reading", "Sports", "Music"]
hobbies_vars = {hobby: tk.BooleanVar() for hobby in hobbies_list}
for hobby in hobbies_list:
    tk.Checkbutton(root, text=hobby, variable=hobbies_vars[hobby]).pack(anchor=tk.W, padx=20)

# Country selection
tk.Label(root, text="Country:").pack(anchor=tk.W, padx=10, pady=5)
country_var = tk.StringVar(value="Select Country")
ttk.Combobox(root, textvariable=country_var, values=["Select Country", "India", "USA"]).pack(padx=10, pady=5)

# Buttons
tk.Button(root, text="Submit", command=submit_form).pack(side=tk.LEFT, padx=10, pady=10)
tk.Button(root, text="Reset", command=reset_form).pack(side=tk.LEFT, padx=10, pady=10)

root.mainloop()
