from tkinter import *
from math import *

testing = Tk()
w = Entry(testing)

index = 0

def onClick0():
    global index
    w.insert(index, "0")
    index += 1

def onClick1():
    global index
    w.insert(index, "1")
    index += 1

def onClick2():
    global index
    w.insert(index, "2")
    index += 1

def onClick3():
    global index
    w.insert(index, "3")
    index += 1
     

def onClick4():
    global index
    w.insert(index, "4")
    index += 1

def onClick5():
    global index
    w.insert(index, "5")
    index += 1

def onClick6():
    global index
    w.insert(index, "6")
    index += 1
     

def onClick7():
    global index
    w.insert(index, "7")
    index += 1

def onClick8():
    global index
    w.insert(index, "8")
    index += 1

def onClick9():
    global index
    w.insert(index, "9")
    index += 1

def onClickPlus():
    global index
    w.insert(index, "+")
    index += 1

def onClickMinus():
    global index
    w.insert(index, "-")
    index += 1

def onClickDivid():
    global index
    w.insert(index, "/")
    index += 1

def onClickMulti():
    global index
    w.insert(index, "*")
    index += 1

def onClickRoot():
    global index
    w.insert(index, "./")
    index += 2

def onClickSqr():
    global index
    w.insert(index, "^(2)")
    index += 4

def onClickOpenBracket():
    global index
    w.insert(index, "(")
    index += 1

def onClickCloseBracket():
    global index
    w.insert(index, ")")
    index += 1

def onClickClear():
    global index
    w.delete(first=0, last=index)
    index = 0

def onClickEnter():
    global index
    calculation = w.get()
    if "./" in calculation:
        calculation = calculation.replace("./", "sqrt")
    elif "^" in calculation:
        calculation = calculation.replace("^", "**")
    answer = str(eval(calculation))
    onClickClear()
    w.insert(0, answer)
    index = len(answer)



button0 = Button(testing, text="0", command=onClick0)
button1 = Button(testing, text="1", command=onClick1)
button2 = Button(testing, text="2", command=onClick2)
button3 = Button(testing, text="3", command=onClick3)
button4 = Button(testing, text="4", command=onClick4)
button5 = Button(testing, text="5", command=onClick5)
button6 = Button(testing, text="6", command=onClick6)
button7 = Button(testing, text="7", command=onClick7)
button8 = Button(testing, text="8", command=onClick8)
button9 = Button(testing, text="9", command=onClick9)

buttonPlus = Button(testing, text="+", command=onClickPlus)
buttonMinus = Button(testing, text="-", command=onClickMinus)
buttonMulti = Button(testing, text="*", command=onClickMulti)
buttonDivid =  Button(testing, text="/", command=onClickDivid)
buttonRoot = Button(testing, text="./", command=onClickRoot)
buttonSqr = Button(testing, text="^2", command=onClickSqr)
buttonOpenBracket = Button(testing, text="(", command=onClickOpenBracket)
buttonCloseBracket = Button(testing, text=")", command=onClickCloseBracket)

buttonEnter = Button(testing, text="Enter", command=onClickEnter)
buttonClear = Button(testing, text="Clear", command=onClickClear)

w.grid(row=4, column=0, columnspan=5)

button0.grid(row=3, column=1)
button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button7.grid(row=0, column=0)
button8.grid(row=0, column=1)
button9.grid(row=0, column=2)

buttonPlus.grid(row=3, column=0)
buttonMinus.grid(row=3, column=2)
buttonMulti.grid(row=0, column=3)
buttonDivid.grid(row=0, column=4)
buttonRoot.grid(row=1, column=3)
buttonSqr.grid(row=1, column=4)
buttonOpenBracket.grid(row=2, column=3)
buttonCloseBracket.grid(row=2, column=4)

buttonEnter.grid(row=5, column=0, columnspan=3)
buttonClear.grid(row=5, column=2, columnspan=2)

testing.mainloop()
