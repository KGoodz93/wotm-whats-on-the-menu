# Modules

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import sqlite3
import win32com.client as win32
import os.path
import time
from configparser import ConfigParser

# Variables

config = ConfigParser()
config.read(r'config.ini')
user = os.getlogin()

verno = config.get('App', 'version')
mailbox = config.get('Contacts', 'mailbox')

path = fr"C:/Users/{user}/Dropbox/Dev/Python/Projects/WOTM Meal Planner/"
db = r"\\192.168.1.97\shared-snowmoon\database\wotm_goodikel.db"
today = datetime.today().strftime("%Y%m%d")
count = 0
modTimesinceEpoc = os.path.getmtime(db)
modificationTime = time.strftime('%d/%m/%Y %H:%M', time.localtime(modTimesinceEpoc))
linebreak = "\n"

# Database Connection

connection = sqlite3.connect(db)
cursor = connection.cursor()

# External UI (User Interface)

ui_view_meals = os.path.join(path, r'UI/button_view_meals.png')
ui_view_items = os.path.join(path, r'UI/button_view_items.png')
ui_generate_shopping = os.path.join(path, r'UI/button_generate.png')
ui_exit = os.path.join(path, r'UI/button_exit.png')
ui_back = os.path.join(path, r'UI/button_back.png')
ui_add = os.path.join(path, r'UI/button_add.png')
ui_remove = os.path.join(path, r'UI/button_remove.png')
ui_add_meal = os.path.join(path, r'UI/button_add_meal.png')
ui_update_meal = os.path.join(path, r'UI/button_update_meal.png')
ui_home = os.path.join(path, r'UI/button_home.png')
ui_add_item = os.path.join(path, r'UI/button_add_item.png')
ui_remove_item = os.path.join(path, r'UI/button_remove_item.png')
ui_refresh = os.path.join(path, r'UI/button_refresh.png')
ui_increase_quantity = os.path.join(path, r'UI/button_quant_increase.png')
ui_decrease_quantity = os.path.join(path, r'UI/button_quant_decrease.png')
ui_confirm = os.path.join(path, r'UI/button_confirm.png')
ui_update = os.path.join(path, r'UI/button_update.png')
ui_delete = os.path.join(path, r'UI/button_delete.png')
ui_add2 = os.path.join(path, r'UI/button_add2.png')
ui_search = os.path.join(path, r'UI/button_search.png')

# Script

root1 = Tk()


def window_main():
    # Tkinter Config

    root1.geometry("300x425+100+100")
    root1.title(f"WOTM Meal Planner - Home")
    root1.configure(bg="#B8D8D8")
    root1.resizable(False, False)

    # External UI

    mainmenu_btn1 = PhotoImage(file=ui_view_meals)
    mainmenu_btn2 = PhotoImage(file=ui_view_items)
    mainmenu_btn3 = PhotoImage(file=ui_generate_shopping)
    mainmenu_btn4 = PhotoImage(file=ui_exit)

    # Actions

    def mainmenu_viewmenu():
        root1.withdraw()
        window_viewmeals()

    def mainmenu_viewitems():
        root1.withdraw()
        window_viewitems()

    def mainmenu_generateshopping():
        root1.withdraw()
        window_generateshopping()

    # Widgets

    btn1 = Button(command=mainmenu_viewmenu, image=mainmenu_btn1, borderwidth=0, highlightthickness=0,
                  activebackground='#B8D8D8', bg="#B8D8D8", bd=0, )
    btn1.grid(column=0, row=1, padx=80, pady=20)

    sep1 = ttk.Separator()
    sep1.place(x=118, y=82, relwidth=0.2)

    btn2 = Button(command=mainmenu_viewitems, image=mainmenu_btn2, borderwidth=0, highlightthickness=0,
                  activebackground='#B8D8D8', bg="#B8D8D8", bd=0, )
    btn2.grid(column=0, row=2, padx=80, pady=20)

    sep2 = ttk.Separator()
    sep2.place(x=118, y=164, relwidth=0.2)

    btn3 = Button(command=mainmenu_generateshopping, image=mainmenu_btn3, borderwidth=0, highlightthickness=0,
                  activebackground='#B8D8D8', bg="#B8D8D8", bd=0, )
    btn3.grid(column=0, row=4, padx=80, pady=20)

    sep3 = ttk.Separator()
    sep3.place(x=118, y=246, relwidth=0.2)

    btn4 = Button(command=root1.destroy, image=mainmenu_btn4, borderwidth=0, highlightthickness=0,
                  activebackground='#B8D8D8', bg="#B8D8D8", bd=0, )
    btn4.grid(column=0, row=5, padx=80, pady=20)

    sep4 = ttk.Separator()
    sep4.place(x=118, y=328, relwidth=0.2)

    label2 = Label(text=f"Last Price Update: {modificationTime}"
                        f"\nCreated by Kelv Gooding"
                        f"\nVersion {verno}", bg="#B8D8D8")
    label2.grid(column=0, row=7, pady=15)

    root1.mainloop()


def window_viewmeals():
    # Tkinter Config

    root2 = Tk()
    root2.geometry("580x420+100+100")
    root2.title("WOTM Meal Planner - View Meals")
    root2.configure(bg="#B8D8D8")
    root2.resizable(False, False)

    # External UI

    viewmenu_btnimg1 = PhotoImage(file=ui_add, master=root2)
    viewmenu_btnimg2 = PhotoImage(file=ui_remove, master=root2)
    viewmenu_btnimg3 = PhotoImage(file=ui_update, master=root2)
    viewmenu_btnimg4 = PhotoImage(file=ui_home, master=root2)

    # Action

    def window_addmeal():
        # Tkinter Config

        root5 = Tk()
        root5.geometry("580x450+100+100")
        root5.title("WOTM Meal Planner - Add Meal")
        root5.configure(bg="#B8D8D8")
        root5.resizable(False, False)

        # External UI

        addmeal_btn1 = PhotoImage(file=ui_confirm, master=root5)
        addmeal_btn2 = PhotoImage(file=ui_back, master=root5)

        # Variables

        meal_list = ["Breakfast", "Lunch", "Dinner"]

        # Actions

        def home():
            root5.destroy()
            root2.deiconify()

        def add():
            meal_type = cbox1.get()
            meal_entry = ebox1.get()

            class GetEntryDetails:
                def __init__(self, quantity, item, price1, price2):
                    self.quantity = quantity
                    self.item = item
                    self.price1 = price1
                    self.price2 = price2

            field1 = GetEntryDetails(quantity_ebox1.get(), item_ebox1.get(), price_ebox1.get(), price_ebox1.get())
            field2 = GetEntryDetails(quantity_ebox2.get(), item_ebox2.get(), price_ebox2.get(), price_ebox1.get())
            field3 = GetEntryDetails(quantity_ebox3.get(), item_ebox3.get(), price_ebox3.get(), price_ebox1.get())
            field4 = GetEntryDetails(quantity_ebox4.get(), item_ebox4.get(), price_ebox4.get(), price_ebox1.get())
            field5 = GetEntryDetails(quantity_ebox5.get(), item_ebox5.get(), price_ebox5.get(), price_ebox1.get())
            field6 = GetEntryDetails(quantity_ebox6.get(), item_ebox6.get(), price_ebox6.get(), price_ebox1.get())
            field7 = GetEntryDetails(quantity_ebox7.get(), item_ebox7.get(), price_ebox7.get(), price_ebox1.get())
            field8 = GetEntryDetails(quantity_ebox8.get(), item_ebox8.get(), price_ebox8.get(), price_ebox1.get())

            cursor.execute(f"INSERT INTO mealitems VALUES (?,?,?,?,?,?)",
                           (field1.quantity, field1.item, field1.price1, field1.price2, meal_entry, meal_type,))
            cursor.execute(f"INSERT INTO mealitems VALUES (?,?,?,?,?,?)",
                           (field2.quantity, field2.item, field2.price1, field2.price2, meal_entry, meal_type,))
            cursor.execute(f"INSERT INTO mealitems VALUES (?,?,?,?,?,?)",
                           (field3.quantity, field3.item, field3.price1, field3.price2, meal_entry, meal_type,))
            cursor.execute(f"INSERT INTO mealitems VALUES (?,?,?,?,?,?)",
                           (field4.quantity, field4.item, field4.price1, field4.price2, meal_entry, meal_type,))
            cursor.execute(f"INSERT INTO mealitems VALUES (?,?,?,?,?,?)",
                           (field5.quantity, field5.item, field5.price1, field5.price2, meal_entry, meal_type,))
            cursor.execute(f"INSERT INTO mealitems VALUES (?,?,?,?,?,?)",
                           (field6.quantity, field6.item, field6.price1, field6.price2, meal_entry, meal_type,))
            cursor.execute(f"INSERT INTO mealitems VALUES (?,?,?,?,?,?)",
                           (field7.quantity, field7.item, field7.price1, field7.price2, meal_entry, meal_type,))
            cursor.execute(f"INSERT INTO mealitems VALUES (?,?,?,?,?,?)",
                           (field8.quantity, field8.item, field8.price1, field8.price2, meal_entry, meal_type,))

            cursor.execute(f"DELETE FROM mealitems WHERE item = '' or item is null")
            connection.commit()
            cursor.close()

            messagebox.showinfo("WOTM - Add", "A new meal has been added!")

            root5.destroy()
            root1.deiconify()

        # Widgets

        frame1 = Frame(root5, padx=5, pady=5, bg="#B8D8D8")
        frame1.grid(column=0, row=0, padx=45)

        frame2 = Frame(root5, padx=5, pady=5, bg="#B8D8D8")
        frame2.grid(column=0, row=1)

        frame3 = Frame(root5, padx=5, pady=5, bg="#B8D8D8")
        frame3.grid(column=0, row=2, padx=20)

        lbl1 = Label(frame1, text="Breakfast / Lunch / Dinner:", bg="#B8D8D8")
        lbl1.grid(column=0, row=0, pady=5)

        cbox1 = ttk.Combobox(frame1, value=meal_list, width=76)
        cbox1.grid(column=0, row=1)

        lbl2 = Label(frame1, text="Name:", bg="#B8D8D8")
        lbl2.grid(column=0, row=2, pady=5)

        ebox1 = Entry(frame1, width=79)
        ebox1.grid(column=0, row=3)

        lbl3 = Label(frame2, text="Quantity", bg="#B8D8D8")
        lbl3.grid(column=0, row=0, pady=5)

        lbl4 = Label(frame2, text="Item", bg="#B8D8D8")
        lbl4.grid(column=1, row=0, pady=5)

        lbl5 = Label(frame2, text="Price", bg="#B8D8D8")
        lbl5.grid(column=2, row=0, pady=5)

        quantity_ebox1 = Entry(frame2, width=13)
        quantity_ebox1.grid(column=0, row=1)
        item_ebox1 = Entry(frame2, width=52)
        item_ebox1.grid(column=1, row=1)
        price_ebox1 = Entry(frame2, width=13)
        price_ebox1.grid(column=2, row=1)

        quantity_ebox2 = Entry(frame2, width=13)
        quantity_ebox2.grid(column=0, row=2)
        item_ebox2 = Entry(frame2, width=52)
        item_ebox2.grid(column=1, row=2)
        price_ebox2 = Entry(frame2, width=13)
        price_ebox2.grid(column=2, row=2)

        quantity_ebox3 = Entry(frame2, width=13)
        quantity_ebox3.grid(column=0, row=3)
        item_ebox3 = Entry(frame2, width=52)
        item_ebox3.grid(column=1, row=3)
        price_ebox3 = Entry(frame2, width=13)
        price_ebox3.grid(column=2, row=3)

        quantity_ebox4 = Entry(frame2, width=13)
        quantity_ebox4.grid(column=0, row=4)
        item_ebox4 = Entry(frame2, width=52)
        item_ebox4.grid(column=1, row=4)
        price_ebox4 = Entry(frame2, width=13)
        price_ebox4.grid(column=2, row=4)

        quantity_ebox5 = Entry(frame2, width=13)
        quantity_ebox5.grid(column=0, row=5)
        item_ebox5 = Entry(frame2, width=52)
        item_ebox5.grid(column=1, row=5)
        price_ebox5 = Entry(frame2, width=13)
        price_ebox5.grid(column=2, row=5)

        quantity_ebox6 = Entry(frame2, width=13)
        quantity_ebox6.grid(column=0, row=6)
        item_ebox6 = Entry(frame2, width=52)
        item_ebox6.grid(column=1, row=6)
        price_ebox6 = Entry(frame2, width=13)
        price_ebox6.grid(column=2, row=6)

        quantity_ebox7 = Entry(frame2, width=13)
        quantity_ebox7.grid(column=0, row=7)
        item_ebox7 = Entry(frame2, width=52)
        item_ebox7.grid(column=1, row=7)
        price_ebox7 = Entry(frame2, width=13)
        price_ebox7.grid(column=2, row=7)

        quantity_ebox8 = Entry(frame2, width=13)
        quantity_ebox8.grid(column=0, row=8)
        item_ebox8 = Entry(frame2, width=52)
        item_ebox8.grid(column=1, row=8)
        price_ebox8 = Entry(frame2, width=13)
        price_ebox8.grid(column=2, row=8)

        quantity_ebox9 = Entry(frame2, width=13)
        quantity_ebox9.grid(column=0, row=9)
        item_ebox9 = Entry(frame2, width=52)
        item_ebox9.grid(column=1, row=9)
        price_ebox9 = Entry(frame2, width=13)
        price_ebox9.grid(column=2, row=9)

        quantity_ebox10 = Entry(frame2, width=13)
        quantity_ebox10.grid(column=0, row=10)
        item_ebox10 = Entry(frame2, width=52)
        item_ebox10.grid(column=1, row=10)
        price_ebox10 = Entry(frame2, width=13)
        price_ebox10.grid(column=2, row=10)

        btn1 = Button(frame3, command=add, image=addmeal_btn1, borderwidth=0, highlightthickness=0,activebackground='#B8D8D8', bg="#B8D8D8", bd=0, )
        btn1.grid(padx=10, column=0, row=0, pady=25, )

        btn2 = Button(frame3, command=home, image=addmeal_btn2, borderwidth=0, highlightthickness=0,activebackground='#B8D8D8', bg="#B8D8D8", bd=0, )
        btn2.grid(padx=10, column=1, row=0, pady=25, )

        root5.mainloop()

    def window_update_meal():
        root6 = Tk()
        root6.geometry("245x420+100+100")
        root6.title("WOTM Meal Planner - Update Meal | Update Items")
        root6.configure(bg="#B8D8D8")
        root6.resizable(False, False)

        def add():

            # Tkinter Window Config

            root7 = Tk()
            root7.geometry("575x250+100+100")
            root7.title("WOTM Meal Planner - Update Meal | Add")
            root7.configure(bg="#B8D8D8")
            root7.resizable(False, False)

            # Functions

            def add():
                cursor.execute('INSERT INTO mealitems values(?,?,?,?,?,?)', (
                entry_quantity.get(), entry_item.get(), entry_price.get(), entry_price.get(), combo1.get(), 'Dinner',))
                connection.commit()
                cursor.close()
                messagebox.showinfo("WOTM Meal Planner", "A new item has been added!")
                combo1.delete(0, END)
                entry_quantity.delete(0, END)
                entry_item.delete(0, END)
                entry_price.delete(0, END)

            # Data

            meals = []

            for i in cursor.execute('select distinct meal from mealitems;'):
                meals.append(i[-1])

            # UI

            btnimg_add = PhotoImage(file=ui_confirm, master=root7)
            btnimg_bac = PhotoImage(file=ui_back, master=root7)

            # Widgets - Frame 1

            frame1 = Frame(root7, padx=40, pady=20, bg="#B8D8D8")
            frame1.grid(column=0, row=0)

            # Widgets - Frame 2

            frame2 = Frame(frame1, padx=5, pady=5, bg="#B8D8D8")
            frame2.grid(column=0, row=0)

            lbl1 = Label(frame2, text="Select Meal:", bg="#B8D8D8")
            lbl1.grid(column=0, row=0, pady=5)

            combo1 = ttk.Combobox(frame2, width=76, value=meals)
            combo1.grid(column=0, row=1)

            # Widgets - Frame 3

            frame3 = Frame(frame1, padx=5, pady=5, bg="#B8D8D8")
            frame3.grid(column=0, row=1)

            lbl1 = Label(frame3, text="Quantity", bg="#B8D8D8")
            lbl1.grid(column=0, row=0, pady=5)

            lbl2 = Label(frame3, text="Item", bg="#B8D8D8")
            lbl2.grid(column=1, row=0, pady=5)

            lbl3 = Label(frame3, text="Price", bg="#B8D8D8")
            lbl3.grid(column=2, row=0, pady=5)

            entry_quantity = Entry(frame3, width=13)
            entry_quantity.grid(column=0, row=1)

            entry_item = Entry(frame3, width=52)
            entry_item.grid(column=1, row=1)

            entry_price = Entry(frame3, width=13)
            entry_price.grid(column=2, row=1)

            # Widgets - Frame 4

            frame4 = Frame(frame1, padx=5, pady=5, bg="#B8D8D8")
            frame4.grid(column=0, row=2)

            add_btn1 = Button(frame4, command=add, image=btnimg_add, borderwidth=0, highlightthickness=0,
                              activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
            add_btn1.grid(padx=10, column=0, row=0, pady=25)

            add_btn2 = Button(frame4, command=root7.destroy, image=btnimg_bac, borderwidth=0, highlightthickness=0,
                              activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
            add_btn2.grid(padx=10, column=1, row=0, pady=25)

            root7.mainloop()

        def upd():
            root9 = Tk()
            root9.geometry("575x310+100+100")
            root9.title("WOTM Meal Planner - Update Meal")
            root9.configure(bg="#B8D8D8")
            root9.resizable(False, False)

            # Functions

            # UI

            btnimg_add = PhotoImage(file=ui_confirm, master=root9)
            btnimg_bac = PhotoImage(file=ui_back, master=root9)
            btnimg_search = PhotoImage(file=ui_search, master=root9)

            meals = []
            meal_items = []

            # Widgets - Frame 1

            frame1 = Frame(root9, padx=40, pady=20, bg="#B8D8D8")
            frame1.grid(column=0, row=0)

            # Widgets - Frame 2

            frame2 = Frame(frame1, padx=5, pady=5, bg="#B8D8D8")
            frame2.grid(column=0, row=0)

            # Combobox 1

            for meal in cursor.execute('select distinct meal from mealitems;'):
                meals.append(meal[-1])

            newlist = '\n'.join(meals)

            lbl1 = Label(frame2, text="Select Meal:", bg="#B8D8D8")
            lbl1.grid(column=0, row=0, pady=5)

            combo1 = ttk.Combobox(frame2, width=76, value=meals)
            combo1.grid(column=0, row=1)

            def search():
                if combo1.get() in newlist:
                    for i in cursor.execute('select item from mealitems where meal=(?)', (f'{combo1.get()}',)):
                        meal_items.append(i[-1])
                        print(i[-1])
                    lbl2 = Label(frame2, text="Select Item:", bg="#B8D8D8")
                    lbl2.grid(column=0, row=2, pady=5)
                    combo2 = ttk.Combobox(frame2, width=76, values=meal_items)
                    combo2.grid(column=0, row=3)

                def confirm():
                    # sql delete from
                    # cursor.execute('INSERT INTO mealitems values(?,?,?,?,?,?)', (entry_quantity.get(), entry_item.get(), entry_price.get(), entry_price.get(), combo1.get(), 'Dinner',))
                    # connection.commit()
                    messagebox.showinfo("WOTM Meal Planner", "An item has been updated!")
                    combo1.delete(0, END)
                    combo2.delete(0, END)
                    entry_quantity.delete(0, END)
                    entry_item.delete(0, END)
                    entry_price.delete(0, END)

                add_btn2 = Button(frame4, command=confirm, image=btnimg_add, borderwidth=0, highlightthickness=0, activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
                add_btn2.grid(padx=10, column=1, row=0, pady=25)

            # Widgets - Frame 3

            frame3 = Frame(frame1, padx=5, pady=5, bg="#B8D8D8")
            frame3.grid(column=0, row=1)

            lbl3 = Label(frame3, text="Quantity", bg="#B8D8D8")
            lbl3.grid(column=0, row=2, pady=5)

            lbl4 = Label(frame3, text="Item", bg="#B8D8D8")
            lbl4.grid(column=1, row=2, pady=5)

            lbl5 = Label(frame3, text="Price", bg="#B8D8D8")
            lbl5.grid(column=2, row=2, pady=5)

            entry_quantity = Entry(frame3, width=13)
            entry_quantity.grid(column=0, row=3)

            entry_item = Entry(frame3, width=52)
            entry_item.grid(column=1, row=3)

            entry_price = Entry(frame3, width=13)
            entry_price.grid(column=2, row=3)

            # Widgets - Frame 3

            frame4 = Frame(frame1, padx=5, pady=5, bg="#B8D8D8")
            frame4.grid(column=0, row=2)

            add_btn1 = Button(frame4, command=search, image=btnimg_search, borderwidth=0, highlightthickness=0,activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
            add_btn1.grid(padx=10, column=0, row=0, pady=25)

            add_btn3 = Button(frame4, command=root9.destroy, image=btnimg_bac, borderwidth=0, highlightthickness=0,activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
            add_btn3.grid(padx=10, column=2, row=0, pady=25)

            root9.mainloop()

        def delete():
            root8 = Tk()
            root8.geometry("570x250+100+100")
            root8.title("WOTM Meal Planner - Update Meal | Delete Item")
            root8.configure(bg="#B8D8D8")
            root8.resizable(False, False)

            # Functions


            def back():
                root8.destroy()

            # UI

            btnimg_add = PhotoImage(file=ui_confirm, master=root8)
            btnimg_bac = PhotoImage(file=ui_back, master=root8)
            btnimg_search = PhotoImage(file=ui_search, master=root8)

            # Data

            meals = []
            meal_items = []

            # Widgets - Frame 1

            frame1 = Frame(root8, padx=40, pady=20, bg="#B8D8D8")
            frame1.grid(column=0, row=0)

            # Widgets - Frame 2

            frame2 = Frame(frame1, padx=5, pady=5, bg="#B8D8D8")
            frame2.grid(column=0, row=0)

            for meal in cursor.execute('select distinct meal from mealitems;'):
                meals.append(meal[-1])

            newlist = '\n'.join(meals)

            lbl1 = Label(frame2, text="Select Meal:", bg="#B8D8D8")
            lbl1.grid(column=0, row=0, pady=5)

            combo1 = ttk.Combobox(frame2, width=76, value=meals)
            combo1.grid(column=0, row=1)

            lbl1 = Label(frame2, text="Select Meal:", bg="#B8D8D8")
            lbl1.grid(column=0, row=0, pady=5)

            combo1 = ttk.Combobox(frame2, width=76, value=meals)
            combo1.grid(column=0, row=1)

            # Widgets - Frame 2

            frame3 = Frame(frame1, padx=5, pady=5, bg="#B8D8D8")
            frame3.grid(column=0, row=2)

            def search():
                if combo1.get() in newlist:
                    for i in cursor.execute('select item from mealitems where meal=(?)', (f'{combo1.get()}',)):
                        meal_items.append(i[-1])
                    lbl2 = Label(frame2, text="Select Item:", bg="#B8D8D8")
                    lbl2.grid(column=0, row=2, pady=5)
                    combo2 = ttk.Combobox(frame2, width=76, values=meal_items)
                    combo2.grid(column=0, row=3)

                    def confirm():
                        cursor.execute('delete from mealitems where meal=(?) and item=(?)', (f'{combo1.get()}', f'{combo2.get()}',))
                        connection.commit()
                        cursor.close()
                        messagebox.showinfo("WOTM Meal Planner", "An item has been deleted!")
                        combo1.delete(0, END)
                        combo2.delete(0, END)

                    add_btn2 = Button(frame3, command=confirm, image=btnimg_add, borderwidth=0, highlightthickness=0, activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
                    add_btn2.grid(padx=10, column=1, row=0, pady=25)

            add_btn1 = Button(frame3, command=search, image=btnimg_search, borderwidth=0, highlightthickness=0, activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
            add_btn1.grid(padx=10, column=0, row=0, pady=25)

            add_btn3 = Button(frame3, command=back, image=btnimg_bac, borderwidth=0, highlightthickness=0, activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
            add_btn3.grid(padx=10, column=2, row=0, pady=25)

            root8.mainloop()

        def back():
            root6.destroy()

        # UI

        btnimg_add = PhotoImage(file=ui_add2, master=root6)
        btnimg_upd = PhotoImage(file=ui_update, master=root6)
        btnimg_del = PhotoImage(file=ui_delete, master=root6)
        btnimg_bac = PhotoImage(file=ui_back, master=root6)

        # Widgets - Frame 1

        frame1 = Frame(root6, padx=40, pady=20, bg="#B8D8D8")
        frame1.grid(column=0, row=0)

        btn1 = Button(frame1, command=add, image=btnimg_add, borderwidth=0, highlightthickness=0, activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
        btn1.grid(padx=10, column=0, row=0, pady=25)

        btn2 = Button(frame1, command=upd, image=btnimg_upd, borderwidth=0, highlightthickness=0, activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
        btn2.grid(padx=10, column=0, row=1, pady=25)

        btn3 = Button(frame1, command=delete, image=btnimg_del, borderwidth=0, highlightthickness=0, activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
        btn3.grid(padx=10, column=0, row=2, pady=25)

        btn4 = Button(frame1, command=back, image=btnimg_bac, borderwidth=0, highlightthickness=0, activebackground='#B8D8D8', bg="#B8D8D8", bd=0)
        btn4.grid(padx=10, column=0, row=3, pady=25)

        root6.mainloop()

    def home():
        root2.destroy()
        root1.deiconify()

    def add_meal():
        root2.withdraw()
        window_addmeal()

    def remove_meal():
        response = messagebox.askyesno("WOTM - View Meals", f"Are you sure you want to delete this meal?")
        if response == 1:
            x = tree.selection()[0]
            uid = tree.item(x)["values"][1]
            tree.delete(x)
            cursor.execute("DELETE FROM mealitems where meal=?", (uid,))
            messagebox.showinfo("WOTM - View Meals", f"{uid} has been deleted!")
            connection.commit()
            cursor.close()

    # Widgets

    frame1 = Frame(root2, padx=5, pady=5, bg="#B8D8D8")
    frame1.pack(padx=10, pady=30)

    frame2 = Frame(root2, padx=5, pady=5, bg="#B8D8D8")
    frame2.pack()

    scrollbar = Scrollbar(frame1, orient=VERTICAL)
    tree = ttk.Treeview(frame1, height=12, selectmode=EXTENDED, yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    scrollbar.config(command=tree.yview)

    # Treeview - Define Columns

    tree["columns"] = ("Type", "Name")

    # Treeview - Format Columns

    tree.column("#0", width=0, stretch=NO)
    tree.column("Type", anchor=CENTER, width=80)
    tree.column("Name", anchor=CENTER, width=400)

    # Treeview - Create Headings

    tree.heading("#0", text="", anchor=W)
    tree.heading("Type", text="Type", anchor=CENTER)
    tree.heading("Name", text="Name", anchor=CENTER)

    tree.grid(column=0, row=0)

    # Treeview - Contents

    global count

    for item in cursor.execute("SELECT DISTINCT meal_type, meal FROM mealitems ORDER BY meal_type, meal ASC;"):
        tree.insert(parent="", index="end", iid=count, text="", values=item)
        count += 1

    # Widgets

    btn1 = Button(frame2, command=add_meal, image=viewmenu_btnimg1, borderwidth=0, highlightthickness=0,
                  activebackground="#B8D8D8", bg="#B8D8D8", bd=0)
    btn1.grid(column=0, row=1, padx=15)

    btn2 = Button(frame2, command=remove_meal, image=viewmenu_btnimg2, borderwidth=0, highlightthickness=0,
                  activebackground="#B8D8D8", bg="#B8D8D8", bd=0)
    btn2.grid(column=1, row=1, padx=15)

    btn3 = Button(frame2, command=window_update_meal, image=viewmenu_btnimg3, borderwidth=0, highlightthickness=0,
                  activebackground="#B8D8D8", bg="#B8D8D8", bd=0)
    btn3.grid(column=2, row=1, padx=15)

    btn4 = Button(frame2, command=home, image=viewmenu_btnimg4, borderwidth=0, highlightthickness=0,
                  activebackground="#B8D8D8", bg="#B8D8D8", bd=0)
    btn4.grid(column=3, row=1, padx=15)

    root2.mainloop()


def window_viewitems():
    # Tkinter Config

    root3 = Tk()
    root3.geometry("580x555+100+100")
    root3.title("WOTM Meal Planner - View Items")
    root3.configure(bg="#B8D8D8")
    root3.resizable(False, False)

    # External UI

    viewitems_btn1 = PhotoImage(file=ui_add_item, master=root3)
    viewitems_btn2 = PhotoImage(file=ui_remove_item, master=root3)
    viewitems_btn3 = PhotoImage(file=ui_home, master=root3)

    # Actions

    def home():
        root3.destroy()
        root1.deiconify()

    def add_item():
        global count
        tree.insert(parent="", index="end", iid=count, text="",
                    values=(content1.get(), content2.get(), content3.get(),))
        count += 1
        cursor.execute("INSERT INTO _other values (?,?,?,?)",
                       (content1.get(), content2.get(), content3.get(), content3.get()))
        connection.commit()
        cursor.close()
        namebox1.delete(0, END)
        namebox2.delete(0, END)
        namebox3.delete(0, END)

    def remove_item():
        x = tree.selection()[0]
        uid = tree.item(x)["values"][3]
        tree.delete(x)
        cursor.execute("DELETE FROM _other where rowid=?", (uid,))
        connection.commit()
        cursor.close()

    # Widgets

    frame3 = Frame(root3, bg="#B8D8D8")
    frame3.pack(pady=20)

    frame1 = Frame(root3, padx=5, bg="#B8D8D8")
    frame1.pack(pady=5)

    frame2 = Frame(root3, padx=5, pady=5, bg="#B8D8D8")
    frame2.pack(pady=30)

    btn1 = Button(frame2, command=add_item, image=viewitems_btn1, borderwidth=0, highlightthickness=0,
                  activebackground='#B8D8D8', bg="#B8D8D8", bd=0, )
    btn1.grid(padx=10, column=0, row=3)

    btn2 = Button(frame2, command=remove_item, image=viewitems_btn2, borderwidth=0, highlightthickness=0,
                  activebackground='#B8D8D8', bg="#B8D8D8", bd=0, )
    btn2.grid(padx=10, column=1, row=3)

    btn3 = Button(frame2, command=home, image=viewitems_btn3, borderwidth=0, highlightthickness=0,
                  activebackground='#B8D8D8', bg="#B8D8D8", bd=0, )
    btn3.grid(padx=10, column=2, row=3)

    label1 = Label(frame3, text="Quantity", bg="#B8D8D8")
    label1.grid(pady=5, column=0, row=0)

    label2 = Label(frame3, text="Item(s)", bg="#B8D8D8")
    label2.grid(pady=5, column=1, row=0)

    label3 = Label(frame3, text="Price", bg="#B8D8D8")
    label3.grid(pady=5, column=2, row=0)

    content1 = StringVar(root3)
    content2 = StringVar(root3)
    content3 = StringVar(root3)

    namebox1 = Entry(frame3, width=13, textvariable=content1)
    namebox1.grid(column=0, row=1)

    namebox2 = Entry(frame3, width=52, textvariable=content2)
    namebox2.grid(column=1, row=1)

    namebox3 = Entry(frame3, width=13, textvariable=content3)
    namebox3.grid(column=2, row=1)

    scrollbar = Scrollbar(frame1, orient=VERTICAL)
    tree = ttk.Treeview(frame1, height=15, selectmode=EXTENDED, yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)
    scrollbar.grid(row=1, column=1, sticky="ns")
    scrollbar.config(command=tree.yview)

    # Treeview - Define Columns

    tree["columns"] = ("Quantity", "item", "Price", "ID")
    tree["displaycolumns"] = ("Quantity", "item", "Price",)

    # Treeview - Format Columns

    tree.column("#0", width=0, stretch=NO)
    tree.column("Quantity", anchor=CENTER, width=80)
    tree.column("item", anchor=CENTER, width=320)
    tree.column("Price", anchor=CENTER, width=80)
    tree.column("ID", anchor=CENTER, width=40)

    # Treeview - Create Headings

    tree.heading("#0", text="", anchor=W)
    tree.heading("Quantity", text="Quantity", anchor=CENTER)
    tree.heading("item", text="Item(s)", anchor=CENTER)
    tree.heading("Price", text="Price", anchor=CENTER)
    tree.heading("ID", text="ID", anchor=CENTER)

    # Treeview - Contents

    global count

    for item in cursor.execute("select *, rowid from _other;"):
        tree.insert(parent="", index="end", iid=count, text="", values=(item[0], item[1], f"£{item[2]}", item[4]))
        count += 1

    tree.grid(column=0, row=1)

    root3.mainloop()


def window_generateshopping():
    # Tkinter Config

    root4 = Tk()
    root4.geometry("920x540+100+100")
    root4.title("WOTM Meal Planner - Generate Shopping")
    root4.configure(bg="#B8D8D8")
    root4.resizable(False, False)

    # Widgets

    frame1 = Frame(root4, padx=5, pady=5, bg="#B8D8D8")
    frame1.grid(column=1, row=0, pady=25)

    frame2 = Frame(root4, padx=5, pady=5, bg="#B8D8D8")
    frame2.grid(column=0, row=1, columnspan=3, padx=1, pady=2)

    frame3 = Frame(root4, padx=5, pady=5, bg="#B8D8D8")
    frame3.grid(column=0, row=0, padx=1, pady=5)

    # External UI

    generateshopping_btn1 = PhotoImage(file=ui_increase_quantity, master=root4)
    generateshopping_btn2 = PhotoImage(file=ui_decrease_quantity, master=root4)
    generateshopping_btn3 = PhotoImage(file=ui_generate_shopping, master=root4)
    generateshopping_btn4 = PhotoImage(file=ui_home, master=root4)
    generateshopping_btn5 = PhotoImage(file=ui_refresh, master=root4)

    # Actions

    def quant_increase():

        global count

        delete_list = []
        item_selection = tree.selection()

        # Add 1 from quantity column when selected.

        for item in item_selection:
            delete_list.append(tree.item(item, "values")[3])
            cursor.executemany("UPDATE _temp SET quantity = quantity + 1 WHERE rowid=?", [(a,) for a in delete_list])
            cursor.executemany("UPDATE _temp SET price = price + r_price WHERE rowid=?", [(a,) for a in delete_list])
            connection.commit()
            cursor.close()

        # Clear Treeview

        tree.delete(*tree.get_children())

        # Refresh Treeview

        for item in cursor.execute(
                "select quantity, item, printf('%.2f', quantity * r_price) as price, r_price, rowid from _temp;"):
            tree.insert(parent="", index="end", iid=count, text="", values=(item[0], item[1], f"£{item[2]}", item[4]))
            count += 1

        # Refresh Item Count and Price

    def quant_decrease():

        global count

        delete_list = []
        item_selection = tree.selection()

        # Remove 1 from quantity column when selected.

        for item in item_selection:
            delete_list.append(tree.item(item, "values")[3])
            cursor.executemany("UPDATE _temp SET quantity = quantity - 1 WHERE rowid=?", [(a,) for a in delete_list])
            cursor.executemany("UPDATE _temp SET price = price - r_price WHERE rowid=?", [(a,) for a in delete_list])
            cursor.execute("DELETE FROM _temp WHERE quantity=0;")
            connection.commit()
            cursor.close()

        # Clear Treeview

        tree.delete(*tree.get_children())

        # Refresh Treeview

        for item in cursor.execute(
                "select quantity, item, printf('%.2f', quantity * r_price) as price, r_price, rowid from _temp;"):
            tree.insert(parent="", index="end", iid=count, text="", values=(item[0], item[1], f"£{item[2]}", item[4]))
            count += 1

    def generate():

        def file_meals():
            return (str(f"Meal 1: {items1[0]}\n"
                        f"Meal 2: {items2[0]}\n"
                        f"Meal 3: {items3[0]}\n"
                        f"Meal 4: {items4[0]}\n"
                        f"Meal 5: {items5[0]}"))

        def file_item():
            all_items = []
            for i in cursor.execute("select * from _temp;"):
                all_items.append(f"{i[0]} | {i[1]}")
            return all_items[:-1]

        def end():
            mail = messagebox.askyesno("WOTM - Generate Shopping", f"Would you like this emailed to {mailbox}?")
            if mail == 1:
                outlook = win32.Dispatch("outlook.application")
                mail = outlook.CreateItem(0)
                mail.To = f"{mailbox}"
                mail.Subject = "WOTM - Your meals and shopping list for this week!"
                mail.Body = f"Hi {user}!" \
                            f"\n\nHere are the meals WOTM has selected for this week:\n\n" \
                            f"{file_meals()}" \
                            f"\n\nAnd here are the item you need this week:" \
                            f"\n{linebreak}{linebreak.join(file_item())}"
                mail.Send()
                messagebox.showinfo("WOTM - Generate Shopping", "Your shopping list has been generated!")
                root4.destroy()
                root1.destroy()

                cursor.execute("delete from _temp;")
                connection.commit()
                cursor.close()

        end()

    def meal_data():
        global items1
        global items2
        global items3
        global items4
        global items5
        global tree

        # Clears content from table _temp and _sorted.

        cursor.execute("delete from _temp;")
        cursor.execute("delete from _sorted;")

        # Generate list of meals and select 1 at random.

        meal1 = cursor.execute("SELECT meal FROM mealitems ORDER BY RANDOM() LIMIT 5;")
        meal2 = cursor.execute("SELECT meal FROM mealitems ORDER BY RANDOM() LIMIT 5;")
        meal3 = cursor.execute("SELECT meal FROM mealitems ORDER BY RANDOM() LIMIT 5;")
        meal4 = cursor.execute("SELECT meal FROM mealitems ORDER BY RANDOM() LIMIT 5;")
        meal5 = cursor.execute("SELECT meal FROM mealitems ORDER BY RANDOM() LIMIT 5;")

        # Iterate through each meal list.

        for items1, items2, items3, items4, items5 in zip(meal1, meal2, meal3, meal4, meal5):
            cursor.execute(
                f'''INSERT INTO _sorted SELECT quantity, item, printf('%.2f', price) as price, printf('%.2f', r_price) as r_price FROM mealitems where meal="{items1[0]}"''')
            cursor.execute(
                f'''INSERT INTO _sorted SELECT quantity, item, printf('%.2f', price) as price, printf('%.2f', r_price) as r_price FROM mealitems where meal="{items2[0]}"''')
            cursor.execute(
                f'''INSERT INTO _sorted SELECT quantity, item, printf('%.2f', price) as price, printf('%.2f', r_price) as r_price FROM mealitems where meal="{items3[0]}"''')
            cursor.execute(
                f'''INSERT INTO _sorted SELECT quantity, item, printf('%.2f', price) as price, printf('%.2f', r_price) as r_price FROM mealitems where meal="{items4[0]}"''')
            cursor.execute(
                f'''INSERT INTO _sorted SELECT quantity, item, printf('%.2f', price) as price, printf('%.2f', r_price) as r_price FROM mealitems where meal="{items5[0]}"''')
            connection.commit()
            cursor.close()

        # Insert data into _temp table.

        cursor.execute(
            "insert into _temp select sum(quantity) as quantity, item, printf('%.2f', price) as price, printf('%.2f', r_price) as r_price from _sorted group by quantity, item, price, r_price ORDER BY rowid ASC;")
        cursor.execute(
            "insert into _temp select quantity, item, printf('%.2f', price) as price, printf('%.2f', r_price) as r_price from _other;")
        connection.commit()
        cursor.close()

        # Labels

        Label(frame3, bg="#FFFFFF", width=40, height=4, text=f"{items1[0]}").grid(column=0, row=0, pady=7, padx=35)
        Label(frame3, bg="#FFFFFF", width=40, height=4, text=f"{items2[0]}").grid(column=0, row=1, pady=7, padx=35)
        Label(frame3, bg="#FFFFFF", width=40, height=4, text=f"{items3[0]}").grid(column=0, row=2, pady=7, padx=35)
        Label(frame3, bg="#FFFFFF", width=40, height=4, text=f"{items4[0]}").grid(column=0, row=3, pady=7, padx=35)
        Label(frame3, bg="#FFFFFF", width=40, height=4, text=f"{items5[0]}").grid(column=0, row=4, pady=7, padx=35)

    meal_data()

    def refresh():
        meal_data()
        treeview_data()

    def home():
        root4.destroy()
        root1.deiconify()

    # Widgets

    btn1 = Button(frame2, command=quant_increase, image=generateshopping_btn1, borderwidth=0, highlightthickness=0,
                  activebackground="#B8D8D8", bg="#B8D8D8", bd=0)
    btn1.grid(padx=15, column=0, row=0)

    btn2 = Button(frame2, command=quant_decrease, image=generateshopping_btn2, borderwidth=0, highlightthickness=0,
                  activebackground="#B8D8D8", bg="#B8D8D8", bd=0)
    btn2.grid(padx=15, column=1, row=0)

    btn6 = Button(frame2, command=refresh, image=generateshopping_btn5, borderwidth=0, highlightthickness=0,
                  activebackground="#B8D8D8", bg="#B8D8D8", bd=0, )
    btn6.grid(padx=15, column=2, row=0)

    btn3 = Button(frame2, command=generate, image=generateshopping_btn3, borderwidth=0, highlightthickness=0,
                  activebackground="#B8D8D8", bg="#B8D8D8", bd=0, )
    btn3.grid(padx=15, column=3, row=0)

    btn4 = Button(frame2, command=home, image=generateshopping_btn4, borderwidth=0, highlightthickness=0,
                  activebackground="#B8D8D8", bg="#B8D8D8", bd=0, )
    btn4.grid(padx=15, column=4, row=0)

    scrollbar = Scrollbar(frame1, orient=VERTICAL)
    tree = ttk.Treeview(frame1, height=18, selectmode=EXTENDED, yscrollcommand=scrollbar.set)
    scrollbar.config(command=tree.yview)
    scrollbar.grid(row=0, column=1, sticky="ns")
    scrollbar.config(command=tree.yview)

    # Treeview - Define Columns

    tree["columns"] = ("Quantity", "item", "Price", "ID")
    tree["displaycolumns"] = ("Quantity", "item", "Price")

    # Treeview - Format Columns

    tree.column("#0", width=0, stretch=NO)
    tree.column("Quantity", anchor=CENTER, width=80)
    tree.column("item", anchor=CENTER, width=320)
    tree.column("Price", anchor=CENTER, width=80)
    tree.column("ID", anchor=CENTER, width=40)

    # Treeview - Create Headings

    tree.heading("#0", text="", anchor=W)
    tree.heading("Quantity", text="Quantity", anchor=CENTER)
    tree.heading("item", text="Item(s)", anchor=CENTER)
    tree.heading("Price", text="Price", anchor=CENTER)
    tree.heading("ID", text="ID", anchor=CENTER)

    tree.grid(column=0, row=0)

    def treeview_data():

        global count

        for i in tree.get_children():
            tree.delete(i)

        for item in cursor.execute(
                "select quantity, item, printf('%.2f', quantity * r_price) as price, r_price, rowid from _temp;"):
            tree.insert(parent="", index="end", iid=count, text="", values=(item[0], item[1], f"£{item[2]}", item[4]))
            count += 1

    treeview_data()

    root4.mainloop()


window_main()
