import tkinter as tk
root = tk.Tk()
root.geometry('400x300')
def send_message():
    print('Hello from GUI')
b1 = tk.Button(root, text='Send Message', command=send_message)
b1.pack()
b2 = tk.Button(root, text='Exit Button', command=root.destroy)
b2.pack()
root.mainloop()