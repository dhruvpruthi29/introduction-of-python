import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.geometry('400x300')

def cal_bmi():
    weight = float(e1.get())
    height = float(e2.get())
    print(weight)
    print(type(weight))
    print(height)
    print(type(height))
    
    bmi = weight/(height*height)
    bmi = round(bmi,2)
    message = 'BMI is: '+str(bmi)
    messagebox.showinfo('BMI' , message)
    
var1 = tk.Label(root, text='Enter Weight in Kg')
var1.pack()
e1 = tk.Entry(root)
e1.pack()
var2 = tk.Label(root, text='Enter Height in meter')
var2.pack()
e2 = tk.Entry(root)
e2.pack()
b1 = tk.Button(root, text='Calculate BMI', command = cal_bmi)   
b1.pack()
b2 = tk.Button(root, text='Exit Button', command = root.destroy)
b2.pack()
root.mainloop()