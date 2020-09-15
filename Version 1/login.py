from tkinter import *
import tkinter.messagebox as tm
import students

class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.label_username=Label(self,text="Username")
        self.label_password=Label(self,text="Password")

        self.entry_username=Entry(self)
        self.entry_password=Entry(self,show="*")

        self.label_username.grid(row=0,sticky=E)
        self.label_password.grid(row=1,sticky=E)
        self.entry_username.grid(row=0,column=1)
        self.entry_password.grid(row=1,column=1)

        self.logbtn=Button(self,text="Login",command=self._login_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _login_btn_clicked(self):
        global username
        username=self.entry_username.get()
        password=self.entry_password.get()
        index=0

        for i in range(0,len(students.usernames)):
            if username==students.usernames[i]:
                index=i
            
        if password==students.passwords[index]:
            tm.showinfo("Login Success", "Welcome")
        else:
            tm.showerror("Login Error", "Incorrect Login Credentials")
