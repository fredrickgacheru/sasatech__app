from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from time import *

class Bill_management:
    def __init__(self, root):
        self.root= root
        screen_width=self.root.winfo_screenwidth()
        screen_height=self.root.winfo_screenheight()
        self.root.geometry("%dx%d" %(screen_width,screen_height))
        self.root.title("Stock management")
        self.root.configure(background="white")


        # --Frame--
        self.all_frame = Frame(self.root)
        self.all_frame.configure(background="white")
        self.all_frame.pack(fill=BOTH)

        self.today_sales_frame = Frame(self.all_frame)
        self.today_sales_frame.configure(background="white")
        self.today_sales_frame.grid(row=0, column=0)

        self.bill_management_frame = Frame(self.all_frame)
        self.bill_management_frame.configure(background="white")
        self.bill_management_frame.grid(row=1, column=2)

        self.bill_items_table_frame= LabelFrame(self.all_frame,text="Products in stock")
        self.bill_items_table_frame.configure(background="white")
        self.bill_items_table_frame.grid(row=1,column=0)

        self.time_frame = Frame(self.all_frame,height=50,width=50)
        self.time_frame.configure(background="white")
        self.time_frame.grid(row=0,column=2)

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

        #--Bill items table frame
        # --Table--
        self.table=Treeview(self.bill_items_table_frame, columns=(1,2,3,4,5), show="headings")
        self.table.grid(row=0,column=0)

        self.table.heading(1, text="No", anchor=W)
        self.table.heading(2, text="Date", anchor=W)
        self.table.heading(3, text="Type", anchor=W)
        self.table.heading(4, text="Description", anchor=W)
        self.table.heading(5, text="Amount", anchor=W)

        self.table.column(1, width=100, minwidth=50)
        self.table.column(2, width=200, minwidth=100)
        self.table.column(3, width=200, minwidth=100)
        self.table.column(4, width=200, minwidth=100)
        self.table.column(5, width=200, minwidth=100)

        # -- bill management frame contents--
        # --labels--
        self.add_product_label=Label(self.bill_management_frame, text="Add Product", font=("calibri",16),bg="white")
        self.add_product_label.grid(row=0,column=0, sticky=W)

        self.product_type_label = Label(self.bill_management_frame, text="Product Type:", bg="white")
        self.product_type_label.grid(row=1,column=0,sticky=W,pady=10)

        self.product_name_label = Label(self.bill_management_frame, text="Product Name:", bg="white")
        self.product_name_label.grid(row=2, column=0,sticky=W,pady=10)

        self.price_label = Label(self.bill_management_frame, text="Price:", bg="white")
        self.price_label.grid(row=4,column=0,sticky=W,pady=10)

        self.quantity_label = Label(self.bill_management_frame, text = "Quatity:", bg="white")
        self.quantity_label.grid(row=6,column=0,sticky=W,pady=10)

        self.remarks_label = Label(self.bill_management_frame, text = "Remarks", bg="white")
        self.remarks_label.grid(row=8,column=0,sticky=W,pady=10)

        # --combobox--
        self.product_service_combobox = ttk.Combobox(self.bill_management_frame, width=20, height=10)
        items = ("Product/Service", "Cyber Services", "Repair", "Movies/Series", "Electronics")
        self.product_service_combobox["values"] = items
        self.product_service_combobox.current(0)
        self.product_service_combobox.grid(row=1, column=1, columnspan=2,sticky=W)


        # -- Entry Fields--
        self.product_name_entry = Text(self.bill_management_frame, width=30, height=1, padx=20,pady=10)
        self.product_name_entry.insert(0.0, "Product Name")
        self.product_name_entry.bind("<Button-1>", self.product_name_entry_clear)
        self.product_name_entry.grid(row=3,column=0,columnspan=2,sticky=W)

        self.price_entry = Text(self.bill_management_frame,width=10,height=1,padx=20,pady=10)
        self.price_entry.insert(0.0, "Price")
        self.price_entry.bind("<Button-1>", self.price_entry_clear)
        self.price_entry.grid(row=5,column=0,sticky=W)

        self.quantity_entry = Text(self.bill_management_frame, width=10, height=1, padx=20, pady=10)
        self.quantity_entry.insert(0.0, "Quantity")
        self.quantity_entry.bind("<Button-1>", self.quantity_entry_clear)
        self.quantity_entry.grid(row=7, column=0,sticky=W)

        self.remarks_entry = Text(self.bill_management_frame, width=30, height=3, padx=20, pady=10)
        self.remarks_entry.insert(0.0, "Remarks")
        self.remarks_entry.bind("<Button-1>", self.remarks_entry_clear)
        self.remarks_entry.grid(row=9, column=0,columnspan=2,sticky=W)


        # --Button--
        self.add_product_button = ttk.Button(self.bill_management_frame, text="Add Product",command=self.submit)
        self.add_product_button.configure(padding=10)
        self.add_product_button.grid(row=10,column=0, padx=20,pady=20)



        #---time frame--
        #--label--
        self.time_now= Label(self.time_frame, text="Time Now:", font=("calibri",12),bg="white")
        self.time_now.pack()

        self.time_show = Label(self.time_frame, font=("calibri", 14),bg="white")
        self.time_show.pack()

    def product_name_entry_clear(self, event):
        self.product_name_entry.delete(0.0, END)

    def price_entry_clear(self, event):
        self.price_entry.delete(0.0, END)

    def quantity_entry_clear(self, event):
        self.quantity_entry.delete(0.0, END)

    def remarks_entry_clear(self, event):
        self.remarks_entry.delete(0.0, END)
        if self.product_name_entry.get(0.0,END) == "":
            self.product_name_entry.insert(0.0,"Product Name")

    def submit(self):
        print(self.product_name_entry.get(0.0,END))

    def show_time(self):
        current_time=strftime("%I:%M %p")
        self.time_show['text']=current_time
        self.root.after(1000,self.show_time)

root = Tk()
master=Bill_management(root)
master
master.show_time()
root.mainloop()