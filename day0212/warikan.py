import tkinter as tk
def btn_click(x,y):
    x/y

root=tk.Tk()
root.title("割り勘くん")
root.geometry('600x600')

button=tk.Button(text="計算する")
button.place(x=10,y=200)
root.mainloop()
