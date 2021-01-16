from tkinter import *
from tkinter.ttk import *

class BasicCalculator():
    
    def __init__(self):
        self.root = Tk()
        self.root.title('FrmBasicCalculator')
        self.root.geometry('250x250')

        self.label = Label(text='Basic Calculator')
        self.label.pack()

        self.option_menu_list = ['+', '-', '*', '/']
        self.variable = StringVar(self.root)
        self.variable.set([0]) #set default to +

        self.first_input = IntVar()
        self.second_input = IntVar()
        
        self.entry1 = Entry(textvariable=self.first_input)
        self.dropdown_menu = OptionMenu(self.root, self.variable, *self.option_menu_list)
        self.entry2 = Entry(textvariable=self.second_input)

        self.entry1.pack()
        self.dropdown_menu.pack()
        self.entry2.pack()

        self.compute_btn = Button(self.root, text='compute', command=self.calculate)
        self.compute_btn.pack()

        self.total_label = Label(self.root, text='Total : \n 0')
        self.total_label.pack()
        
        self.root.mainloop()

    def calculate(self):

        get_operation = self.variable.get()

        if get_operation == '+':
            sum = int(self.entry1.get()) + int(self.entry2.get())
            label = self.total_label.configure(text='Total \n' + str(sum))

        elif get_operation == '-':
            difference = int(self.entry1.get()) - int(self.entry2.get())
            label = self.total_label.configure(text='Total \n' + str(difference))
            
        elif get_operation == '*':
            result = int(self.entry1.get()) * int(self.entry2.get())
            label = self.total_label.configure(text='Total \n' + str(result))
        
        else:
            quotient = int(self.entry1.get()) / int(self.entry2.get())
            label = self.total_label.configure(text='Total \n' + str(quotient))
        
app = BasicCalculator()
