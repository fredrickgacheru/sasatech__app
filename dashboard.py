from tkinter import *
from time import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk
from tkinter.ttk import Treeview

class Dashboard:
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

        self.pie_chart =Frame(self.all_frame)
        self.pie_chart.configure(background="white")
        self.pie_chart.grid(row=0,column=2)

        self.time_frame = Frame(self.all_frame, height=50, width=50)
        self.time_frame.configure(background="white")
        self.time_frame.grid(row=0, column=3, padx=20,pady=20)

        self.stock_distribution= Frame(self.all_frame)
        self.stock_distribution.configure(background="white")
        self.stock_distribution.grid(row=0,column=4)


        # --Today Sales Frame--
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

        # --Pie chart Frame--
        self.fig = matplotlib.figure.Figure(figsize=(2, 2))
        self.ax = self.fig.add_subplot(111)
        self.ax.pie([30, 60, 30], labels=['cyber', 'beauty', 'well'], autopct='%0.1f%%', startangle=90)

        self.circle=matplotlib.patches.Circle( (0,0), 0.7, color='white')
        self.ax.add_artist(self.circle)

        self.canvas = FigureCanvasTkAgg(self.fig, self.pie_chart)
        self.canvas.get_tk_widget().pack()
        self.canvas.draw()

        #--Time Frame--
        #  time frame label
        self.now_label = Label(self.time_frame, text="NOW", font=("times new roman", 15), bg="white")
        self.now_label.pack()

        self.time_label = Label(self.time_frame, font=("times new roman", 15), bg="white")
        self.time_label.pack()

        # -- Stock distribution frame--
        # --Labels --
        self.stock_distribution_label=Label(self.stock_distribution, text="Stock Distribution",font=("arial",12),bg="white")
        self.stock_distribution_label.grid(row=0,column=0)

        self.USB_cables =Label(self.stock_distribution, text="USB cables", font=("arial",7),bg="white")
        self.USB_cables.grid(row=1,column=0)

        self.USB_cables_number = Label(self.stock_distribution, text="6", font=("arial", 7), bg="white")
        self.USB_cables_number.grid(row=1, column=1)

        self.wireless_mouse = Label(self.stock_distribution, text="wireless mouse", font=("arial", 7), bg="white")
        self.wireless_mouse.grid(row=2, column=0)

        self.wireless_mouse_number = Label(self.stock_distribution, text="6", font=("arial", 7), bg="white")
        self.wireless_mouse_number.grid(row=2, column=1)

    def display_time(self):
        self.current_time = strftime("%I:%M  %p")
        self.time_label['text'] = self.current_time
        self.root.after(1000, self.display_time)

root=Tk()
dash=Dashboard(root)
dash
dash.display_time()
root.mainloop()