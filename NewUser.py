from tkinter import *
from pymysql import *
from tkinter import messagebox as msg

class Registration(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.lblempid=Label(self,text="Emplyee No",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lblename=Label(self,text="Employee Name",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        
        self.lbldesig=Label(self,text="Designation",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        
        self.lbluserid=Label(self,text="User Name",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lblpassword=Label(self,text="Password",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lblutype=Label(self,text="User Type",fg="darkgray",bg="lightblue",font=("sans-serif",16))

        self.txtempid=Entry(self,fg="darkgray",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtename=Entry(self,fg="darkgray",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtdesig=Entry(self,fg="darkgray",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtutype=Entry(self,fg="darkgray",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtuserid=Entry(self,fg="darkgray",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtpassword=Entry(self,show='*',fg="darkgray",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")

        self.btnsubmit=Button(self,text='Register',bg="lightblue",font=("sans-serif",16),bd=6,justify="center",command=self.register)
        

        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.rowconfigure(index=4,pad=10)
        self.rowconfigure(index=5,pad=10)
        self.rowconfigure(index=6,pad=10)

        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)

        self.lblempid.grid(row=0,column=0)
        self.txtempid.grid(row=0,column=1)

        self.lblename.grid(row=1,column=0)
        self.txtename.grid(row=1,column=1)


        self.lbldesig.grid(row=2,column=0)
        self.txtdesig.grid(row=2,column=1)

        self.lbluserid.grid(row=3,column=0)
        self.txtuserid.grid(row=3,column=1)

        self.lblpassword.grid(row=4,column=0)
        self.txtpassword.grid(row=4,column=1)

        self.lblutype.grid(row=5,column=0)
        self.txtutype.grid(row=5,column=1)

        self.btnsubmit.grid(columnspan=2)
        
        self.pack()
    def register(self):
        con=connect(db='mall',user='root',passwd='shivsql123',host='localhost')
        cur=con.cursor()
        eid=int(self.txtempid.get())
        ename=self.txtename.get()
        desig=self.txtdesig.get()
        uid=self.txtuserid.get()
        pwd=self.txtpassword.get()
        utype=self.txtutype.get()
        confirm=cur.execute("insert into employee values(%d,'%s','%s','%s','%s','%s')"%(eid,ename,desig,uid,pwd,utype))
        if(confirm==1):
            con.commit()
            msg.showinfo('Confirmation','Thanks for Register'+ename)
            self.txtempid.delete(0,'end')
            self.txtename.delete(0,'end')
            self.txtdesig.delete(0,'end')
            self.txtuserid.delete(0,'end')
            self.txtpassword.delete(0,'end')
            self.txtutype.delete(0,'end')
            self.txtempid.focus()
            con.close()

        