import tkinter as tk
root = tk.Tk()
root.geometry()
def test_number():
    x = int(e1.get())
    if(x%2==0):
        var2 = tk.Label(root, text='Even Number')
        var2.grid(row=2, column=1)
        
    else:
        var2 = tk.Label(root, text='Odd Number')
        var2.grid(row=2, column=1)
        
var1 = tk.Label(root, text='Enter a Number')
var1.grid(row=0, column=0, padx = 20, pady = 20)
e1 = tk.Entry(root)
e1.grid(row=0, column=1, padx=20, pady=20)
b1 = tk.Button(root, text='Test Number' , command=test_number)
b1.grid(row=1,column=0,columnspan=2 , padx=20, pady=20)
root.mainloop()