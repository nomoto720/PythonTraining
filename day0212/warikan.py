import tkinter as tk
def btn_click():
    global prices
    global nums
    prices=int(entry_money.get())
    nums=int(entry_nums.get())
    price=int(prices/nums/100)
    kanji=price*100+100
    price=int((prices-kanji)/(nums-1))
    str='1人あたあり',price,'円(',nums-1,'人),幹事は',kanji,'円です'
    label['text']=str
    label.update()
prices=None
nums=None

root=tk.Tk()
root.title("割り勘くん")
root.geometry('300x400')
root.configure(bg='skyblue')

label1=tk.Label(text='金額',bg='skyblue')
label1.pack(padx=5, pady=5, anchor=tk.W) 
entry_money=tk.Entry(width=20, relief=tk.RIDGE, bd=2)
entry_money.pack(padx=5, pady=5, anchor=tk.W)

label1=tk.Label(text='人数',bg='skyblue')
label1.pack(padx=5, pady=5, anchor=tk.W)
entry_nums=tk.Entry(width=20,relief=tk.RIDGE,bd=2)
entry_nums.pack(padx=5, pady=5, anchor=tk.W)

button=tk.Button(text="計算する",command=btn_click)
button.pack(padx=5, pady=20, anchor=tk.W)

label=tk.Label(text=' ',bg='skyblue')
label.pack(padx=5, pady=5, anchor=tk.W)

root.mainloop()
