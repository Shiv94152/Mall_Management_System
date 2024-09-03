from tkinter import *
from pymysql import *
from tkinter import messagebox as msg

class ModifyUser(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.lbleid=Label(self,text='Employee Id',bg='lightblue',font=('sans-serif',16))
        self.lbldesig=Label(self,text='New Designation',bg='lightblue',font=('sans-serif',16))
        self.lbluserid=Label(self,text='New User Id',bg='lightblue',font=('sans-serif',16))
        self.lblpasswd=Label(self,text='New Password',bg='lightblue',font=('sans-serif',16))
        self.lblusertype=Label(self,text='User Type',bg='lightblue',font=('sans-serif',16))


        self.txteid=Entry(self,bg='lightblue',font=('sans-serif',16),bd=6,justify='center')
        self.txtdesig=Entry(self,bg='lightblue',font=('sans-serif',16),bd=6,justify='center')
        self.txtuserid=Entry(self,bg='lightblue',font=('sans-serif',16),bd=6,justify='center')
        self.txtpasswd=Entry(self,show='*',bg='lightblue',font=('sans-serif',16),bd=6,justify='center')
        self.txtusertype=Entry(self,bg='lightblue',font=('sans-serif',16),bd=6,justify='center')


        self.b1=Button(self,text='Update User',bg='lightblue',font=('sans-serif',16),bd=6,justify='center',command=self.updateuser)

        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)
        self.rowconfigure(index=3,pad=10)
        self.rowconfigure(index=4,pad=10)
        self.rowconfigure(index=5,pad=10)


        self.columnconfigure(index=0,pad=15)
        self.columnconfigure(index=1,pad=15)

        self.lbleid.grid(row=0,column=0)
        self.txteid.grid(row=0,column=1)

        self.lbldesig.grid(row=1,column=0)
        self.txtdesig.grid(row=1,column=1)

        self.lbluserid.grid(row=2,column=0)
        self.txtuserid.grid(row=2,column=1)

        self.lblpasswd.grid(row=3,column=0)
        self.txtpasswd.grid(row=3,column=1)

        self.lblusertype.grid(row=4,column=0)
        self.txtusertype.grid(row=4,column=1)

        self.b1.grid(columnspan=2)

        self.pack()
    
    def updateuser(self):
    
        con=connect(db='mall',user='root',passwd='shivsql123',host='localhost')
        cur=con.cursor()
        eid=int(self.txteid.get())
        desig=self.txtdesig.get()
        userid=self.txtuserid.get()
        passwd=self.txtpasswd.get()
        usertype=self.txtusertype.get()

        try:
            i=cur.execute("Update employee set desig='%s',userid='%s',passwd='%s',usertype='%s' where eid=%d"%(desig,userid,passwd,usertype,eid))
            if(i==1):
                con.commit()
                msg.showinfo('Confirmation','User Modified')
                con.close()
                self.txteid.delete(0,'end')
                self.txtdesig.delete(0,'end')
                self.txtuserid.delete(0,'end')
                self.txtpasswd.delete(0,'end')
                self.txtusertype.delete(0,'end')
                self.txteid.focus()
        except MySQLError as me:
            msg.showerror('Error','Oops! Something went wrong. '+me)
            con.close()
        