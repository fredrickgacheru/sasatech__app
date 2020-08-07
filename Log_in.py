from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import json
from tkinter import messagebox
import requests



def start():
    logInPage = Tk()
    login = LogIn(logInPage)
    login

    logInPage.mainloop()

class LogIn:
    def __init__(self, root):
        self.root = root
        self.root.title("Log In Page")
        screen_width=self.root.winfo_screenwidth()
        screen_heigh=self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (screen_width,screen_heigh))
        self.root.configure(background="white")

        # == variables
        self.user_email=StringVar()
        self.upassword=StringVar()




        # ==Images
        self.user_icon = ImageTk.PhotoImage(file="batman icon.jpg")

        #  ==Labels
        title = Label(self.root, text="Sasatech", font=("Times New Roman", 40, "bold"), bg="white", fg="black", bd=10,relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)


        # ==Frame (and its items)
        self.log_in_Frame = Frame(self.root, bg="white")
        self.log_in_Frame.place(x=400, y=100)

        # ==Frame labels
        self.logo = Label(self.log_in_Frame, image=self.user_icon).grid(row=0, column=0, columnspan=2, pady=20)
        self.userlabel = Label(self.log_in_Frame, text="E-mail:", compound=LEFT, font=("Times New Roman", 20, "bold"),bg="white").grid(row=1, column=0, padx=20, pady=10)
        self.userpass = Label(self.log_in_Frame, text="Password  :", compound=LEFT, font=("Times New Roman", 20, "bold"),bg="white").grid(row=2, column=0, padx=20, pady=10)


        # ==Frame entry fields
        self.user_text = Entry(self.log_in_Frame, textvariable=self.user_email, bd=5, relief=GROOVE, font=("", 15)).grid(row=1, column=1, padx=20, pady=10)
        self.user_password = Entry(self.log_in_Frame,textvariable=self.upassword,show="*" ,bd=5, relief=GROOVE, font=("", 15)).grid(row=2, column=1, padx=20, pady=10)


        # ==Frame Buttons
        self.logIn_button = Button(self.log_in_Frame, text="Log In", font=("Times new roman", 15, "bold"), bg="orange", fg="white", padx=40, pady=15, command=self.submit).grid(row=3, column=1, pady=10)




    def submit(self):

        try:
            user_data = {
                "user_email":self.user_email.get(),
                "user_password":self.upassword.get()
            }

            encoded_data = json.dumps(user_data)
            response = requests.post("http://192.168.201.2:8000/api/staff/login/", encoded_data)

            if response.ok:
                print("pass")

            else:
                messagebox.showwarning("Error!","Invalid User Name or Password")

        except:
            messagebox.showwarning("Server Error!"), "The application is not connected to the server. Please ensure the server is turned on."

if __name__=='__main__':
    start()







