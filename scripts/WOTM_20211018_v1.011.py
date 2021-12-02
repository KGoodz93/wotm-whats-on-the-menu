from tkinter import *
from tkinter import ttk
import sys
import os
import datetime
import random
import win32com.client as win32

# Variables

clear = lambda: os.system("cls")
today = datetime.datetime.today().strftime("%Y%m%d")
verno = (str(1.011))

# Tkinter Variables
# Tkinter Variables

root = Tk()
root.geometry("537x570")
root.title("WOTM - What's On The Menu!")
root.configure(bg="#d9d7e3")
root.resizable(False, False)

kelv1 = [
        "Tesco White Bread Loaf\n",
        "Drink - Apple Juice\n",
        "Drink - Tropical Carton\n",
        "Drink - Blackcurrent Squash\n",
        "Cheddar Cheese\n",
        "Skinny Chips\n",
        "Maggi Noodles - Chicken\n",
        "Butter\n"
        "Pizza Express - American Hot\n",
        "Chicago Town Pizza - Margarita\n\n"
    ]
kelv2 = [
    "Shower Gel\n",
    "Deodorant\n",
    "Antiperspirant\n",
    "Lotion - Cocoa Butter\n",
    "Shampoo\n\n",
]
essentials = [
    "Toilet Roll\n",
    "Kitchen Roll\n",
    "Handwash\n",
    "Black Bin Bags\n",
    "Small Bin Bags\n",
    "Washing Up Liquid\n",
    "Washing Capsules - Lavender\n",
    "Washing Gems - Lavender\n",
    "Foil\n",
    "Clingfilm\n",
    "Baking Paper\n",
    "Antibacterial Spray\n",
    "Bathroom Cleaner\n",
    "Toilet Gel\n",
    "Viakal\n",
    "Polish\n",
    "Glass Cleaner\n",
    "Oven Cleaner\n",
    "Drain Unblocker\n",
    "Flash Mop Wipes\n",
    "Disinfectant\n",
    "Bleach\n\n",
]
emma1 = [
    "Brioche\n",
    "New York Bakery Plain Bagel\n",
    "Mozzarella Sticks\n",
    "Drink - Lemon Squash\n",
    "Drink - Pepsi\n",
    "Drink - Fanta Orange\n",
    "Drink - Lilt\n",
    "Drink - Sprite\n",
    "Drink - Apple & Mango Juice\n",
    "Drink - Breakfast Juice\n",
    "Magic Stars Chocolate\n",
    "White Chocolate Bar\n",
    "Haribo Starmix\n",
    "Skittles\n",
    "Flake Ice Cream\n",
    "Yoghurt - Dairy Milk Ports of Joy\n"
    "Pain au Chocolat\n"
    "Cadbury Twirl Bites\n",
    "Ham\n\n"
]
emma2 = [
    "Shower Gel - Imperial Leather\n",
    "Cleansing Pads\n",
    "Micellar Water\n",
    "Deodrant\n"
    "Face Wash\n"
    "Face Pads\n"
    "Antiperspirant",
]

test = kelv1 + kelv2 + essentials + emma1 + emma2

breakfast = [
    "Toast\n",
    "Cheese Toastie\n",
    "Omlette\n",
    "Scrambled Egg & Toast\n",
    "Fried Egg & Toast\n",
    "Crossaints\n",
    "Spaghetti & Toast\n",
]
dinner = [
    "Baked Chicken Breast & Rice\n",
    "Beef Steak Burgers & Salad\n",
    "Brown Stew Chicken, Rice & Salad\n",
    "Brown Stew Chicken, Rice, Mac & Cheese\n",
    "Chicken Curry\n",
    "Chicken Enchiladas\n",
    "Chicken Fajitas\n",
    "Chicken Roast\n",
    "Chicken Stir Fry\n",
    "Chicken Wings\n",
    "Chilli Con Carne\n",
    "Fried Chicken & Homemade Oven Chips\n",
    "Homemade Pizza\n",
    "Hot Dogs\n",
    "Pasta Bake\n",
    "Pasta Sauce & Garlic Bread\n",
    "Sausage & Chips\n",
    "Soup & Bread\n",
]
baking = [
    "Vanilla Sponge Cake\n",
    "Vanilla Cupcakes\n",
    "Cinnamon & Almond Sponge Cake\n",
    "Flapjack\n",
]

def window2():
    pop = Toplevel(root)
    pop.title("WOTM - What's On The Menu!")
    pop.geometry("350x150")
    pop.config(bg="#d9d7e3")
    Label(pop, text="Your shopping list has now been generated!\n", bg="#d9d7e3").grid(column=1, row=0, columnspan=2)
    Button(pop, text="OK", height=2, width=18,command=pop.destroy).grid(column=1, row=1, columnspan=2)

def sortdata():

    def remove_duplicates():
        content = open("WOTM_SHOPPING_LIST_" + today + ".txt", "r").readlines()
        content_set = sorted(set(content))
        cleandata = open("WOTM_SHOPPING_LIST_" + today + ".txt", "w")

        for line in content_set:
            cleandata.write(line)

    def sort_data():
        names = list()
        filename = "WOTM_SHOPPING_LIST_" + today + ".txt"

        with open(filename) as fin:
            for line in fin:
                names.append(line.strip())

        names.sort()

        with open(filename, "w") as fout:
            for band in names:
                fout.write(band + "\n")

    def merge_files():
        with open ("WOTM_SHOPPING_LIST_WEEKLY_" + today + ".txt") as fp:
            data1 = fp.read()

        with open ("WOTM_SHOPPING_LIST_" + today + ".txt") as fp:
            data2 = fp.read()

        data = data1 + data2

        data += "\n"

        with open (today + "_shoppinglist.txt", "w") as fp:
            fp.write(data)

    def remove_files():
        os.remove("WOTM_SHOPPING_LIST_" + today + ".txt")
        os.remove("WOTM_SHOPPING_LIST_WEEKLY_" + today + ".txt")

    remove_duplicates()
    sort_data()
    merge_files()
    remove_files()

def shopping_list():
    for i in test:
        file = open("WOTM_SHOPPING_LIST_WEEKLY_" + today + ".txt", "a")
        file.writelines(i)
        file.close()

def menu_breakfast():

    global A2, A1, A3, A4, A5

    # Breakfast Menu

    breakfast = [
        "Toast",
        "Cheese Toastie",
        "Omlette",
        "Scrambled Egg & Toast",
        "Fried Egg & Toast",
        "Crossaints",
        "Spaghetti & Toast",
    ]

    # Breakfast Ingredients

    toast = [
        "Tesco White Bread Loaf",
        "Butter"
    ]
    cheese_toastie = [
        "Tesco White Bread Loaf",
        "Butter",
        "Cheddar Cheese"
    ]
    omlette = [
        "Eggs",
        "Olive Oil",
        "Black Pepper",
        "Mixed Herbs",
        "Salt",
        "Butter",
        "Cheddar Cheese",
        "Ham",
    ]
    scrambled_egg_toast = [
        "Eggs",
        "Olive Oil",
        "Salt",
        "Black Pepper",
        "Mixed Herbs",
        "Tesco White Bread Loaf",
        "Butter",
    ]
    fried_egg_toast = [
        "Eggs",
        "Salt",
        "Tesco White Bread Loaf",
        "Butter",
    ]
    crossaints = [
        "Crossaints",
    ]
    spaghetti_toast = [
        "Tesco White Bread Loaf",
        "Heinz Spaghetti Hoops",
        "Butter"
    ]

    A1 = random.choice(breakfast)
    A2 = random.choice(breakfast)
    A3 = random.choice(breakfast)
    A4 = random.choice(breakfast)
    A5 = random.choice(breakfast)

    if (A1 == "Toast") or (A2 == "Toast") or (A3 == "Toast") or (A4 == "Toast") or (A5 == "Toast"):
        for i in toast:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Cheese Toastie") or (A2 == "Cheese Toastie") or (A3 == "Cheese Toastie") or (A4 == "Cheese Toastie") or (A5 == "Cheese Toastie"):
        for i in cheese_toastie:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Omlette") or (A2 == "Omlette") or (A3 == "Omlette") or (A4 == "Omlette") or (A5 == "Omlette"):
        for i in omlette:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Scrambled Egg & Toast") or (A2 == "Scrambled Egg & Toast") or (A3 == "Scrambled Egg & Toast") or (A4 == "Scrambled Egg & Toast") or (A5 == "Scrambled Egg & Toast"):
        for i in scrambled_egg_toast:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Fried Egg & Toast") or (A2 == "Fried Egg & Toast") or (A3 == "Fried Egg & Toast") or (A4 == "Fried Egg & Toast") or (A5 == "Fried Egg & Toast"):
        for i in fried_egg_toast:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Crossaints") or (A2 == "Crossaints") or (A3 == "Crossaints") or (A4 == "Crossaints") or (A5 == "Crossaints"):
        for i in crossaints:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Spaghetti & Toast") or (A2 == "Spaghetti & Toast") or (A3 == "Spaghetti & Toast") or (A4 == "Spaghetti & Toast") or (A5 == "Spaghetti & Toast"):
        for i in spaghetti_toast:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    file = open(today + "_meals.txt", "a")
    file.write("----- BREAKFAST -----\n\n" + A1 + "\n" + A2 + "\n" + A3 + "\n" + A4 + "\n" + A5 + "\n")
    file.close()

def menu_dinner():

    global A1, A2, A3, A4, A5

    # Dinner Menu

    dinner = [
        "Baked Chicken Breast & Rice",
        "Beef Steak Burgers & Salad",
        "Brown Stew Chicken, Rice & Salad",
        "Brown Stew Chicken, Rice, Mac & Cheese",
        "Chicken Curry",
        "Chicken Enchiladas",
        "Chicken Fajitas",
        "Chicken Roast",
        "Chicken Stir Fry",
        "Chicken Wings",
        "Chilli Con Carne",
        "Fried Chicken & Homemade Oven Chips",
        "Homemade Pizza",
        "Hot Dogs",
        "Pasta Bake",
        "Pasta Sauce & Garlic Bread",
        "Sausage & Chips",
        "Soup & Bread",
    ]

    # Dinner Ingredients

    baked_chicken_breast_rice = [
        "Chicken Breast",
        "Olive Oil",
        "Black Pepper",
        "Smoked Paprika",
        "Garlic Power",
        "Basmatti Rice",
    ]
    beef_stake_burger = [
        "Burgers",
        "Burger Buns",
        "Cheddar Cheese",
        "Iceberg Lettuce",
        "Tomatoes",
        "Red Onions",
    ]
    brown_stew_chicken_rice_salad = [
        "Chicken Breast",
        "Scotch Bonnet",
        "Mixed Bell Peppers",
        "Spring Onions",
        "Red Onions",
        "Olive Oil",
        "All Purpose Seasoning",
        "Paprika",
        "Thyme",
        "Black Pepper",
        "Garlic",
        "Browning",
        "Italian Tomato Puree",
        "Basmatti Rice",
        "Aduki Beans",
        "Cucumber",
        "Tomatoes",
        "Iceberg Lettuce",
    ]
    brown_stew_chicken_rice_mac_cheese = [
        "Chicken Breast",
        "Scotch Bonnet",
        "Mixed Bell Peppers",
        "Spring Onions",
        "Red Onions",
        "Olive Oil",
        "All Purpose Seasoning",
        "Paprika",
        "Thyme",
        "Black Pepper",
        "Garlic",
        "Browning",
        "Italian Tomato Puree",
        "Basmatti Rice",
        "Aduki Beans",
        "Pasta (Fusilli)",
        "Cheddar Cheese",
        "Macaroni Cheese Sauce",
        "Red Bell Peppers",
        "Olive Oil",
        "Salt",
    ]
    chicken_curry = [
        "Chicken Fillet (Large)",
        "Black Pepper",
        "Salt",
        "Chicken Tikka Sauce",
        "Basmatti Rice",
        "Olive Oil",
        "Naan Bread",
    ]
    chicken_enchiladas = [
        "Chicken Fillet (Large)",
        "Cheesy Baked Enchilada Dinner Kit",
        "Cheddar Cheese",
    ]
    chicken_fajitas = [
        "Chicken Fillet (Large)",
        "Crispy Chicken Fajita Seasoning Mix",
        "Wrap",
        "Mild Salsa",
        "Iceberg Lettuce",
        "Red Bell Peppers",
    ]
    chicken_roast = [
        "Baked Chicken Breast",
        "Roast Potatoes",
        "Potatoes",
        "Ground Black Pepper",
        "Olive Oil",
        "Pig in Blankets",
        "Sage & Onion Stuffing Mix",
        "Yorkshire Pudding",
        "Bisto Gravy Onion",
                     ]
    chicken_stir_fry = [
        "Chicken Fillet (Small)",
        "Mixed Bell Peppers",
        "Red Onions",
        "Bean Sprouts",
        "Spring Onions",
        "Olive Oil",
        "Noodles",
        "Blue Dragon Chow Mein Sauce",
        "Salt",
        "Pepper",
        "Garlic",
    ]
    chicken_wings = [
        "Chicken Wings",
        "Levi Roots Reggae Jerk BBQ Sauce",
        "Spring Onions",
        "Red Bell Peppers",
        "Toasted Sesame Seeds",
        "Olive Oil",
    ]
    chilli_con_carne = [
        "Beef Mince",
        "Olive Oil",
        "Chopped Tomatoes",
        "Red Onions",
        "Red Bell Peppers",
        "Green Bell Peppers",
        "Cumin Seeds",
        "Chilli Flakes",
        "Ground Black Pepper",
        "Mixed Herbs",
        "Salt",
    ]
    fried_chicken_homemade_oven_chips = [
        "Chicken Fillet (Small)",
        "Eggs",
        "Breadcrumb Seasoning",
        "Olive Oil",
        "Potato",
        "Ground Black Pepper",
        "Salt",
        "Sage",
        "Olive Oil",
    ]
    homemade_pizza = [
        "Plain Flour",
        "Salt",
        "Sugar",
        "Olive Oil",
    ]
    hotdogs = [
        "Hot Dogs",
        "Buns",
        "Butter",
    ]
    pasta_bake = [
        "Pasta (Fusilli)",
        "Cheddar Cheese",
        "Pasta Bake Sauce",
        "Olive Oil",
        "Salt",
    ]
    pasta_sauce_garlic_bread = [
        "Pasta (Fusilli)",
        "Pasta Sauce",
        "Salt",
        "Olive Oil",
        "Garlic Bread",
    ]
    sausage_chips = [
        "Richmond Sausages",
        "Chips",
        "Olive Oil",
        "Black Pepper",
        "Sage",
    ]
    soup_bread = [
        "Tomato Soup",
        "French Stick Bread",
        "Butter",
    ]

    A1 = random.choice(dinner)
    A2 = random.choice(dinner)
    A3 = random.choice(dinner)
    A4 = random.choice(dinner)
    A5 = random.choice(dinner)

    if (A1 == "Baked Chicken Breast & Rice") or (A2 == "Baked Chicken Breast & Rice") or (A3 == "Baked Chicken Breast & Rice") or (A4 == "Baked Chicken Breast & Rice") or (A5 == "Baked Chicken Breast & Rice"):
        for i in baked_chicken_breast_rice:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Beef Steak Burgers & Salad") or (A2 == "Beef Steak Burgers & Salad") or (A3 == "Beef Steak Burgers & Salad") or (A4 == "Beef Steak Burgers & Salad") or (A5 == "Beef Steak Burgers & Salad"):
        for i in beef_stake_burger:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Brown Stew Chicken, Rice & Salad") or (A2 == "Brown Stew Chicken, Rice & Salad") or (A3 == "Brown Stew Chicken, Rice & Salad") or (A4 == "Brown Stew Chicken, Rice & Salad") or (A5 == "Brown Stew Chicken, Rice & Salad"):
        for i in brown_stew_chicken_rice_salad:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Brown Stew Chicken, Rice, Mac & Cheese") or (A2 == "Brown Stew Chicken, Rice, Mac & Cheese") or (A3 == "Brown Stew Chicken, Rice, Mac & Cheese") or (A4 == "Brown Stew Chicken, Rice, Mac & Cheese") or (A5 == "Brown Stew Chicken, Rice, Mac & Cheese"):
        for i in brown_stew_chicken_rice_mac_cheese:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Chicken Curry") or (A2 == "Chicken Curry") or (A3 == "Chicken Curry") or (A4 == "Chicken Curry") or (A5 == "Chicken Curry"):
        for i in chicken_curry:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Chicken Enchiladas") or (A2 == "Chicken Enchiladas") or (A3 == "Chicken Enchiladas") or (A4 == "Chicken Enchiladas") or (A5 == "Chicken Enchiladas"):
        for i in chicken_enchiladas:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Chicken Fajitas") or (A2 == "Chicken Fajitas") or (A3 == "Chicken Fajitas") or (A4 == "Chicken Fajitas") or (A5 == "Chicken Fajitas"):
        for i in chicken_fajitas:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Chicken Roast") or (A2 == "Chicken Roast") or (A3 == "Chicken Roast") or (A4 == "Chicken Roast") or (A5 == "Chicken Roast"):
        for i in chicken_roast:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Chicken Stir Fry") or (A2 == "Chicken Stir Fry") or (A3 == "Chicken Stir Fry") or (A4 == "Chicken Stir Fry") or (A5 == "Chicken Stir Fry"):
        for i in chicken_stir_fry:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Chicken Wings") or (A2 == "Chicken Wings") or (A3 == "Chicken Wings") or (A4 == "Chicken Wings")or (A5 == "Chicken Wings"):
        for i in chicken_wings:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Chilli Con Carne") or (A2 == "Chilli Con Carne") or (A3 == "Chilli Con Carne") or (A4 == "Chilli Con Carne") or (A5 == "Chilli Con Carne"):
        for i in chilli_con_carne:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Fried Chicken & Homemade Oven Chips") or (A2 == "Fried Chicken & Homemade Oven Chips") or (A3 == "Fried Chicken & Homemade Oven Chips") or (A4 == "Fried Chicken & Homemade Oven Chips") or (A5 == "Fried Chicken & Homemade Oven Chips"):
        for i in fried_chicken_homemade_oven_chips:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Homemade Pizza") or (A2 == "Homemade Pizza") or (A3 == "Homemade Pizza") or (A4 == "Homemade Pizza") or (A5 == "Homemade Pizza"):
        for i in homemade_pizza:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Hot Dogs") or (A2 == "Hot Dogs") or (A3 == "Hot Dogs") or (A4 == "Hot Dogs") or (A5 == "Hot Dogs"):
        for i in hotdogs:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Pasta Bake") or (A2 == "Pasta Bake") or (A3 == "Pasta Bake") or (A4 == "Pasta Bake") or (A5 == "Pasta Bake"):
        for i in pasta_bake:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Pasta Sauce & Garlic Bread") or (A2 == "Pasta Sauce & Garlic Bread") or (A3 == "Pasta Sauce & Garlic Bread") or (A4 == "Pasta Sauce & Garlic Bread") or (A5 == "Pasta Sauce & Garlic Bread"):
        for i in pasta_sauce_garlic_bread:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Sausage & Chips") or (A2 == "Sausage & Chips") or (A3 == "Sausage & Chips") or (A4 == "Sausage & Chips") or (A5 == "Sausage & Chips"):
        for i in sausage_chips:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Soup & Bread") or (A2 == "Soup & Bread") or (A3 == "Soup & Bread") or (A4 == "Soup & Bread"):
        for i in soup_bread:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    file = open(today + "_meals.txt", "a")
    file.write("\n----- DINNER -----\n\n" + A1 + "\n" + A2 + "\n" + A3 + "\n" + A4 + "\n" + A5 + "\n")
    file.close()




def SMTP():
    outlook = win32.Dispatch("outlook.application")
    mail = outlook.CreateItem(0)
    mail.To = "kelvingooding@msn.com"
    #attachment = (file1)
    #mail.Attachments.Add(attachment)
    mail.Subject = "WOTM - What's On The Menu! " + today
    mail.Body = "Hi," \
                "\n\nPlease ignore this mail." \
                "\n\nThis is a reply to the original message." \
                "\n\nKind Regards" \
                "\nKelv Gooding" + str(shopping_list)
    mail.Send()

def BTN1():
    textbox.configure(state="normal")
    textbox.delete("1.0", END)
    for i in test:
        textbox.insert(END,(i))
    textbox.configure(state="disabled")

def BTN2():
    textbox.configure(state="normal")
    textbox.delete("1.0", END)
    breakfast.sort()
    for i in breakfast:
        textbox.insert(END, (i))
    textbox.configure(state="disabled")

def BTN3():
    textbox.configure(state="normal")
    textbox.delete("1.0", END)
    dinner.sort()
    for i in dinner:
        textbox.insert(END, (i))
    textbox.configure(state="disabled")

def BTN4():
    textbox.configure(state="normal")
    textbox.delete("1.0", END)
    baking.sort()
    for i in baking:
        textbox.insert(END, (i))
    textbox.configure(state="disabled")

def BTN5():
    shopping_list()
    menu_breakfast()
    menu_dinner()
    sortdata()
    #SMTP()
    window2()

btn1 = Button(
    text="View Shopping List",
    command=BTN1,
    height=2,
    width=18).grid(
    column=0,
    row=0,
    padx=50,
    pady=10)

sep1 = ttk.Separator().place(x=90, y=80, relwidth=0.1)

btn2 = Button(
    text="View Breakfast Menu",
    command=BTN2,
    height=2,
    width=18).grid(
    column=0,
    row=1,
    padx=50,
    pady=10)

btn3 = Button(
    text="View Dinner Menu",
    command=BTN3,
    height=2,
    width=18).grid(
    column=0,
    row=2,
    padx=50,
    pady=10)

btn4 = Button(
    text="View Baking Menu",
    command=BTN4,
    height=2,
    width=18).grid(
    column=0,
    row=3,
    padx=50,
    pady=10)

sep2 = ttk.Separator().place(x=90, y=321, relwidth=0.1)

btn5 = Button(
    text="Generate Shopping List",
    command=BTN5,
    height=2,
    width=18).grid(
    column=0,
    row=4,
    padx=50,
    pady=10)

sep3 = ttk.Separator().place(x=90, y=405, relwidth=0.1)

btn6 = Button(
    text="Exit",
    height=2,
    width=18,
    command=sys.exit).grid(
    column=0,
    row=5,
    padx=50,
    pady=10)

label1 = Label(text = "", bg="#d9d7e3").grid(column=0, row=6, columnspan=2,)
label2 = Label(text = "Created by Kelv Gooding\n© 2021 Copyright. All rights reserved.\n" + " Version " + verno, bg="#d9d7e3").grid(column=0, row=7, columnspan=2,)

frame = Frame(root,bg='#A8B9BF')

textbox = Text(root, height=30, width=40)
textbox.configure(font=("Arial", 10,), state="disabled")
textbox.grid(row=0, column=1, rowspan=6)
textbox.config(bg='#FFFFFF')

scrollbar = Scrollbar(root, orient=VERTICAL)
scrollbar.grid(row=0, column=2, rowspan=6, sticky=NS,)

textbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=textbox.yview)

root.mainloop()






































