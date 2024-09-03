from tkinter import *
from pymysql import *
from tkinter import messagebox as msg

class StockModificationForm(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.lblitemid=Label(self,text="Item Id",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lbldate=Label(self,text="Date On",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lblquantity=Label(self,text="New Quantity",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lblunitprice=Label(self,text="Unit Price",fg="darkgray",bg="lightblue",font=("sans-serif",16))

        self.txtitemid=Entry(self,fg="red",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtdate=Entry(self,fg="red",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtquantity=Entry(self,fg="red",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtunitprice=Entry(self,fg="red",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")

        self.b1=Button(self,text='Update Product',bg='lightblue',fg='red',font=('algerian',15),bd=6,command=self.modifyitem)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.rowconfigure(index=4,pad=10)
        
        self.columnconfigure(index=0,pad=15)
        self.columnconfigure(index=1,pad=15)

        self.lblitemid.grid(row=0,column=0)
        self.txtitemid.grid(row=0,column=1)

        
        self.lbldate.grid(row=1,column=0)
        self.txtdate.grid(row=1,column=1)

        
        self.lblquantity.grid(row=2,column=0)
        self.txtquantity.grid(row=2,column=1)

        self.lblunitprice.grid(row=3,column=0)
        self.txtunitprice.grid(row=3,column=1)

        self.b1.grid(columnspan=2)
        self.pack()
    def modifyitem(self):
        con=connect(db='mall',user='root',password='shivsql123',host='localhost')
        cur=con.cursor()
        itemid=int(self.txtitemid.get())
        sdate=self.txtdate.get()
        qty=int(self.txtquantity.get())
        price=int(self.txtunitprice.get())
        try:
            i=cur.execute("update stock set stock_date='%s',quantity=quantity+%d,unit_price=%d where itemid=%d"%(sdate,qty,price,itemid))
            if(i==1):
                con.commit()
                msg.showinfo('Confirmation','Item Modified')
                con.close()
                self.txtitemid.delete(0,'end')
                self.txtdate.delete(0,'end')
                self.txtquantity.delete(0,'end')
                self.txtunitprice.delete(0,'end')
                self.txtitemid.focus()
        except MySQLError as me:
            msg.showerror('Error Box',me)