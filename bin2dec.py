import tkinter as tk

def test(name):
    print(name)
window = tk.Tk()

window.geometry("300x275")
dec_text = tk.Text(window,height=2,width=18,font=("Arial",24))
dec_text.grid(columnspan=5)
bin_text = tk.Text(window,height=2,width=18,font=("Arial",24))
bin_text.grid(columnspan=5)

btn_0 = tk.Button(window,text="0",command=lambda: test("0"),width=5,font=("Arial",14))
btn_0.grid(row=2,column=1)
btn_1 = tk.Button(window,text="1",command=lambda: test("1"),width=5,font=("Arial",14))
btn_1.grid(row=2,column=2)
btn_bck = tk.Button(window,text="<",command=lambda: test("back"),width=5,font=("Arial",14))
btn_bck.grid(row=2,column=3)
btn_clr = tk.Button(window,text="C",command=lambda: test("c"),width=5,font=("Arial",14))
btn_clr.grid(row=2,column=4)
window.mainloop()

