from tkinter import *

win = Tk()
win.geometry("300x400")
win.title("Calculator")

uservalue = StringVar()
uservalue.set("")
userentry = Entry(win, textvariable=uservalue, font="lucida 20 bold")
userentry.pack(padx=10, pady=10)

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        if uservalue.get().isdigit():
            value = int(uservalue.get())
        else:
            try:
                value = eval(uservalue.get())
            except:
                value = "Error"

        uservalue.set(value)
        userentry.update()
    elif text == "C":
        uservalue.set("")
        userentry.update()
    else:
        uservalue.set(uservalue.get() + text)
        userentry.update()

list = ["7","8","9","4","5","6","1","2","3","+","0","/",".","%","-","*","C","="]

for i in range(0,6):
    f = Frame(win)
    b1 = Button(f, text=list[i*3], font="lucida 15 bold", width=5)
    b1.pack(side=LEFT, fill=X)
    b1.bind("<Button-1>", click)

    b1 = Button(f, text=list[i*3 + 1], font="lucida 15 bold", width=5)
    b1.pack(side=LEFT, fill=X)
    b1.bind("<Button-1>", click)

    b1 = Button(f, text=list[i*3 + 2], font="lucida 15 bold", width=5)
    b1.pack(side=LEFT, fill=X)
    b1.bind("<Button-1>", click)
    
    f.pack()

win.configure(bg='black')
win.mainloop()