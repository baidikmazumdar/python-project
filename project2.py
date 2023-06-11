from tkinter import*
from tkinter import messagebox
# from PIL import ImageTK
class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)
        


        #background image
     #    self.bg=PhotoImage(file="C:\Users\91813\Downloads")
     #    self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)



        #Login frame
        Frame_login=Frame(self.root,bg="lightgrey")
        Frame_login.place(x=330,y=150,width=500,height=400)
        #Title and subtitle
        title=Label(Frame_login,text="Login Here",font=("Impact",23,"bold"),fg="#6162FF",bg="white").place(x=90,y=30)
        subtitle=Label(Frame_login,text="Members Login Area",font=("Goundy old style",15,"bold"),fg="#1d1d1d",bg="white").place(x=90,y=100)
        #username
        lbl_user=Label(Frame_login,text="Username",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=140)
        self.username=Entry(Frame_login,font=("Goundy old style",15),bg="#E7E6E6")
        self.username.place(x=90,y=170,width=320,height=35)
        # password
        lbl_password=Label(Frame_login,text="Password",font=("Goudy old style",15,"bold"),fg="grey",bg="white").place(x=90,y=210)
        self.password=Entry(Frame_login,font=("Goundy old style",15),bg="#E7E6E6")
        self.password.place(x=90,y=240,width=320,height=35)
        #button
        forget=Button(Frame_login,text="Forget password?",bd=0,cursor="hand2",font=("Goudy old style",12,"bold"),fg="grey",bg="white").place(x=90,y=280)
        #login button
        submit=Button(Frame_login,command=self.check_function,cursor="hand2",text="Login",bd=0,font=("Goudy old style",15,"bold"),fg="black",bg="blue").place(x=90,y=320,width=180,height=40)
        
    def check_function(self):
        if self.username.get()==""or self.password.get=="":
             messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.username.get()!="tech2etc"or self.password.get()!="123456":
             messagebox.showerror("Error","Inavalid username or password",parent=self.root)
        else:
             messagebox.showinfo("Welcome",f"Welcome{self.username.get()}")

root=Tk()
obj=Login(root)
root.mainloop()