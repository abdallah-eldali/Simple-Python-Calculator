from tkinter import *
from math import *

pointer = 0

#-----------------------------------------------------------------------

class createButton:
    def __init__(self, master, text, location, entry):
        self.button = Button(master, text=text, command=self.onClick)
        self.button.grid(row=location[0], column=location[1])

        self.text = text
        self.location = location
        self.entry = entry

    def onClick(self):
        global pointer
        if self.text == "Enter":
            pass
        elif self.text == "Clear":
            self.entry.delete(0, pointer)
            pointer = 0
        else:
            if self.text == "./":
                self.entry.insert(pointer, "./(")
                pointer += len("./(")
            else:
                self.entry.insert(pointer, self.text)
                pointer += len(self.text)

#-----------------------------------------------------------------------

def createEntry(master, row=0, column=0, columnspan=1):
    entry = Entry(master)
    entry.grid(row=row, column=column, columnspan=columnspan)
    return entry

def calculate(entry):
    inputCalculation = entry.get()
    if "./" in inputCalculation:
        calculation = inputCalculation.replace("./", "sqrt")
    if "^" in inputCalculation:
        calculation = inputCalculation.replace("^", "**")
    
    return str(eval(calculation))

def main():

    tk = Tk()

    entry = createEntry(tk, columnspan=3)

    #Numbers:
    button0 = createButton(tk, "0", (4, 1), entry)

    numberList = ["7", "8", "9", "4", "5", "6", "1", "2", "3"]
    pointer = 0

    for rows in range(1, 4):
        for columns in range(3):
            print(rows, columns)
            print(numberList[pointer])
            button = createButton(tk, numberList[pointer], (rows, columns), entry)
            pointer += 1


    #Signs
    buttonPlus = createButton(tk, "+", (1, 3), entry)
    buttonMinus = createButton(tk, "-", (1, 4), entry)
    buttonMulti = createButton(tk, "*", (2, 3), entry)
    buttonDivid = createButton(tk, "/", (2, 4), entry)
    buttonRoot = createButton(tk, "./", (3, 3), entry)
    buttonSqr = createButton(tk, "^(2)", (3, 4), entry)

    #Enter & Clear
    butttonEnter = createButton(tk, "Enter", (4, 0), entry)
    buttonClear = createButton(tk, "Clear", (4, 2), entry)

    #Checking
    res = Label(tk)
    res.grid(row=0, column=3, columnspan=2)

    res.configure(text="= ")




    tk.mainloop()

if __name__ == "__main__":
    main()
