from tkinter import *
from pymysql import *
from tkinter import messagebox as msg
from NewUser import *
from AdminPanel import *
from UserPanel import *
class UserLogin(Frame):
    def __init__(self,master):
        super().__init__(master)

        self.lbluserid=Label(self,text="User Name",fg="darkgray",bg="lightblue",font=("sans-serif",16))
        self.lblpassword=Label(self,text="Password",fg="darkgray",bg="lightblue",font=("sans-serif",16))

        self.txtuserid=Entry(self,fg="darkgray",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")
        self.txtpassword=Entry(self,show='*',fg="darkgray",bg="lightblue",font=("sans-serif",16),bd=6,justify="center")

        self.btnsubmit=Button(self,text='Login',bg="lightblue",font=("sans-serif",16),bd=6,justify="center",command=self.check)
        self.btnnewuser=Button(self,text='New User',bg="lightblue",font=("sans-serif",16),bd=6,justify="center",command=self.newuser)

        self.rowconfigure(index=0,pad=10)
        self.rowconfigure(index=1,pad=10)
        self.rowconfigure(index=2,pad=10)

        self.columnconfigure(index=0,pad=10)
        self.columnconfigure(index=1,pad=10)

        self.lbluserid.grid(row=0,column=0)
        self.txtuserid.grid(row=0,column=1)

        self.lblpassword.grid(row=1,column=0)
        self.txtpassword.grid(row=1,column=1)

        self.btnsubmit.grid(row=2,column=0)
        self.btnnewuser.grid(row=2,column=1)
        self.pack()
    def newuser(self):
        root1=Tk()
        ob=Registration(root1)
        root1.geometry('480x450')
        root1.title('Login Box')
        root1.mainloop()
    def check(self):
        uid=self.txtuserid.get()
        pwd=self.txtpassword.get()
        con=connect(db='mall',user='root',passwd='shivsql123',host='localhost')
        cur=con.cursor()
        cur.execute("select * from employee where userid='%s' and passwd='%s'"%(uid,pwd))
        result=cur.fetchall()
        if(len(result)==0):
            msg.showerror('Errro Information','Sorry either username or password is wrong!!!')
            self.txtuserid.delete(0,'end')
            self.txtpassword.delete(0,'end')
            self.txtuserid.focus()
        else:
            type=result[0][5]
            if(type=='admin'):
                root=Tk()
                ob=MyMenu(root)
                root.state('zoomed')
                root.config(menu=ob.menubar)
                root.mainloop()
            else:
                root=Tk()
                ob=UserMenu(root)
                root.state('zoomed')
                root.config(menu=ob.menubar)
                root.mainloop()



root=Tk()
ob=UserLogin(root)
root.geometry('480x250')
root.title('Login Box')
root.mainloop()

        