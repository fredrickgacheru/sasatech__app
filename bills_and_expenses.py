from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from time import *


class Expense_management:
    def __init__(self, root):
        self.root = root
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d" % (screen_width, screen_height))
        self.root.title("Bills and Expenses")
        self.root.configure(background="white")

        # -- Frames
        self.all_frame = Frame(self.root)
        self.all_frame.configure(background="white")
        self.all_frame.pack(fill=BOTH)

        self.today_sales_frame = Frame(self.all_frame)
        self.today_sales_frame.configure(background="white")
        self.today_sales_frame.grid(row=0, column=1)

        self.chart_frame = Frame(self.all_frame)
        self.chart_frame.configure(background="white")
        self.chart_frame.grid(row=0, column=2)

        self.time_frame = Frame(self.all_frame)
        self.time_frame.configure(background="white")
        self.time_frame.grid(row=0, column=2)

        self.table_frame = LabelFrame(self.all_frame, text="Billed Items")
        self.table_frame.configure(background="white")
        self.table_frame.grid(row=1, column=1)

        self.bill_management_frame = Frame(self.all_frame)
        self.bill_management_frame.configure(background="white")
        self.bill_management_frame.grid(row=1, column=2)

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
        # --time frame
        self.now_label = Label(self.time_frame, text="NOW", font=("times new roman", 15), bg="white")
        self.now_label.pack()

        self.time_label = Label(self.time_frame, font=("times new roman", 15), bg="white")
        self.time_label.pack()

        # --table frame
        self.bill_record_table = Treeview(self.table_frame, columns=(1, 2, 3, 4, 5), show="headings",
                                          height="9")
        self.bill_record_table.grid(row=0, column=0)

        self.bill_record_table.heading(1, text="No", anchor=W)
        self.bill_record_table.heading(2, text="Date", anchor=W)
        self.bill_record_table.heading(3, text="Bill Name", anchor=W)
        self.bill_record_table.heading(4, text="Description", anchor=W)
        self.bill_record_table.heading(5, text="Amount", anchor=W)

        self.bill_record_table.column(1, width=100)
        self.bill_record_table.column(2, width=200)
        self.bill_record_table.column(3, width=200)
        self.bill_record_table.column(4, width=200)
        self.bill_record_table.column(5, width=200)

        # --bill management frame
        # --bill management frame--
        # --label
        self.bill_management_label = Label(self.bill_management_frame, text="Bill Entry Form", bg='white')
        self.bill_management_label.grid(row=0, column=0, sticky=W, padx=10, pady=10)

        self.bill_name = Label(self.bill_management_frame, text="Bill Name:",bg="white")
        self.bill_name.grid(row=1, column=0, sticky=W)

        self.bill_description = Label(self.bill_management_frame, text="Bill Name:", bg="white")
        self.bill_description.grid(row=3, column=0, sticky=W)

        self.bill_amount = Label(self.bill_management_frame, text="Amount:", bg="white")
        self.bill_amount.grid(row=5, column=0, sticky=W)


        # --text_boxes
        self.Bill_Name = Text(self.bill_management_frame, height=1, width=30, padx=10, pady=10)
        self.Bill_Name.insert(0.0, "Bill Name")
        self.Bill_Name.bind('<Button-1>', self.on_entry_click)
        self.Bill_Name.grid(row=2, column=0, sticky=W, padx=5, pady=5)

        self.bill_description = Text(self.bill_management_frame, height=1, width=30, padx=10, pady=10)
        self.bill_description.insert(0.0, "Bill Description")
        self.bill_description.bind('<Button-1>', self.bill_description_txt_delete)
        self.bill_description.grid(row=4, column=0, sticky=W, padx=10, pady=10)

        self.bill_amount_text = Text(self.bill_management_frame, height=1, width=30, padx=10, pady=10)
        self.bill_amount_text.insert(0.0, "Amount")
        self.bill_amount_text.bind('<Button-1>', self.bill_amount_txt_delete)
        self.bill_amount_text.grid(row=6, column=0, sticky=W, padx=10, pady=10)


        # -- buttons
        style = ttk.Style()
        style.configure("TButton", padding=10)
        self.add_employee = ttk.Button(self.bill_management_frame, text="Submit")
        self.add_employee.grid(row=7, column=0, sticky=W, padx=10, pady=10)

    def on_entry_click(self, event):
        self.Bill_Name.delete(0.0, END)

    def bill_amount_txt_delete(self, event):
        self.bill_amount_text.delete(0.0, END)

    def bill_description_txt_delete(self, event):
        self.bill_description.delete(0.0, END)

    def display_time(self):
        self.current_time = strftime("%I:%M  %p")
        self.time_label['text'] = self.current_time
        self.root.after(1000, self.display_time)


root = Tk()
master = Expense_management(root)
master
master.display_time()
root.mainloop()
