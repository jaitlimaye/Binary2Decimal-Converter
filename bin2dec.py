import tkinter as tk

eq = ""
dec = ""
def dispdec(eq):
    global dec
    if(len(eq) > 0):
        dec = str(int(eq,2))
    else:
        dec = ""
    dec_text.config(text = dec)

def numpress(value):
    global eq
    if(len(eq) < 8):
        eq += value
        bin_text.config(text=eq)
        dispdec(eq)

def clear():
    global dec
    global eq
    eq = ""
    bin_text.config(text=eq)
    dec = ""
    dec_text.config(text = dec)

def bckspc():
    global eq
    if(len(eq) > 0):
        eq = eq[:-1]
        bin_text.config(text=eq)
        dispdec(eq)

window = tk.Tk()

window.geometry("300x275")
window.title("bin2dec")
window.resizable(False,False)
window.configure(bg="#17161b")
bin_text = tk.Label(window,height=2,width=25,text="",font=("Arial",24))
bin_text.pack()
dec_text = tk.Label(window,height=2,width=25,text="",font=("Arial",24))
dec_text.pack()

tk.Button(window,text="0",command=lambda: numpress("0"),width=5,font=("Arial",14)).place(x=10,y=200)
tk.Button(window,text="1",command=lambda: numpress("1"),width=5,font=("Arial",14)).place(x=80,y=200)
tk.Button(window,text="<",command=lambda: bckspc(),width=5,font=("Arial",14)).place(x=150,y=200)
tk.Button(window,text="C",command=lambda: clear(),width=5,font=("Arial",14)).place(x=220,y=200)
'''
btn_0 = tk.Button(window,text="0",command=lambda: test("0"),width=5,font=("Arial",14))
btn_0.grid(row=2,column=1)
btn_1 = tk.Button(window,text="1",command=lambda: test("1"),width=5,font=("Arial",14))
btn_1.grid(row=2,column=2)
btn_bck = tk.Button(window,text="<",command=lambda: test("back"),width=5,font=("Arial",14))
btn_bck.grid(row=2,column=3)
btn_clr = tk.Button(window,text="C",command=lambda: test("c"),width=5,font=("Arial",14))
btn_clr.grid(row=2,column=4)
'''
window.mainloop()

