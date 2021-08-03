from tkinter import*

root=Tk()
root.title("Calculator")
root.geometry("410x480")

Font_tuple = ("Comic Sans MS", 25, "bold")

e=Entry(root,width=16,borderwidth=2,font=Font_tuple)
e.grid(row=0,column=0,columnspan=4,padx=10,pady=30)


def click(number):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def clear():
    e.delete(0,END)

def add():
    firstNumber=e.get()
    global fNum
    global math
    math="addition"
    fNum=int(firstNumber)
    e.delete(0,END)

def equal():
    secondNumber=e.get()
    e.delete(0,END)

    if math=="addition":
        e.insert(0,fNum+int(secondNumber))
    elif math=="multiplication":
        e.insert(0,fNum*int(secondNumber))
    elif math=="division":
        e.insert(0,fNum/int(secondNumber))
    elif math=="subtraction":
        e.insert(0,fNum-int(secondNumber))

def buttonMultiply():
    firstNumber=e.get()
    global fNum
    global math
    math="multiplication"
    fNum=int(firstNumber)
    e.delete(0,END)

def buttonDivide():
    firstNumber=e.get()
    global fNum
    global math
    math="division"
    fNum=int(firstNumber)
    e.delete(0,END)

def buttonSubtract():
    firstNumber=e.get()
    global fNum
    global math
    math="subtraction"
    fNum=int(firstNumber)
    e.delete(0,END)

#define img
#button.config(image=img)
img0=PhotoImage(file="butoane/0.png")
img1=PhotoImage(file="butoane/1.png")
img2=PhotoImage(file="butoane/2.png")
img3=PhotoImage(file="butoane/3.png")
img4=PhotoImage(file="butoane/4.png")
img5=PhotoImage(file="butoane/5.png")
img6=PhotoImage(file="butoane/6.png")
img7=PhotoImage(file="butoane/7.png")
img8=PhotoImage(file="butoane/8.png")
img9=PhotoImage(file="butoane/9.png")

delete=PhotoImage(file="butoane/del.png")
egal=PhotoImage(file="butoane/egal.png")
imp=PhotoImage(file="butoane/imp.png")
minus=PhotoImage(file="butoane/minus.png")
ori=PhotoImage(file="butoane/ori.png")
plus=PhotoImage(file="butoane/plus.png")



#define buttons
num1=Button(root,image=img1,font=Font_tuple,padx=23,pady=10,command=lambda: click(1),border=3,borderwidth=0)
num2=Button(root,image=img2,font=Font_tuple,padx=23,pady=10,command=lambda: click(2),border=3,borderwidth=0)
num3=Button(root,image=img3,font=Font_tuple,padx=23,pady=10,command=lambda: click(3),border=3,borderwidth=0)
num4=Button(root,image=img4,font=Font_tuple,padx=23,pady=10,command=lambda: click(4),border=3,borderwidth=0)
num5=Button(root,image=img5,font=Font_tuple,padx=23,pady=10,command=lambda: click(5),border=3,borderwidth=0)
num6=Button(root,image=img6,font=Font_tuple,padx=23,pady=10,command=lambda: click(6),border=3,borderwidth=0)
num7=Button(root,image=img7,font=Font_tuple,padx=23,pady=10,command=lambda: click(7),border=3,borderwidth=0)
num8=Button(root,image=img8,font=Font_tuple,padx=23,pady=10,command=lambda: click(8),border=3,borderwidth=0)
num9=Button(root,image=img9,font=Font_tuple,padx=23,pady=10,command=lambda: click(9),border=3,borderwidth=0)
num0=Button(root,image=img0,font=Font_tuple,padx=23,pady=10,command=lambda: click(0),border=3,borderwidth=0)

equal=Button(root,image=egal,padx=23,pady=10,border=3,font=Font_tuple,command=equal,borderwidth=0)
buttonAdd=Button(root,image=plus,padx=23,pady=10,border=3,font=Font_tuple,command=add,borderwidth=0)
clear=Button(root,image=delete,padx=23,pady=10,border=3,font=Font_tuple,command=clear,borderwidth=0)
multiply=Button(root,image=ori,padx=23,pady=10,border=3,font=Font_tuple,command=buttonMultiply,borderwidth=0)
divide=Button(root,image=imp,padx=23,pady=10,border=3,font=Font_tuple,command=buttonDivide,borderwidth=0)
subtract=Button(root,image=minus,padx=23,pady=10,border=3,font=Font_tuple,command=buttonSubtract,borderwidth=0)

num1.grid(row=1,column=0)
num2.grid(row=1,column=1)
num3.grid(row=1,column=2)

num4.grid(row=2,column=0)
num5.grid(row=2,column=1)
num6.grid(row=2,column=2)

num7.grid(row=3,column=0)
num8.grid(row=3,column=1)
num9.grid(row=3,column=2)

num0.grid(row=4,column=0)
equal.grid(row=4,column=2)
clear.grid(row=4,column=1)
multiply.grid(row=1,column=3)
divide.grid(row=2,column=3)
buttonAdd.grid(row=3,column=3)
subtract.grid(row=4,column=3)

root.mainloop()