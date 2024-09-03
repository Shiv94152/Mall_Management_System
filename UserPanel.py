from tkinter import *
from SalesForm import *
class UserMenu(Frame):
    def __init__(self,local):
        super().__init__(local)
        
        self.menubar=Menu(self)
        
        self.filemenu=Menu(self.menubar,tearoff=0)
        
        self.filemenu.add_command(label='Sale Product',command=self.method11)
        self.filemenu.add_command(label='Recipts Print')
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit',command=self.close)
        
        
        
        self.menubar.add_cascade(label='User Menu',underline=1,menu=self.filemenu)
        
        self.pack()
    def close(self):
        exit()
    def method11(self):
        root=Tk()
        ob=Sales(root)
        root.geometry('480x550')
        root.mainloop()
