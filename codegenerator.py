import tkinter as tk
from tkinter import *
import qrcode
from PIL import Image, ImageTk
root = tk.Tk()
global var1
root.geometry('500x500')
def create_qr():
    global var1
    var1.destroy()
    x = e1.get()
    y = qrcode.make(x)
    y.save('myqr.jpg')
    photo = Image.open('myqr.jpg')
    ph = ImageTk.PhotoImage(photo)
    var1 = tk.Label(root, image=ph)
    var1.image = ph
    var1.pack()
e1 = tk.Entry(root)
e1.pack()
b1 = tk.Button(root, text='Generate QR Code', command=create_qr)
b1.pack()
var1 = tk.Label(root,image='')
var1.pack()
root.mainloop()