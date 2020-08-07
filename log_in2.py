from tkinter import *
from PIL import Image, ImageTk

from tkinter import messagebox


class LogIn:
    def __init__(self, root):
        self.root = root
        self.root.title("Log In Page")
        self.root.geometry("1350x700+0+0")

        # == variables
        self.uname=StringVar()
        self.upassword=StringVar()

        # ==Images
        self.bgimage = ImageTk.PhotoImage(file="green.jpg")
        self.user_icon = ImageTk.PhotoImage(file="batman icon.jpg")


        #  ==Labels
        title = Label(self.root, text="Sasatech", font=("Times New Roman", 40, "bold"), bg="white", fg="black", bd=10,relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)



        background = Label(self.root, image=self.bgimage).pack()

        # ==Frame(and its items)
        log_in_Frame = Frame(self.root)
        log_in_Frame.place(x=400, y=20)


        # ==Frame labels
        self.logo = Label(log_in_Frame, image=self.user_icon).grid(row=0, column=0, columnspan=2, pady=20)
        self.userlabel = Label(log_in_Frame, text="User Name:", compound=LEFT, font=("Times New Roman", 20, "bold"),bg="white").grid(row=1, column=0, padx=20, pady=10)
        self.userpass = Label(log_in_Frame, text="Password  :", compound=LEFT, font=("Times New Roman", 20, "bold"),bg="white").grid(row=2, column=0, padx=20, pady=10)
        self.copy = Label(log_in_Frame, text="Copyright Sasatech©2020").grid(row=3, column=1, padx=10,pady=10)

        # ==Frame entry fields
        self.user_text = Entry(log_in_Frame,textvariable=self.uname, bd=5, relief=GROOVE, font=("", 15)).grid(row=1, column=1, padx=20, pady=10)
        self.user_password = Entry(log_in_Frame,textvariable=self.upassword,show="*" ,bd=5, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20, pady=10)


        # ==Frame Buttons
        self.logIn_button = Button(log_in_Frame, text="Log In", font=("Times new roman", 15, "bold"), bg="orange",fg="white", padx=40, pady=15, command=self.login).grid(row=3, column=1, pady=10)

    def login(self):
        if self.uname.get().title()=="" or self.upassword.get()=="":
            messagebox.showinfo("Error!", "All fields are required!!")

        elif self.uname.get().title() == "Freddie" and self.upassword.get() == "Freddie":
            messagebox.showinfo("Success!", f"welcome {self.uname.get().title()}")

        else:
            messagebox.showinfo("Error!", "Invalid Username or Password!!")


logInPage = Tk()
login = LogIn(logInPage)
login

logInPage.mainloop()
