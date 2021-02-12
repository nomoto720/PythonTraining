import tkinter as tk
def btn_click(x,y):
    x/y

root=tk.Tk()
root.title("割り勘くん")
root.geometry('400x200')

entry=tk.Entry(width=20)
entry.pack()

entry=tk.Entry(width=20)
entry.pack()

button=tk.Button(text="計算する",command=btn_click)
button.pack()
root.mainloop()
