from tkinter import *
from tkinter import ttk
from tkinter.ttk import Treeview
from time import *
import sqlite3

connection = sqlite3.connect('sasatechDB.db')
cursor = connection.cursor()

cursor.execute('SELECT * FROM transactions')
result = cursor.fetchall()


class Transactions:
    def __init__(self, root):
        self.root = root
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry("%dx%d+0+0" % (screen_width, screen_height))
        self.root.configure(background="white")
        self.root.title("Transaction")

        # --Frames--
        self.all_frame = Frame(self.root)
        self.all_frame.configure(background="white")
        self.all_frame.pack()

        self.today_sales_frame = Frame(self.all_frame)
        self.today_sales_frame.configure(background="white")
        self.today_sales_frame.grid(row=0, column=1)

        self.time_frame = Frame(self.all_frame, height=50, width=50)
        self.time_frame.configure(background="white")
        self.time_frame.grid(row=0, column=3, padx=20,pady=20)

        self.transaction_recorder = Frame(self.all_frame, height=400, width=100)
        self.transaction_recorder.configure(background="white")
        self.transaction_recorder.grid(row=1, column=3)

        self.transaction_table = Frame(self.all_frame, height=40, width=100)
        self.transaction_table.grid(row=1, column=1)

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
        # --transaction recorder items--
        # --labels--
        self.record_label = Label(self.transaction_recorder, text='Record A Sale', font=("Times new roman", 14),
                                  bg="white")
        self.record_label.grid(row=0, column=1)

        # --combobox--
        self.product_service_combobox = ttk.Combobox(self.transaction_recorder, width=20, height=10)
        items = ("Product/Service", "Cyber Services", "Repair", "Movies/Series", "Electronics")
        self.product_service_combobox["values"] = items
        self.product_service_combobox.current(0)
        self.product_service_combobox.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

        # --text boxes--
        self.description_entry_box = Text(self.transaction_recorder, height=1, width=30, padx=20, pady=10)
        self.description_entry_box.insert(0.0, "Description")
        self.description_entry_box.bind('<Button-1>', self.clear_description_box)
        self.description_entry_box.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

        self.amount_entry = Text(self.transaction_recorder, height=1, width=30, padx=20, pady=10)
        self.amount_entry.insert(0.0, "Amount")
        self.amount_entry.bind('<Button-1>', self.clear_amount_entry)
        self.amount_entry.grid(row=3, column=0, padx=10, pady=10, columnspan=3)

        # --labels--
        self.payment_label = Label(self.transaction_recorder, text="Payment Method", fg="grey",
                                   font=("times new roman", 9), bg="white")
        self.payment_label.grid(row=4, column=0, sticky=W)

        # --RadioButton --
        self.paymode = StringVar()
        self.paymode.set("cash")
        self.cash_radio_button = Radiobutton(self.transaction_recorder, text="Cash", variable=self.paymode,
                                             value="cash", bg="white")
        self.cash_radio_button.grid(row=5, column=0, sticky=W)

        self.mpesa_radio_button = Radiobutton(self.transaction_recorder, text="M-Pesa", variable=self.paymode,
                                              value="mpesa", bg="white")
        self.mpesa_radio_button.grid(row=6, column=0, sticky=W)

        # --Button
        self.complete_sale_button = ttk.Button(self.transaction_recorder, text="Submit Sale", command=self.submit)
        self.complete_sale_button.configure(padding=10)
        self.complete_sale_button.grid(row=5, column=1, rowspan=2)

        # --transaction table contents--
        # --table--

        self.transaction_record_table = Treeview(self.transaction_table, columns=(1, 2, 3, 4, 5, 6), show="headings",
                                                 height="10")
        self.transaction_record_table.pack(side=LEFT)

        self.transaction_record_table.heading(1, text="#", anchor=W)
        self.transaction_record_table.heading(2, text="Date/Time", anchor=W)
        self.transaction_record_table.heading(3, text="Service/Product", anchor=W)
        self.transaction_record_table.heading(4, text="Description", anchor=W)
        self.transaction_record_table.heading(5, text="Amount", anchor=W)
        self.transaction_record_table.heading(6, text="Payment Method", anchor=W)

        self.transaction_record_table.column(1, width=60)
        self.transaction_record_table.column(2, width=150)
        self.transaction_record_table.column(3, width=150)
        self.transaction_record_table.column(4, width=130)
        self.transaction_record_table.column(5, width=130)
        self.transaction_record_table.column(6, width=130)

        # scroll bar
        self.yscrollbar = ttk.Scrollbar(self.transaction_table, orient="vertical", command=self.transaction_record_table.yview)
        self.yscrollbar.pack(side=RIGHT, fill="y")

        self.transaction_record_table.configure(yscrollcommand=self.yscrollbar.set)

        #  time frame label
        self.now_label= Label(self.time_frame,text="NOW", font=("times new roman", 15),bg="white")
        self.now_label.pack()

        self.time_label=Label(self.time_frame,font=("times new roman", 15),bg="white")
        self.time_label.pack()

    def clear_description_box(self, event):
        self.description_entry_box.delete(0.0, END)

    def clear_amount_entry(self, event):
        self.amount_entry.delete(0.0, END)

    def submit(self):
        self.description = self.description_entry_box.get(0.0, END)
        self.amount = self.amount_entry.get(0.0, END)
        self.payment_type = self.paymode.get()
        print(self.amount + self.description + self.payment_type)

    def update_table(self, result):
        for row in result:
            self.transaction_record_table.insert("", END, value=(row))

    def display_time(self):
        self.current_time = strftime("%I:%M  %p")
        self.time_label['text'] = self.current_time
        self.root.after(1000, self.display_time)


root = Tk()
screen = Transactions(root)
screen
screen.update_table(result)
screen.display_time()
if __name__ == '__main__':
    root.mainloop()
