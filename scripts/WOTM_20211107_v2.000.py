# Modules

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import datetime
import sys
import sqlite3
import os

# Variables

user = os.getlogin()
db = os.path.join(r"C:\Users\{}\Dropbox\Programming\Databases\wotmdb.db").format(user)
today = datetime.datetime.today().strftime("%Y%m%d")
verno = (str(2.000))
count = 0

# Database Connection

connection = sqlite3.connect(db)
cursor = connection.cursor()

def window_viewmenu():

    # Tkinter Config

    root2 = Tk()
    root2.geometry("700x425")
    #root2.iconbitmap(".ico)
    root2.title("WOTM - View Menu")
    root2.configure(bg="#B8D8D8")
    root2.resizable(False, False)

    # External UI

    viewmenu_btnimg1 = PhotoImage(file=r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\UI\button_home.png", master=root2)

    # Widgets

    frame1 = Frame(root2, padx=5, pady=5, bg="#B8D8D8")
    frame2 = Frame(root2, padx=5, pady=5, bg="#B8D8D8")
    tree = ttk.Treeview(frame1, height=12,)

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

    # Treeview - Contents

    global count
    sql_viewmenu = cursor.execute("select meal_type, meal from _meals;")
    for i in sql_viewmenu:
        tree.insert(parent="", index="end", iid=count, text="", values=(i))
        count +=1

    btn1 = Button(
        frame2,
        command=root2.destroy,
        image=viewmenu_btnimg1,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#B8D8D8",
        bg="#B8D8D8",
        bd=0)

    # Tkinter Layout Management

    btn1.grid(column=0, row=1)
    frame1.pack(padx=10, pady=30)
    frame2.pack()
    tree.grid(column=0, row=0)


    root2.mainloop()

def window_scratchpad():

    # Tkinter Config

    root3 = Tk()
    root3.geometry("700x425")
    #root3.iconbitmap(".ico)
    root3.title("WOTM - Scratchpad")
    root3.configure(bg="#B8D8D8")
    root3.resizable(False, False)

    # External UI

    scratchpad_btnimg1 = PhotoImage(file=r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\UI\button_add.png", master=root3)
    scratchpad_btnimg2 = PhotoImage(file=r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\UI\button_remove-item.png", master=root3)
    scratchpad_btnimg3 = PhotoImage(file=r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\UI\button_home.png", master=root3)

    # Actions

    def add_record():
        global count
        tree.insert(parent="", index="end", iid=count, text="", values=(content1.get(), content2.get(), content3.get(),))
        count += 1
        cursor.execute("INSERT INTO _scratchpad values (?,?,?)", (content1.get(), content2.get(), content3.get(),))
        connection.commit()
        namebox1.delete(0, END)
        namebox2.delete(0, END)
        namebox3.delete(0, END)

    def removeitem():
        x = tree.selection()[0]
        uid = tree.item(x)["values"][3]
        tree.delete(x)
        cursor.execute("DELETE FROM _scratchpad where rowid=?", (uid,))
        connection.commit()
        messagebox.showinfo("WOTM - Generate Shopping", "Item has been removed.")

    # Widgets

    frame3 = Frame(root3, bg="#B8D8D8")
    frame2 = Frame(root3, padx=5, pady=5, bg="#B8D8D8")
    frame1 = Frame(root3, padx=5, bg="#B8D8D8")

    content1 = StringVar(root3)
    content2 = StringVar(root3)
    content3 = StringVar(root3)

    namebox1 = Entry(frame3, width=13, textvariable=content1)
    namebox2 = Entry(frame3, width=52, textvariable=content2)
    namebox3 = Entry(frame3, width=13, textvariable=content3)

    tree = ttk.Treeview(frame1)

    # Treeview - Define Columns

    tree["columns"] = ("Quantity", "Items", "Price", "ID")
    tree["displaycolumns"] = ("Quantity", "Items", "Price",)

    # Treeview - Format Columns

    tree.column("#0", width=0, stretch=NO)
    tree.column("Quantity", anchor=CENTER, width=80)
    tree.column("Items", anchor=CENTER, width=320)
    tree.column("Price", anchor=CENTER, width=80)
    tree.column("ID", anchor=CENTER, width=40)

    # Treeview - Create Headings

    tree.heading("#0", text="", anchor=W)
    tree.heading("Quantity", text="Quantity", anchor=CENTER)
    tree.heading("Items", text="Item(s)", anchor=CENTER)
    tree.heading("Price", text="Price", anchor=CENTER)
    tree.heading("ID", text="ID", anchor=CENTER)

    # Treeview - Contents

    global count
    sql_scratchpad = cursor.execute("select *, rowid from _scratchpad;")
    for i in sql_scratchpad:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3]))
        count += 1

    btn1 = Button(
        frame2,
        command=add_record,
        image=scratchpad_btnimg1,
        borderwidth=0,
        highlightthickness=0,
        activebackground='#B8D8D8',
        bg="#B8D8D8",
        bd=0,)

    btn2 = Button(
        frame2,
        command=removeitem,
        image=scratchpad_btnimg2,
        borderwidth=0,
        highlightthickness=0,
        activebackground='#B8D8D8',
        bg="#B8D8D8",
        bd=0,)

    btn3 = Button(
        frame2,
        command=root3.destroy,
        image=scratchpad_btnimg3,
        borderwidth=0,
        highlightthickness=0,
        activebackground='#B8D8D8',
        bg="#B8D8D8",
        bd=0,)

    # Tkinter Layout Management

    btn1.grid(padx=10, column=0, row=3,)
    btn2.grid(padx=10, column=1, row=3,)
    btn3.grid(padx=10, column=2, row=3,)
    namebox1.grid(column=0, row=0)
    namebox2.grid(column=1, row=0)
    namebox3.grid(column=2, row=0)
    frame3.pack(pady=20)
    frame1.pack(pady=5)
    frame2.pack(pady=30)
    tree.grid(column=0, row=1)

    root3.mainloop()

def window_generateshopping():

    # Tkinter Config

    root4 = Tk()
    root4.geometry("700x425")
    #root4.iconbitmap(".ico)
    root4.title("WOTM - Generate Shopping")
    root4.configure(bg="#B8D8D8")
    root4.resizable(False, False)
    frame1 = Frame(root4, padx=5, pady=5, bg="#B8D8D8")
    frame2 = Frame(root4, padx=5, pady=5, bg="#B8D8D8")

    # External UI

    generate_btnimg1 = PhotoImage(file=r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\UI\button_generate-shopping.png", master=root4)
    generate_btnimg2 = PhotoImage(file=r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\UI\button_remove-item.png", master=root4)
    generate_btnimg3 = PhotoImage(file=r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\UI\button_home.png", master=root4)

    # Actions

    def estcost():
        sql_estprice = cursor.execute("select ROUND(sum(price),2) from _temp;")
        for i in sql_estprice:
            Label(frame1, width=68, bg="#FFFFFF", text="Estimated Cost: GBP " + str(i[0])).grid(column=0, row=1)

    def itemcount():
        sql_itemcount = cursor.execute("select count (ingredients) from _temp;")
        for i in sql_itemcount:
            Label(frame1, width=68, bg="#FFFFFF", text="Number of Items: " + str(i[0])).grid(column=0, row=2)

    def generateshopping():
        sql_generateshopping = cursor.execute("select * from _temp;")
        f = open(r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\logs\wotm_shopping_" + today + ".txt ", "w")
        for i in sql_generateshopping:
            f.write(str(i[0]) + " | " + (str(i[1])) + "\n")
        f.close()
        cursor.execute("delete from _temp;")
        cursor.execute("delete from _scratchpad;")
        connection.commit()
        messagebox.showinfo("WOTM - Generate Shopping", "Shopping List has been generated!")

    def removeitem():
        x = tree.selection()[0]
        uid = tree.item(x)["values"][3]
        tree.delete(x)
        cursor.execute("DELETE FROM _temp where rowid=?", (uid,))
        connection.commit()
        estcost()
        itemcount()
        messagebox.showinfo("WOTM - Generate Shopping", "Item has been removed.")

    estcost()
    itemcount()

    # Widgets

    tree = ttk.Treeview(frame1)

    # Treeview - Define Columns

    tree["columns"] = ("Quantity", "Items", "Price", "ID")
    tree["displaycolumns"]=("Quantity", "Items", "Price")

    # Treeview - Format Columns

    tree.column("#0", width=0, stretch=NO)
    tree.column("Quantity", anchor=CENTER, width=80)
    tree.column("Items", anchor=CENTER, width=320)
    tree.column("Price", anchor=CENTER, width=80)
    tree.column("ID", anchor=CENTER, width=40)

    # Treeview - Create Headings

    tree.heading("#0", text="", anchor=W)
    tree.heading("Quantity", text="Quantity", anchor=CENTER)
    tree.heading("Items", text="Item(s)", anchor=CENTER)
    tree.heading("Price", text="Price", anchor=CENTER)
    tree.heading("ID", text="ID", anchor=CENTER)

    # Treeview - Contents

    global count
    sql_shoppinglist = cursor.execute("select distinct *, rowid from _temp;")
    for i in sql_shoppinglist:
        tree.insert(parent="", index="end", iid=count, text="", values=(i[0], i[1], i[2], i[3]))
        count += 1

    btn1 = Button(
        frame2,
        command=generateshopping,
        image=generate_btnimg1,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#B8D8D8",
        bg="#B8D8D8",
        bd=0)

    btn2 = Button(
        frame2,
        command=removeitem,
        image=generate_btnimg2,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#B8D8D8",
        bg="#B8D8D8",
        bd=0)

    btn3 = Button(
        frame2,
        command=root4.destroy,
        image=generate_btnimg3,
        borderwidth=0,
        highlightthickness=0,
        activebackground="#B8D8D8",
        bg="#B8D8D8",
        bd=0,)

    # Tkinter Layout Management

    btn1.grid(padx=15,column=0,row=0)
    btn2.grid(padx=15,column=1,row=0)
    btn3.grid(padx=15,column=2,row=0)
    frame1.pack(padx=10, pady=30)
    frame2.pack()
    tree.grid(column=0, row=0)

    root4.mainloop()

def window_main():

    # Tkinter Config

    root1 = Tk()
    root1.geometry("300x425")
    #root.iconbitmap(".ico)
    root1.title("WOTM - What's On The Menu!")
    root1.configure(bg="#B8D8D8")
    root1.resizable(False, False)

    # External UI

    btnimg1_mainmenu = PhotoImage(file=r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\UI\button_view-menu.png")
    btnimg2_mainmenu = PhotoImage(file=r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\UI\button_scratchpad.png")
    btnimg3_mainmenu = PhotoImage(file=r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\UI\button_generate-shopping.png")
    btnimg4_mainmenu = PhotoImage(file=r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\UI\button_exit.png")

    # Actions

    def btncmd_mainmenu_viewmenu():
        window_viewmenu()

    def btncmd_mainmenu_scratchpad():
        cursor.execute("insert into _temp select * from _scratchpad;")
        connection.commit()
        window_scratchpad()

    def btncmd_mainmenu_generateshopping():
        cursor.execute("delete from _temp;")

        auto1 = cursor.execute("SELECT name FROM sqlite_master WHERE name LIKE ? ORDER BY RANDOM() LIMIT 5;", ("dinner%",))
        f = open(r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\logs\wotm_meals_"  + today + ".txt", "a")
        for i in auto1:
            cursor.execute('''INSERT INTO _temp SELECT * FROM {}'''.format(i[0]), )
            connection.commit()
            f.write(str((i[0])) + "\n")
            f.close()

        auto2 = cursor.execute("SELECT name FROM sqlite_master WHERE name LIKE ? ORDER BY RANDOM() LIMIT 5;", ("dinner%",))
        f = open(r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\logs\wotm_meals_"  + today + ".txt", "a")
        for i in auto2:
            cursor.execute('''INSERT INTO _temp SELECT * FROM {}'''.format(i[0]), )
            connection.commit()
            f.write(str((i[0])) + "\n")
            f.close()

        auto3 = cursor.execute("SELECT name FROM sqlite_master WHERE name LIKE ? ORDER BY RANDOM() LIMIT 5;", ("dinner%",))
        f = open(r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\logs\wotm_meals_"  + today + ".txt", "a")
        for i in auto3:
            cursor.execute('''INSERT INTO _temp SELECT * FROM {}'''.format(i[0]), )
            connection.commit()
            f.write(str((i[0])) + "\n")
            f.close()

        auto4 = cursor.execute("SELECT name FROM sqlite_master WHERE name LIKE ? ORDER BY RANDOM() LIMIT 5;", ("dinner%",))
        f = open(r"C:\Users\Kelv\Dropbox\Programming\Python\Projects\Completed\WOTM - What's On The Menu!\logs\wotm_meals_"  + today + ".txt", "a")
        for i in auto4:
            cursor.execute('''INSERT INTO _temp SELECT * FROM {}'''.format(i[0]), )
            connection.commit()
            f.write(str((i[0])) + "\n")
            f.close()

        cursor.execute("insert into _temp select * from _other;")
        cursor.execute("insert into _temp select * from _em;")
        cursor.execute("insert into _temp select * from _scratchpad;")
        connection.commit()

        window_generateshopping()

    # Widgets

    btn1 = Button(
        command=btncmd_mainmenu_viewmenu,
        image=btnimg1_mainmenu,
        borderwidth=0,
        highlightthickness=0,
        activebackground='#B8D8D8',
        bg="#B8D8D8",
        bd=0,)

    sep1 = ttk.Separator()

    btn2 = Button(
        command=btncmd_mainmenu_scratchpad,
        image=btnimg2_mainmenu,
        borderwidth=0,
        highlightthickness=0,
        activebackground='#B8D8D8',
        bg="#B8D8D8",
        bd=0,)

    sep2 = ttk.Separator()

    btn3 = Button(
        command=btncmd_mainmenu_generateshopping,
        image=btnimg3_mainmenu,
        borderwidth=0,
        highlightthickness=0,
        activebackground='#B8D8D8',
        bg="#B8D8D8",
        bd=0,)

    sep3 = ttk.Separator()

    btn4 = Button(
        command=root1.destroy,
        image=btnimg4_mainmenu,
        borderwidth=0,
        highlightthickness=0,
        activebackground='#B8D8D8',
        bg="#B8D8D8",
        bd=0,)

    sep4 = ttk.Separator()

    label2 = Label(
        text="Created by Kelv Gooding\n© 2021 Copyright. All rights reserved.\n" + " Version " + verno,
        bg="#B8D8D8")

    # Tkinter Layout Management

    btn1.grid(column=0, row=1, padx=80, pady=20)
    sep1.place(x=118, y=82, relwidth=0.2)
    btn2.grid(column=0, row=2, padx=80, pady=20)
    sep2.place(x=118, y=164, relwidth=0.2)
    btn3.grid(column=0, row=4, padx=80, pady=20)
    sep3.place(x=118, y=246, relwidth=0.2)
    btn4.grid(column=0, row=5, padx=80, pady=20)
    sep4.place(x=118, y=328, relwidth=0.2)
    label2.grid(column=0, row=7, pady=15)

    root1.mainloop()
window_main()