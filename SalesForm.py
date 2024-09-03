from datetime import *
from tkinter import *
from pymysql import *
from tkinter import messagebox as msg
class Sales(Frame):
    def __init__(self,abc):
        super().__init__(abc)
        dt=datetime.now()
        self.ndate=str(dt.year)+"-"+str(dt.month)+"-"+str(dt.day)

        self.lblcustomerid=Label(self,text='Customer Id',bg='gray',fg="purple",font=('sans-serif',16))
        self.lblcustomername=Label(self,text='Customer Name',bg='gray',fg="purple",font=('sans-serif',16))
        self.lblsaledate=Label(self,text='Sale Date',bg='gray',fg="purple",font=('sans-serif',16))
        self.lblitemid=Label(self,text='Item Id',bg='gray',fg="purple",font=('sans-serif',16))
        self.lblquantity=Label(self,text='Purchage Quantity',bg='gray',fg="purple",font=('sans-serif',16))
        self.lblunitprice=Label(self,text='Unit Price',bg='gray',fg="purple",font=('sans-serif',16))
        self.lbltotalprice=Label(self,text='Total Price',bg='gray',fg="purple",font=('sans-serif',16))

        self.txtcustomerid=Entry(self,bg='gray',fg="purple",font=('sans-serif',16),bd=6,justify='center')
        self.txtcustomername=Entry(self,bg='gray',fg="purple",font=('sans-serif',16),bd=6,justify='center')
        self.txtsaledate=Entry(self,bg='gray',fg="purple",font=('sans-serif',16),bd=6,justify='center')
        self.txtitemid=Entry(self,bg='gray',fg="purple",font=('sans-serif',16),bd=6,justify='center')
        self.txtitemid.bind("<Return>",self.search)
        self.txtquantity=Entry(self,bg='gray',fg="purple",font=('sans-serif',16),bd=6,justify='center')
        self.txtquantity.bind("<Return>",self.calc)
        self.txtunitprice=Entry(self,bg='gray',fg="purple",font=('sans-serif',16),bd=6,justify='center')
        
        self.txttotalprice=Entry(self,bg='gray',fg="purple",font=('sans-serif',16),bd=6,justify='center')
        self.txtsaledate.insert(0,self.ndate)
        self.b1=Button(self,text='Submit',bg='gray',fg="purple",font=('sans-serif',16),bd=6,justify='center',command=self.salessave)

        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.rowconfigure(index=4,pad=10)
        self.rowconfigure(index=5,pad=10)
        self.rowconfigure(index=6,pad=10)
        self.rowconfigure(index=7,pad=10)

        self.columnconfigure(index=0,pad=15)
        self.columnconfigure(index=1,pad=15)

        self.lblcustomerid.grid(row=0,column=0)
        self.txtcustomerid.grid(row=0,column=1)

        self.lblcustomername.grid(row=1,column=0)
        self.txtcustomername.grid(row=1,column=1)

        self.lblsaledate.grid(row=2,column=0)
        self.txtsaledate.grid(row=2,column=1)

        self.lblitemid.grid(row=3,column=0)
        self.txtitemid.grid(row=3,column=1)

        self.lblquantity.grid(row=4,column=0)
        self.txtquantity.grid(row=4,column=1)

        self.lblunitprice.grid(row=5,column=0)
        self.txtunitprice.grid(row=5,column=1)

        self.lbltotalprice.grid(row=6,column=0)
        self.txttotalprice.grid(row=6,column=1)

        self.b1.grid(columnspan=2)
        self.pack()
    def conn(self):
        con=connect(db='mall',user='root',password='shivsql123',host='localhost')
        return con
    def search(self,event):
        con=self.conn()
        cur=con.cursor()
        itemid=int(self.txtitemid.get())
        cur.execute("select unit_price from stock where itemid=%d"%(itemid))
        data=cur.fetchone()
        self.txtunitprice.insert(0,data[0])
        con.close()
    def calc(self,event):
        qty=int(self.txtquantity.get())
        price=int(self.txtunitprice.get())
        tprice=qty*price
        self.txttotalprice.insert(0,str(tprice))
    def salessave(self):
        con=self.conn()
        cur=con.cursor()
        cid=int(self.txtcustomerid.get())
        cname=self.txtcustomername.get()
        sdate=self.txtsaledate.get()
        itemid=int(self.txtitemid.get())
        qty=int(self.txtquantity.get())
        uprice=int(self.txtunitprice.get())
        tprice=int(self.txttotalprice.get())
        i=cur.execute("update stock set stock_date='%s',quantity=quantity-%d where itemid=%d"%(sdate,qty,itemid))
        if(i==1):
            j=cur.execute("insert into sales values(%d,'%s','%s',%d,%d,%d,%d)"%(cid,cname,sdate,itemid,qty,uprice,tprice))
            if(j==1):
                con.commit()
                con.close()
                msg.showinfo('Confirmation','Thanks ')

