from tkinter import Tk, Entry, Button, StringVar
import math

class Calculator:
    def __init__(self, master):
        master.title('Advanced Calculator')
        master.geometry('400x500+100+100')
        master.config(bg='#2b2b2b')
        master.resizable(False, False)

        self.equation = StringVar()
        self.entry_value = ''
        Entry(width=24, bg='#f0f0f0', font=('Arial Bold', 24), textvariable=self.equation, justify='right').place(x=10, y=10)

        # Row 1
        Button(width=10, height=2, text='C', relief='flat', bg='#ff6666', fg='white', command=self.clear).place(x=10, y=70)
        Button(width=10, height=2, text='√', relief='flat', bg='#6699ff', fg='white', command=lambda: self.show('math.sqrt(')).place(x=105, y=70)
        Button(width=10, height=2, text='x²', relief='flat', bg='#6699ff', fg='white', command=lambda: self.show('**2')).place(x=200, y=70)
        Button(width=10, height=2, text='/', relief='flat', bg='#ffa64d', fg='white', command=lambda: self.show('/')).place(x=295, y=70)

        # Row 2
        Button(width=10, height=2, text='7', relief='flat', bg='#ffffff', command=lambda: self.show(7)).place(x=10, y=140)
        Button(width=10, height=2, text='8', relief='flat', bg='#ffffff', command=lambda: self.show(8)).place(x=105, y=140)
        Button(width=10, height=2, text='9', relief='flat', bg='#ffffff', command=lambda: self.show(9)).place(x=200, y=140)
        Button(width=10, height=2, text='*', relief='flat', bg='#ffa64d', fg='white', command=lambda: self.show('*')).place(x=295, y=140)

        # Row 3
        Button(width=10, height=2, text='4', relief='flat', bg='#ffffff', command=lambda: self.show(4)).place(x=10, y=210)
        Button(width=10, height=2, text='5', relief='flat', bg='#ffffff', command=lambda: self.show(5)).place(x=105, y=210)
        Button(width=10, height=2, text='6', relief='flat', bg='#ffffff', command=lambda: self.show(6)).place(x=200, y=210)
        Button(width=10, height=2, text='-', relief='flat', bg='#ffa64d', fg='white', command=lambda: self.show('-')).place(x=295, y=210)

        # Row 4
        Button(width=10, height=2, text='1', relief='flat', bg='#ffffff', command=lambda: self.show(1)).place(x=10, y=280)
        Button(width=10, height=2, text='2', relief='flat', bg='#ffffff', command=lambda: self.show(2)).place(x=105, y=280)
        Button(width=10, height=2, text='3', relief='flat', bg='#ffffff', command=lambda: self.show(3)).place(x=200, y=280)
        Button(width=10, height=2, text='+', relief='flat', bg='#ffa64d', fg='white', command=lambda: self.show('+')).place(x=295, y=280)

        # Row 5
        Button(width=10, height=2, text='.', relief='flat', bg='#ffffff', command=lambda: self.show('.')).place(x=10, y=350)
        Button(width=10, height=2, text='0', relief='flat', bg='#ffffff', command=lambda: self.show(0)).place(x=105, y=350)
        Button(width=10, height=2, text='1/x', relief='flat', bg='#6699ff', fg='white', command=lambda: self.show('1/')).place(x=200, y=350)
        Button(width=10, height=2, text='=', relief='flat', bg='#66cc66', fg='white', command=self.solve).place(x=295, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
            self.entry_value = str(result)
        except Exception as e:
            self.equation.set("Error")
            self.entry_value = ''

root = Tk()
calculator = Calculator(root)
root.mainloop()
