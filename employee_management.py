from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from time import *
import sqlite3

connection=sqlite3.connect("sasatechDB.db")
cursor=connection.cursor()
cursor.execute("SELECT * from employee_information")
result=cursor.fetchall()



class Bill:
    def __init__(self,root):
        self.root=root
        width_value=self.root.winfo_screenwidth()
        height_value=self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" %(width_value,height_value))
        self.root.configure(background="white")

        # --Frames--
        self.all_frame = Frame(self.root)
        self.all_frame.configure(background="white")
        self.all_frame.pack(fill=BOTH)

        self.time_frame=Frame(self.all_frame)
        self.time_frame.configure(background="white")
        self.time_frame.grid(row=0,column=3, padx=20, pady=20)

        self.today_sales_frame = Frame(self.all_frame)
        self.today_sales_frame.configure(background="white")
        self.today_sales_frame.grid(row=0, column=1, padx=20, pady=20)

        self.tableLabelFrame= LabelFrame(self.all_frame, text="Employee Information")
        self.tableLabelFrame.configure(background="white")
        self.tableLabelFrame.grid(row=1, column=1)

        self.search_section = Frame(self.all_frame)
        self.search_section.configure(background="white")
        self.search_section.grid(row=2,column=1, sticky=W, padx=20, pady=20)

        self.bill_management_frame= Frame(self.all_frame, height=200, width=100)
        self.bill_management_frame.configure(background="white")
        self.bill_management_frame.grid(row=1,column=3, padx=20, pady=20)

        # --today sales frame
        # --labels
        self.total_label = Label(self.today_sales_frame, text="Today", font=("New Times Roman", 15), fg='Orange',
                                 bg="white")
        self.total_label.grid(row=0, column=0, sticky=W)

        self.sales_today_label = Label(self.today_sales_frame, text="Sales today", font=("New Times Roman", 15),
                                       fg='Orange', bg="white")
        self.sales_today_label.grid(row=1, column=0, sticky=W)

        self.no_sales = Label(self.today_sales_frame, text="No of Sales", font=("New Times Roman", 6), bg="white")
        self.no_sales.grid(row=0, column=1, padx=40)

        self.sales = Label(self.today_sales_frame, text=15, font=("New Times Roman", 13), bg="white")
        self.sales.grid(row=1, column=1, padx=40)

        self.amount_label = Label(self.today_sales_frame, text="Amount", font=("New Times Roman", 6), bg="white")
        self.amount_label.grid(row=0, column=2, padx=40)

        self.amount_no_label = Label(self.today_sales_frame, text=1500, font=("New Times Roman", 13), bg="white")
        self.amount_no_label.grid(row=1, column=2, padx=40)

        self.top_product_label = Label(self.today_sales_frame, text="Top Product", font=("New Times Roman", 6),
                                       bg="white")
        self.top_product_label.grid(row=0, column=3, padx=40)

        self.item_label = Label(self.today_sales_frame, text="Cyber Services", font=("New Times Roman", 13), bg="white")
        self.item_label.grid(row=1, column=3, padx=40)

        #--bill management frame--
        #--label
        self.bill_management_label= Label(self.bill_management_frame, text="Add Employee",bg='white')
        self.bill_management_label.grid(row=0,column=0,sticky=W,padx=10,pady=10)

        # --labels--
        self.employee_first_name_label = Label(self.bill_management_frame, text ="First Name:" ,bg="white")
        self.employee_first_name_label.grid(row=1, column=0, sticky=W,padx=20,pady=10)

        self.employee_second_name_label = Label(self.bill_management_frame, text="Last Name:", bg="white")
        self.employee_second_name_label.grid(row=1, column=1, sticky=W, pady=10,padx=20)

        self.id_number_label = Label(self.bill_management_frame, text="ID Number:", bg="white")
        self.id_number_label.grid(row=3, column=0, sticky=W,padx=20,pady=10)

        self.email_label = Label(self.bill_management_frame, text="Employee Email:", bg="white")
        self.email_label.grid(row=3,column=1, sticky=W,padx=20,pady=10)

        self.employee_number = Label(self.bill_management_frame, text="Employee Phone Number:", bg="white")
        self.employee_number.grid(row=5,column=0,sticky=W,padx=20,pady=10)

        self.employee_role_label = Label(self.bill_management_frame, text="Employee Role", bg="white")
        self.employee_role_label.grid(row=5,column=1, sticky=W,padx=20,pady=10)

        self.job_description_label = Label(self.bill_management_frame, text="Job Description", bg="white")
        self.job_description_label.grid(row=7,column=0,sticky=W,padx=20,pady=10)

        #--text_boxes
        self.employee_first_name = Text(self.bill_management_frame, height=1, width=30, padx=10, pady=10)
        self.employee_first_name.insert(0.0, "First Name")
        self.employee_first_name.bind('<Button-1>', self.on_entry_click)
        self.employee_first_name.grid(row=2, column=0,sticky=W,padx=20)

        self.employee_second_name = Text(self.bill_management_frame, height=1, width=30, padx=10, pady=10)
        self.employee_second_name.insert(0.0, "Last Name")
        self.employee_second_name.bind('<Button-1>', self.second_name_delete)
        self.employee_second_name.grid(row=2, column=1, sticky=W,padx=20)

        self.id_number = Text(self.bill_management_frame, height=1,width=30,padx=10,pady=10)
        self.id_number.insert(0.0, "ID Number")
        self.id_number.bind('<Button-1>', self.id_number_txt_delete)
        self.id_number.grid(row=4, column=0, sticky=W,padx=20)

        self.employee_email = Text(self.bill_management_frame, height=1, width=30, padx=10, pady=10)
        self.employee_email.insert(0.0, "Enter Email")
        self.employee_email.bind('<Button-1>', self.employee_mail_txt_delete)
        self.employee_email.grid(row=4,column=1, sticky=W,padx=20)

        self.employee_phone_number_text = Text(self.bill_management_frame, height=1, width=30, padx=10, pady=10)
        self.employee_phone_number_text.insert(0.0, "Enter Phone Number")
        self.employee_phone_number_text.bind('<Button-1>', self.employee_mail_txt_delete)
        self.employee_phone_number_text.grid(row=6, column=0,sticky=W,padx=20)

        self.job_description = Text(self.bill_management_frame, height=3, width=30, padx=10,pady=10)
        self.job_description.insert(0.0, "Job Description")
        self.job_description.bind('<Button-1>', self.job_description_txt_delete)
        self.job_description.grid(row=8,column=0, sticky=W,padx=20)


        # add employee_email and phone number


        #--combobox
        self.employee_role = ttk.Combobox(self.bill_management_frame)
        self.items = ("--Select One--","Sales Manager", "Repair", "Chief engineer", "Investor","Other")
        self.employee_role["values"]=self.items
        self.employee_role.current(0)
        self.employee_role.grid(row=6,column=1,sticky=W)


        # --buttons
        style=ttk.Style()
        style.configure("TButton",padding=10)
        self.add_employee=ttk.Button(self.bill_management_frame, text= "Add employee", command=self.add_employee)
        self.add_employee.grid(row=12,column=0,sticky=W,padx=10,pady=10)


        #--table frame
        #--table
        self.tableStyle=ttk.Style

        self.table=Treeview(self.tableLabelFrame, columns=(1,2,3,4), show='headings', height='7')
        self.table.grid(row=0,column=0)

        self.table.heading(1, text="Employee ID")
        self.table.heading(2, text="First Name")
        self.table.heading(3, text="Last Name")
        self.table.heading(4, text="Description")

        self.table.column(1, width=100, minwidth=50)
        self.table.column(2, width=200, minwidth=100)
        self.table.column(3, width=200, minwidth=100)
        self.table.column(4, width=200, minwidth=100)

        # -- Search label frame
        self.search_label=Label(self.search_section, text="Search:", bg="white", padx=10,pady=10)
        self.search_label.grid(row=0,column=0, sticky=W)

        self.search_entry = Text(self.search_section, height=1,width=45,padx=10,pady=5)
        self.search_entry.grid(row=0,column=1, sticky=W)

        self.search_button= ttk.Button(self.search_section, text="Search")
        self.search_button.configure(padding=10)
        self.search_button.grid(row=1,column=1)


        #--time frame
        self.time_now=Label(self.time_frame, text="Time Now:", font=("calibri",14), bg="white")
        self.time_now.pack()

        self.display_time=Label(self.time_frame,font=14,bg="white")
        self.display_time.pack()

    def on_entry_click(self,event):
        self.employee_first_name.delete(0.0, END)

    def second_name_delete(self,event):
        self.employee_second_name.delete(0.0, END)

    def id_number_txt_delete(self,event):
        self.id_number.delete(0.0,END)


    def job_description_txt_delete(self,event):
        self.job_description.delete(0.0,END)

    def add_employee(self):
        print(str(self.employee_first_name.get(0.0, END)) + str(self.id_number.get(0.0, END)) + str(self.job_description.get(0.0, END)))

    def employee_mail_txt_delete(self,event):
        self.employee_email.delete(0.0,END)

    def employee_number_txt_delete(self,event):
        self.employee_phone_number_text.delete(0.0,END)

    def update_table(self,result):
        for row in result:
            self.table.insert("",END,value=row)

    def show_time(self):
        current_time= strftime("%I:%M %p")
        self.display_time['text']=current_time
        self.root.after(1000, self.show_time)

    def search(self):
        self.unique_code=self.search_entry.get()



root=Tk()
bill=Bill(root)
bill
bill.update_table(result)
bill.show_time()

if __name__ == "__main__":
    root.mainloop()