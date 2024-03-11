import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

#Connect to SQLite database
conn=sqlite3.connect('bmi_data.db')
c=conn.cursor()

#Create table
c.execute('''CREATE TABLE IF NOT EXISTS bmi_records
          (id INTEGER PRIMARY KEY,
          weight REAL,
          height REAL,
          bmi REAL,
          category TEXT)''')
conn.commit()

def calculate_bmi(weight,height):
    return weight/((height/100)**2)

def classify_bmi(bmi):
    if bmi<18.5:
        return "Underweight"
    elif 18.5<=bmi<25:
        return "Normal Weight"
    elif 25<=bmi<30:
        return "Overweight"
    else:
        return "Obese"
    
def save_bmi(weight,height,bmi,category):
    c.execute('''INSERT INTO bmi_records(weight, height, bmi, category) 
                 VALUES (?, ?, ?, ?)''',(weight, height, bmi, category))
    conn.commit()

def on_calculate():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi=calculate_bmi(weight,height)
        category = classify_bmi(bmi)
        result_label.config(text=f"Your BMI is: {bmi:.2f} ({category})", fg="blue")
        save_bmi(weight,height,bmi,category)
    except ValueError:
        messagebox.showerror("Error","Please enter valid weight and height.")

#GUI
root=tk.Tk()
root.title("BMI Calculator")
root.configure(background="#f0f0f0")

frame=tk.Frame(root,bg="#f0f0f0")
frame.pack(padx=10,pady=10)

#Load and display BMI Logo
bmi_logo=Image.open("bmi.png")
bmi_logo=bmi_logo.resize((50,50),Image.LANCZOS)
bmi_logo=ImageTk.PhotoImage(bmi_logo)
bmi_logo_label=tk.Label(frame, image=bmi_logo, bg="#f0f0f0")
bmi_logo_label.grid(row=0, column=0, padx=10, pady=10)

#Add Heading
heading_label=tk.Label(frame, text="BMI Calculator", font=("Helvetica",16,"bold"))
heading_label.grid(row=0, column=1, columnspan=2, pady=10)

weight_label=tk.Label(frame, text="Weight (kg):", bg="#f0f0f0")
weight_label.grid(row=1, column=0, padx=5, pady=5)

weight_entry=tk.Entry(frame)
weight_entry.grid(row=1, column=1, padx=5, pady=5)

height_label=tk.Label(frame, text="Height (cm):", bg="#f0f0f0")
height_label.grid(row=2, column=0, padx=5, pady=5)

height_entry=tk.Entry(frame)
height_entry.grid(row=2, column=1, padx=5, pady=5)

calculate_button=tk.Button(frame, text="Calculate BMI", command=on_calculate)
calculate_button.grid(row=3, columnspan=2, pady=10)

result_label=tk.Label(frame, text="", bg="#f0f0f0", font=("Helvetica",16,"bold"))
result_label.grid(row=4, columnspan=2)

#Add labels for BMI Categories
underweight_label=tk.Label(frame, text="Underweight: BMI < 18.5", bg="#f0f0f0")
underweight_label.grid(row=5, columnspan=2, pady=5)

normalweight_label=tk.Label(frame, text="Normal weight: 18.5 <= BMI < 25", bg="#f0f0f0")
normalweight_label.grid(row=6, columnspan=2, pady=5)

overweight_label=tk.Label(frame, text="Overweight: 25 <= BMI < 30", bg="#f0f0f0")
overweight_label.grid(row=7, columnspan=2, pady=5)

obese_label=tk.Label(frame, text="Obese: BMI >= 30", bg="#f0f0f0")
obese_label.grid(row=8, columnspan=2, pady=5)

root.mainloop()

