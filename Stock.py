from tkinter import *
from pymysql import *
from tkinter import messagebox as msg

class StockForm(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.lblitemid=Label(self,text="Item Id",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lblitemname=Label(self,text="Item Name",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lbldate=Label(self,text="Date On",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lblmeasurement=Label(self,text="Unit of Measurement",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lblquantity=Label(self,text="Quantity",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lblunitprice=Label(self,text="Unit Price",fg="darkgray",bg="lightblue",font=("sans-serif",16))

        self.txtitemid=Entry(self,fg="red",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtitemname=Entry(self,fg="red",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtdate=Entry(self,fg="red",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtmeasurement=Entry(self,fg="red",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtquantity=Entry(self,fg="red",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtunitprice=Entry(self,fg="red",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")

        self.b1=Button(self,text='Add Product',bg='lightblue',fg='red',font=('algerian',15),bd=6,command=self.additem)
        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.rowconfigure(index=4,pad=10)
        self.rowconfigure(index=5,pad=10)
        self.rowconfigure(index=6,pad=10)

        self.columnconfigure(index=0,pad=15)
        self.columnconfigure(index=1,pad=15)

        self.lblitemid.grid(row=0,column=0)
        self.txtitemid.grid(row=0,column=1)

        self.lblitemname.grid(row=1,column=0)
        self.txtitemname.grid(row=1,column=1)

        self.lbldate.grid(row=2,column=0)
        self.txtdate.grid(row=2,column=1)

        self.lblmeasurement.grid(row=3,column=0)
        self.txtmeasurement.grid(row=3,column=1)

        self.lblquantity.grid(row=4,column=0)
        self.txtquantity.grid(row=4,column=1)

        self.lblunitprice.grid(row=5,column=0)
        self.txtunitprice.grid(row=5,column=1)

        self.b1.grid(columnspan=2)
        self.pack()
    def additem(self):
        con=connect(db='mall',user='root',password='shivsql123',host='localhost')
        cur=con.cursor()
        itemid=int(self.txtitemid.get())
        itemname=self.txtitemname.get()
        sdate=self.txtdate.get()
        unit=self.txtmeasurement.get()
        qty=int(self.txtquantity.get())
        price=int(self.txtunitprice.get())
        try:
            i=cur.execute("insert into stock values(%d,'%s','%s','%s',%d,%d)"%(itemid,itemname,sdate,unit,qty,price))
            if(i==1):
                con.commit()
                msg.showinfo('Confirmation','Thanks to add item')
                con.close()
                self.txtitemid.delete(0,'end')
                self.txtitemname.delete(0,'end')
                self.txtdate.delete(0,'end')
                self.txtmeasurement.delete(0,'end')
                self.txtquantity.delete(0,'end')
                self.txtunitprice.delete(0,'end')
                self.txtitemid.focus()
        except MySQLError as me:
    
            msg.showerror('Error Box','OOPs something went wrong!!'+me)
            con.close()