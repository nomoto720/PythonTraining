import tkinter

rt=tkinter.Tk()
rt.geometry('300x200')

btn=tkinter.Button(rt,text='終了',width=14)
btn.pack(fill='x',padx=30,side='left')
btn2=tkinter.Button(rt,text='終了',width=14)
btn2.pack(fill='x',padx=30,side='left')
btn2=tkinter.Button(rt,text='終了')
btn2.pack(fill='x',padx=30)

rt.mainloop()
