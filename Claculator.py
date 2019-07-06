from tkinter import *
from math import *

pointer = 0

class createButton:
    def __init__(self, master, text, location, entry):
        self.button = Button(master, text=text, command=self.onClick)
        self.button.grid(row=location[0], column=location[1])

        self.text = text
        self.location = location
        self.entry = entry

    def onClick(self):
        global pointer
        if self.text == "Enter" or self.text == "Clear":
            pass
        else:
            if self.text == "./":
                self.entry.insert(pointer, "./(")
                pointer += len("./(")
            else:
                self.entry.insert(pointer, self.text)
                pointer += len(self.text)


def createEntry(master, row=0, column=0, columnspan=1):
    entry = Entry(master)
    entry.grid(row=row, column=column, columnspan=columnspan)
    return entry

def main():

    tk = Tk()

    entry = createEntry(tk, columnspan=5)

    #Numbers:
    button7 = createButton(tk, "7", (1, 0), entry)
    button8 = createButton(tk, "8", (1, 1), entry)
    button9 = createButton(tk, "9", (1, 2), entry)
    button4 = createButton(tk, "4", (2, 0), entry)
    button5 = createButton(tk, "5", (2, 1), entry)
    button6 = createButton(tk, "6", (2, 2), entry)
    button1 = createButton(tk, "1", (3, 0), entry)
    button2 = createButton(tk, "2", (3, 1), entry)
    button3 = createButton(tk, "3", (3, 2), entry)
    button0 = createButton(tk, "0", (4, 1), entry)

    #Signs
    buttonPlus = createButton(tk, "+", (1, 3), entry)
    buttonMinus = createButton(tk, "-", (1, 4), entry)
    buttonMulti = createButton(tk, "*", (2, 3), entry)
    buttonDivid = createButton(tk, "/", (2, 4), entry)
    buttonRoot = createButton(tk, "./", (3, 3), entry)
    buttonSqr = createButton(tk, "^(2)", (3, 4), entry)

    tk.mainloop()

if __name__ == "__main__":
    main()
