from tkinter import *
from NewUser import *
from Stock import *
from StockModification import *
from quantityadd import *
from modifyuser import *

class MyMenu(Frame):
    def __init__(self,local):
        super().__init__(local)
        
        self.menubar=Menu(self)
        
        self.filemenu=Menu(self.menubar,tearoff=0)
        
        self.filemenu.add_command(label='Register',command=self.method1)
        self.filemenu.add_command(label='Add Product',command=self.method2)
        self.filemenu.add_command(label='Product Modify',command=self.method3)
        self.filemenu.add_command(label='Quantity Add',command=self.method4)
        self.filemenu.add_command(label='Employee Modify',command=self.method5)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit',command=self.close)
        
        
        
        self.menubar.add_cascade(label='Mall Menu',underline=1,menu=self.filemenu)
        
        self.pack()
    def close(self):
        exit()
    def method1(self):
        root1=Tk()
        ob=Registration(root1)
        root1.geometry('480x450')
        root1.title('Registration Form')
        root1.mainloop()
    def method2(self):
        root2=Tk()
        ob=StockForm(root2)
        root2.geometry('480x400')
        root2.mainloop()
    def method3(self):
        root3=Tk()
        ob=StockModificationForm(root3)
        root3.geometry('480x350')
        root3.mainloop()
        
    def method4(self):
        root4=Tk()
        ob=AddQuantity(root4)
        root4.geometry('480x350')
        root4.mainloop()
        
    def method5(self):
        root5=Tk()
        ob=ModifyUser(root5)
        root5.geometry('480x350')
        root5.mainloop()