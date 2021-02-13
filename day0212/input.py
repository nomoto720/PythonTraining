import tkinter as tk
import tkinter.messagebox as mbox
def btn_click():
    global alcohol
    global degree
    global water
    alcohol=entry_alcohol.get()
    degree=entry_degree.get()
    water=entry_water.get()    
    if alcohol=='' or degree=='' or water=='':
        mbox.showinfo('情報','入力してください')
    else:
        alcohol=int(alcohol)
        degree=int(degree)/100
        water=int(water)
        alcohol_degree=int((degree*alcohol)/(alcohol+water)*100)
        msg=alcohol_degree
        label1['text']='アルコール度数は'
        label1.update()
        label2['text']=msg
        label2.update()
        label3['text']='度です'
        label3.update()
def  btn_clear():
        entry_alcohol.delete(0, tk.END)    
        entry_degree.delete(0, tk.END)    
        entry_water.delete(0, tk.END)    
        label1['text']=''
        label1.update()
        label2['text']=''
        label2.update()
        label3['text']=''
        label3.update()
    
alcohol=None
degree=None
water=None

root=tk.Tk()
root.title("水割りアルコール度数計算機")
root.geometry('300x400')
root.resizable(0,0)
root.configure(bg='lemonchiffon')

label1=tk.Label(text='水割りアルコール度数計算',bg='lightseagreen',font=("Arial", 12,'bold'),fg='white',width=300)
label1.pack() 


f1 = tk.Frame()
label1=tk.Label(text='お酒の量(ml)',bg='lemonchiffon',font=("Arial",10))
label1.pack(padx=5, pady=5, anchor=tk.W) 
entry_alcohol=tk.Entry(width=20, relief=tk.RIDGE, bd=2)
entry_alcohol.pack(padx=5, pady=5, anchor=tk.W)

label1=tk.Label(text='アルコール度数',bg='lemonchiffon',font=("Arial",10))
label1.pack(padx=5, pady=5, anchor=tk.W)
entry_degree=tk.Entry(width=20,relief=tk.RIDGE,bd=2)
entry_degree.pack(padx=5, pady=5, anchor=tk.W)

label1=tk.Label(text='割るお水の量(ml)',bg='lemonchiffon',font=("Arial",10))
label1.pack(padx=5, pady=5, anchor=tk.W)
entry_water=tk.Entry(width=20,relief=tk.RIDGE,bd=2)
entry_water.pack(padx=5, pady=5, anchor=tk.W)
f1.pack(padx=5,pady=10,anchor=tk.W)


button=tk.Button(text="計算する",width=8,font=("Arial",10,'bold'),bg='darkorange',fg='white',command=btn_click)
button.pack(padx=5, pady=5, anchor=tk.W)
button=tk.Button(text="クリア",width=8,font=("Arial",10,'bold'),bg='lightseagreen',fg='white',command=btn_clear)
button.pack(padx=5, pady=5, anchor=tk.W)

label1=tk.Label(text='',font=("Arial",10,),bg='lemonchiffon')
label1.pack(padx=5, pady=10, anchor=tk.W,side='left')
label2=tk.Label(text='',font=("Arial",20,),bg='lemonchiffon',fg='red')
label2.pack(padx=5, pady=10, anchor=tk.W,side='left')
label3=tk.Label(text='',font=("Arial",10,),bg='lemonchiffon')
label3.pack(padx=5, pady=10, anchor=tk.W,side='left')


root.mainloop()
