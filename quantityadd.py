from tkinter import *
from pymysql import *
from tkinter import messagebox as msg

class AddQuantity(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.lblitemid=Label(self,text='Item Id',bg='lightblue',font=('sans-serif',16))
        self.lblquantity=Label(self,text='New Quantity',bg='lightblue',font=('sans-serif',16))

        self.txtitemid=Entry(self,bg='lightblue',font=('sans-serif',16),bd=6,justify='center')
        self.txtquantity=Entry(self,bg='lightblue',font=('sans-serif',16),bd=6,justify='center')

        self.b1=Button(self,text='Add Quantity',bg='lightblue',font=('sans-serif',16),bd=6,justify='center',command=self.addquantity)

        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)

        self.columnconfigure(index=0,pad=15)
        self.columnconfigure(index=1,pad=15)

        self.lblitemid.grid(row=0,column=0)
        self.txtitemid.grid(row=0,column=1)

        self.lblquantity.grid(row=1,column=0)
        self.txtquantity.grid(row=1,column=1)

        self.b1.grid(columnspan=2)

        self.pack()
    
    def addquantity(self):
        
        con=connect(db='mall',user='root',passwd='shivsql123',host='localhost')
        cur=con.cursor()
        itemid=int(self.txtitemid.get())
        qty=int(self.txtquantity.get())
        try:
            i=cur.execute("Update stock set quantity=quantity+%d where itemid=%d"%(qty,itemid))
            if(i==1):
                con.commit()
                msg.showinfo('Confirmation','Quantity Added')
                con.close()
                self.txtitemid.delete(0,'end')
                self.txtquantity.delete(0,'end')
                self.txtitemid.focus()
        except MySQLError as me:
            msg.showerror('Error','Oops! Something went wrong. '+me)
            con.close()
        