# Modules

import datetime
import time
import sys
import os
import random

# Variables

clear = lambda: os.system("cls")
today = datetime.datetime.today().strftime("%d_%m_%Y")

# Script Info

def script_info():
    created_date = "Creation Date:    Mon 30/08/2021"
    dateformat1 = datetime.datetime.today().strftime("Today Date:       %a %d/%m/%Y")
    verno = (str(1.6))

    print("--- Script Information ---\n")
    print("Script Creator:   Kelv Gooding")
    print(created_date)
    print(dateformat1)
    print("Version:          " + verno)
    print("\n--- Starting Script ---")

# Merge / Clean / Sort

def sortdata():
    # Clean Data - Working

    def remove_duplicates():
        content = open("WOTM_SHOPPING_LIST_" + today + ".txt", "r").readlines()
        content_set = sorted(set(content))
        cleandata = open("WOTM_SHOPPING_LIST_" + today + ".txt", "w")

        for line in content_set:
            cleandata.write(line)
    remove_duplicates()

    # Sort Data - This is not working

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
    sort_data()

    def merge_files():
        with open ("WOTM_SHOPPING_LIST_KELV_" + today + ".txt") as fp:
            data1 = fp.read()

        with open ("WOTM_SHOPPING_LIST_" + today + ".txt") as fp:
            data2 = fp.read()

        with open ("WOTM_SHOPPING_LIST_EM_" + today + ".txt") as fp:
            data3 = fp.read()

        with open ("WOTM_SHOPPING_LIST_ESSENTIALS_" + today + ".txt") as fp:
            data4 = fp.read()

        with open ("WOTM_SHOPPING_LIST_TOILETRIES_" + today + ".txt") as fp:
            data5 = fp.read()

        data = data1 + data2 + data3 + data4 + data5

        data += "\n"

        with open ("testfile.txt", "w") as fp:
            fp.write(data)
    merge_files()

# Main Menu

def main_menu():

    choice1 ='0'
    while choice1 =='0':
        print("--- WHATS ON THE MENU ---\n")
        print("1. Food / Essentials List")
        print("2. Breakfast")
        print("3. Dinner")
        print("4. Baking")
        print("5. Generate")
        print("6. Exit")
        print("\n--------------------------")

        choice1 = input("\nPlease enter a number: ")

        if choice1 == "1":
            clear()
            view_shopping_list()
        elif choice1 == "2":
            clear()
            view_breakfast_menu()
        elif choice1 == "3":
            clear()
            view_dinner_menu()
        elif choice1 == "4":
            clear()
            view_baking_menu()
        elif choice1 == "5":
            try:
                menu_shopping_list()
                menu_breakfast()
                menu_dinner()
                menu_baking()
                clear()
                sortdata()
                print("Shopping list and Meals have been exported!")

                Q1 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

                if (Q1 == "Y") or (Q1 == "y"):
                    clear()
                    main_menu()
                elif (Q1 == "N") or (Q1 == "n"):
                    print("\nThank you for using WOTM!")
                    sys.exit(0)
                else:
                    print("\nInvalid option. Please try again.")
                    time.sleep(3)
                    view_shopping_list()
            except FileNotFoundError:
                print("\nThank you for using WOTM!")
                sys.exit(0)
        elif choice1 == "6":
            print("\nThank you for using WOTM!")
            sys.exit(0)
        else:
            clear()
            print("Invalid option. Please try again.\n")
            main_menu()

# View Shopping List / Meals

def view_shopping_list():
    kelv = [
        "Tesco White Bread Loaf",
        "Drink - Orange Juice",
        "Drink - Apple Juice",
        "Drink - Tropical Carton",
        "Drink - Blackcurrent Squash",
        "Mixed Bell Peppers",
        "Tomatoes",
        "Spring Onions",
        "Red Apples",
        "Cheddar Cheese",
        "Skinny Chips",
        "Steak Chips",
        "Maggi Noodles - Chicken",
        "Tomato Soup",
        "Butter",
        "Chicago Town Pizza - Margarita"
    ]
    emma = [
        "Brioche",
        "New York Bakery Plain Bagel",
        "Mozzarella Sticks",
        "Drink - Lemon Squash",
        "Drink - Pepsi",
        "Drink - Fanta Orange",
        "Drink - Lilt",
        "Drink - Sprite",
        "Drink - Apple & Mango Juice",
        "Drink - Breakfast Juice",
        "Magic Stars Chocolate",
        "White Chocolate Bar",
        "Haribo Starmix",
        "Skittles",
        "Flake Ice Cream",
        "Yoghurt - Dairy Milk Ports of Joy",
        "Shower Gel - Imperial Leather",
        "Cleansing Pads",
        "Micellar Water",
        "Ham",
    ]
    essentials = [
        "Toilet Roll",
        "Kitchen Roll",
        "Handwash",
        "Black Bin Bags",
        "Small Bin Bags",
        "Washing Up Liquid",
        "Washing Capsules - Lavender",
        "Washing Gems - Lavender",
        "Foil",
        "Clingfilm",
        "Baking Paper",
        "Antibacterial Spray",
        "Bathroom Cleaner",
        "Toilet Gel",
        "Viakal",
        "Polish",
        "Glass Cleaner",
        "Oven Cleaner",
        "Drain Unblocker",
        "Flash Mop Wipes",
        "Disinfectant",
        "Bleach",
    ]
    toiletries = [
        "Shower Gel",
        "Deodorant",
        "Antiperspirant",
        "Lotion - Cocoa Butter",
        "Shampoo",
    ]

    print("----- Kelv -----\n")
    kelv.sort()
    for i in kelv:
        print(i)

    print("\n----- Em -----\n")
    emma.sort()
    for i in emma:
        print(i)

    print("\n----- Essentials -----\n")
    essentials.sort()
    for i in essentials:
        print(i)

    print("\n----- Toiletries -----\n")
    toiletries.sort()
    for i in toiletries:
        print(i)

    Q1 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

    if (Q1 == "Y") or (Q1 == "y"):
        clear()
        main_menu()
    elif (Q1 == "N") or (Q1 == "n"):
        print("\nThank you for using WOTM!")
        sys.exit(0)
    else:
        print("\nInvalid option. Please try again.")
        time.sleep(3)
        view_shopping_list()

def view_breakfast_menu():
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

    breakfast.sort()
    for i in breakfast:
        print(i)

    Q1 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

    if (Q1 == "Y") or (Q1 == "y"):
        clear()
        main_menu()
    elif (Q1 == "N") or (Q1 == "n"):
        print("\nThank you for using WOTM!")
        sys.exit(0)
    else:
        print("\nInvalid option. Please try again.")
        time.sleep(3)
        view_breakfast_menu()

def view_dinner_menu():
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

    dinner.sort()
    for i in dinner:
        print(i)

    Q1 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

    if (Q1 == "Y") or (Q1 == "y"):
        clear()
        main_menu()
    elif (Q1 == "N") or (Q1 == "n"):
        print("\nThank you for using WOTM!")
        sys.exit(0)
    else:
        print("\nInvalid option. Please try again.")
        time.sleep(3)
        view_dinner_menu()

def view_baking_menu():
    # Baking Menu

    baking = [
        "Vanilla Sponge Cake",
        "Vanilla Cupcakes",
        "Cinnamon & Almond Sponge Cake",
        "Flapjack",
    ]

    baking.sort()
    for i in baking:
        print(i)

    Q1 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

    if (Q1 == "Y") or (Q1 == "y"):
        clear()
        main_menu()
    elif (Q1 == "N") or (Q1 == "n"):
        print("\nThank you for using WOTM!")
        sys.exit(0)
    else:
        print("\nInvalid option. Please try again.")
        time.sleep(3)
        view_baking_menu()

# Generate Shopping List / Meals

def menu_shopping_list():

    kelv = [
        "Tesco White Bread Loaf",
        "Drink - Orange Juice",
        "Drink - Apple Juice",
        "Drink - Tropical Carton",
        "Drink - Blackcurrent Squash",
        "Mixed Bell Peppers",
        "Tomatoes",
        "Spring Onions",
        "Red Apples",
        "Cheddar Cheese",
        "Skinny Chips",
        "Steak Chips",
        "Maggi Noodles - Chicken",
        "Tomato Soup",
        "Butter",
        "Chicago Town Pizza - Margarita"
    ]
    emma = [
        "Brioche",
        "New York Bakery Plain Bagel",
        "Mozzarella Sticks",
        "Drink - Lemon Squash",
        "Drink - Pepsi",
        "Drink - Fanta Orange",
        "Drink - Lilt",
        "Drink - Sprite",
        "Drink - Apple & Mango Juice",
        "Drink - Breakfast Juice",
        "Magic Stars Chocolate",
        "White Chocolate Bar",
        "Haribo Starmix",
        "Skittles",
        "Flake Ice Cream",
        "Yoghurt - Dairy Milk Ports of Joy",
        "Shower Gel - Imperial Leather",
        "Cleansing Pads",
        "Micellar Water",
        "Ham",
        ]
    essentials = [
        "Toilet Roll",
        "Kitchen Roll",
        "Handwash",
        "Black Bin Bags",
        "Small Bin Bags",
        "Washing Up Liquid",
        "Washing Capsules - Lavender",
        "Washing Gems - Lavender",
        "Foil",
        "Clingfilm",
        "Baking Paper",
        "Antibacterial Spray",
        "Bathroom Cleaner",
        "Toilet Gel",
        "Viakal",
        "Polish",
        "Glass Cleaner",
        "Oven Cleaner",
        "Drain Unblocker",
        "Flash Mop Wipes",
        "Disinfectant",
        "Bleach",
    ]
    toiletries = [
        "Shower Gel",
        "Deodorant",
        "Antiperspirant",
        "Lotion - Cocoa Butter",
        "Shampoo",
    ]

    kelv.sort()
    for i in kelv:
        file = open("WOTM_SHOPPING_LIST_KELV_" + today + ".txt", "a")
        file.writelines(i + "\n")
        file.close()

    emma.sort()
    for i in emma:
        file = open("WOTM_SHOPPING_LIST_EM_" + today + ".txt", "a")
        file.writelines(i + "\n")
        file.close()

    essentials.sort()
    for i in essentials:
        file = open("WOTM_SHOPPING_LIST_ESSENTIALS_" + today + ".txt", "a")
        file.writelines(i + "\n")
        file.close()

    toiletries.sort()
    for i in toiletries:
        file = open("WOTM_SHOPPING_LIST_TOILETRIES_" + today + ".txt", "a")
        file.writelines(i + "\n")
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

    file = open("WOTM_MEALS_" + today + ".txt", "a")
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
        "Lettuce",
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
        "Spring Onions",
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
        "Chicken Fillets",
        "Black Pepper",
        "Salt",
        "Chicken Tikka Sauce",
        "Basmatti Rice",
        "Olive Oil",
        "Naan Bread",
    ]
    chicken_enchiladas = [
        "Chicken Fillets",
        "Cheesy Baked Enchilada Dinner Kit",
        "Cheddar Cheese",
    ]
    chicken_fajitas = [
        "Chicken Fillets",
        "Crispy Chicken Fajita Seasoning Mix",
        "Wrap",
        "Mild Salsa",
        "Lettuce",
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
        "Chicken Fillets",
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
        "Chicken Fillets",
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

    file = open("WOTM_MEALS_" + today + ".txt", "a")
    file.write("\n----- DINNER -----\n\n" + A1 + "\n" + A2 + "\n" + A3 + "\n" + A4 + "\n" + A5 + "\n")
    file.close()

def menu_baking():

    # Baking Menu

    baking = [
        "Vanilla Sponge Cake",
        "Vanilla Cupcakes",
        "Cinnamon & Almond Sponge Cake",
        "Flapjack",
    ]

    # Baking Ingredients

    cinnamon_almond_sponge_cake = [
        "Butter",
        "Caster Sugar",
        "Self-Rising Flour",
        "Eggs",
        "Almond Essence",
        "Cinnamon Essence",
    ]
    flapjack = [
        "Oats",
        "Granulated Sugar",
        "Butter",
        "Golden Syrup",
    ]
    vanilla_cupcakes = [
        "Butter",
        "Caster Sugar",
        "Self-Rising Flour",
        "Eggs",
        "Vanilla Essence",
    ]
    vanilla_sponge_cake = [
        "Butter",
        "Caster Sugar",
        "Self-Rising Flour",
        "Eggs",
        "Vanilla Essence",
    ]

    A1 = random.choice(baking)
    A2 = random.choice(baking)

    if (A1 == "Cinnamon & Almond Sponge Cake") or (A2 == "Cinnamon & Almond Sponge Cake"):
        for i in cinnamon_almond_sponge_cake:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Flapjack") or (A2 == "Flapjack"):
        for i in flapjack:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Vanilla Cupcakes") or (A2 == "Vanilla Cupcakes"):
        for i in vanilla_cupcakes:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    if (A1 == "Vanilla Sponge Cake") or (A2 == "Vanilla Sponge Cake"):
        for i in vanilla_sponge_cake:
            file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
            file.write(i + "\n")
            file.close()

    file = open("WOTM_MEALS_" + today + ".txt", "a")
    file.write("\n----- BAKING -----\n\n" + A1 + "\n" + A2 + "\n")
    file.close()

main_menu()