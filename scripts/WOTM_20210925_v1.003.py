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
    verno = (str(1.3))

    print("--- Script Information ---\n")
    print("Script Creator:   Kelv Gooding")
    print(created_date)
    print(dateformat1)
    print("Version:          " + verno)
    print("\n--- Starting Script ---")

# Main Menu

def main_menu():

    choice1 ='0'
    while choice1 =='0':
        print("--- WHATS ON THE MENU ---\n")
        print("1. Food / Essentials List")
        print("2. Breakfast")
        print("3. Dinner")
        print("4. Baking")
        print("5. Exit")
        print("\n--------------------------")

        choice1 = input("\nSelect a number: ")

        if choice1 == "1":
            clear()
            menu_food_essentials()
        elif choice1 == "2":
            clear()
            menu_breakfast()
        elif choice1 == "3":
            clear()
            menu_dinner()
        elif choice1 == "4":
            clear()
            menu_baking()
        elif choice1 == "5":
            print("\nClosing Application..")
            sys.exit(0)
        else:
            clear()
            print("Invalid option. Please try again.\n")
            main_menu()

# Food / Meals

def menu_food_essentials():

    # Shopping List

    kelv_food = [
        "Tesco White Bread Loaf",
        "Chicken Breast / Fillet",
        "Orange Juice / Apple Juice",
        "Carton Juice - Tropical",
        "Squash - Blackcurrent",
        "Bell Peppers",
        "Tomatoes",
        "Spring Onions",
        "Red Apples",
        "Cheddar Cheese (Mild)",
        "Skinny Chips",
        "Steak Chips",
        "Maggi Noodles",
        "Tomato Soup",
        "Butter",
    ]
    emma_food = [
        "Brioche",
        "New York Bakery Plain Bagel",
        "Mozzarella Sticks",
        "Squash - Lemon",
        "Pepsi",
        "Fanta Orange",
        "Lilt",
        "Sprite",
        "Apple & Mango Juice",
        "Breakfast Juice",
        "Chocolate - Magic Stars",
        "White Chocolate Bar",
        "Sweets - Haribo Starmix",
        "Sweets - Skittles",
        "Flake Ice Cream",
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

    print("----- Food / Essential Shopping List -----")

    print("\n----- Kelv Food -----\n")

    for i in kelv_food:
        print(i)
        file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
        file.writelines(i + "\n")
        file.close()

    print("\n----- Emma Food -----\n")

    for i in emma_food:
        print(i)
        file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
        file.writelines(i + "\n")
        file.close()

    print("\n----- Essentials -----\n")

    for i in essentials:
        print(i)
        file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
        file.writelines(i + "\n")
        file.close()

    Q1 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

    if (Q1 == "Y") or (Q1 == "y"):
        clear()
        main_menu()
    elif (Q1 == "N") or (Q1 == "n"):
        print("\nClosing application..")
        sys.exit(0)
    else:
        print("\nInvalid option. Please try again.")
        time.sleep(3)
        menu_food_essentials()

def menu_breakfast():

    global A2, A1, A3, A4, A5
    global M1, M2, M3, M4, M5

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
        "Cheddar Cheese - Mild"
    ]
    omlette = [
        "Eggs",
        "Olive Oil",
        "Black Pepper",
        "Mixed Herbs",
        "Salt",
        "Butter",
        "Cheddar Cheese"
        "Ham",
    ]
    scrambled_egg_toast = [
        "Egg",
        "Olive Oil",
        "Salt",
        "Black Pepper",
        "Mixed Herbs",
        "Tesco White Bread Loaf",
        "Butter",
    ]
    fried_egg_toast = [
        "Egg",
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

    print("----- Breakfast Menu -----\n")

    for i in breakfast:
        print(i)

    Q1 = input("\nWould you like to continue? (Enter Y or N): ")

    if (Q1 == "Y") or (Q1 == "y"):
        Q2 = input("\nAuto selection or Manual selection? (Enter A or M): ")
        if (Q2 == "A") or (Q2 == "a"):
            clear()
            print("--- Meals and Ingredients ---")
            A1 = random.choice(breakfast)
            A2 = random.choice(breakfast)
            A3 = random.choice(breakfast)
            A4 = random.choice(breakfast)
            A5 = random.choice(breakfast)

            if (A1 == "Toast") or (A2 == "Toast") or (A3 == "Toast") or (A4 == "Toast") or (A5 == "Toast"):
                print("\nToast Ingredients:\n")
                for i in toast:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Cheese Toastie") or (A2 == "Cheese Toastie") or (A3 == "Cheese Toastie") or (A4 == "Cheese Toastie") or (A5 == "Cheese Toastie"):
                print("\nCheese Toastie Ingredients:\n")
                for i in cheese_toastie:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Omlette") or (A2 == "Omlette") or (A3 == "Omlette") or (A4 == "Omlette") or (A5 == "Omlette"):
                print("\nOmlette Ingredients:\n")
                for i in omlette:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Scrambled Egg & Toast") or (A2 == "Scrambled Egg & Toast") or (A3 == "Scrambled Egg & Toast") or (A4 == "Scrambled Egg & Toast") or (A5 == "Scrambled Egg & Toast"):
                print("\nScrambled Egg & Toast Ingredients:\n")
                for i in scrambled_egg_toast:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Fried Egg & Toast") or (A2 == "Fried Egg & Toast") or (A3 == "Fried Egg & Toast") or (A4 == "Fried Egg & Toast") or (A5 == "Fried Egg & Toast"):
                print("\nFried Egg & Toast Ingredients:\n")
                for i in fried_egg_toast:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Crossaints") or (A2 == "Crossaints") or (A3 == "Crossaints") or (A4 == "Crossaints") or (A5 == "Crossaints"):
                print("\nCrossaints Ingredients:\n")
                for i in crossaints:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Spaghetti & Toast") or (A2 == "Spaghetti & Toast") or (A3 == "Spaghetti & Toast") or (A4 == "Spaghetti & Toast") or (A5 == "Spaghetti & Toast"):
                print("\nSpaghetti & Toast Ingredients:\n")
                for i in spaghetti_toast:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            print("\n----- Breakfast Menu for this week -----\n")
            print(A1)
            print(A2)
            print(A3)
            print(A4)
            print(A5)

            file = open("WOTM_MEALS_" + today + ".txt", "a")
            file.write("----- Breakfast Menu for this week -----\n\n" + A1 + "\n" + A2 + "\n" + A3 + "\n" + A4 + "\n" + A5 + "\n")
            file.close()

            Q3 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

            if (Q3 == "Y") or (Q3 == "y"):
                clear()
                main_menu()
            elif (Q3 == "N") or (Q3 == "n"):
                print("\nClosing application..")
                sys.exit(0)
            else:
                print("\nInvalid option. Please try again.")
                time.sleep(3)
                menu_breakfast()
        elif (Q2 == "M") or (Q2 == "m"):
            print("\nBreakfast Menu (Choose 5 from this menu):")

            M1 = input("\nEnter Meal 1: ")
            M2 = input("Enter Meal 2: ")
            M3 = input("Enter Meal 3: ")
            M4 = input("Enter Meal 4: ")
            M5 = input("Enter Meal 5: ")

            if (M1 == "Toast") or (M2 == "Toast") or (M3 == "Toast") or (M4 == "Toast") or (M5 == "Toast"):
                print("\nToast Ingredients:\n")
                for i in toast:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (M1 == "Cheese Toastie") or (M2 == "Cheese Toastie") or (M3 == "Cheese Toastie") or (M4 == "Cheese Toastie") or (M5 == "Cheese Toastie"):
                print("\nCheese Toastie Ingredients:\n")
                for i in cheese_toastie:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (M1 == "Omlette") or (M2 == "Omlette") or (M3 == "Omlette") or (M4 == "Omlette") or (M5 == "Omlette"):
                print("\nOmlette Ingredients:\n")
                for i in omlette:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (M1 == "Scrambled Egg & Toast") or (M2 == "Scrambled Egg & Toast") or (M3 == "Scrambled Egg & Toast") or (M4 == "Scrambled Egg & Toast") or (M5 == "Scrambled Egg & Toast"):
                print("\nScrambled Egg & Toast Ingredients:\n")
                for i in scrambled_egg_toast:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (M1 == "Fried Egg & Toast") or (M2 == "Fried Egg & Toast") or (M3 == "Fried Egg & Toast") or (M4 == "Fried Egg & Toast") or (M5 == "Fried Egg & Toast"):
                print("\nFried Egg & Toast Ingredients:\n")
                for i in fried_egg_toast:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (M1 == "Crossaints") or (M2 == "Crossaints") or (M3 == "Crossaints") or (M4 == "Crossaints") or (M5 == "Crossaints"):
                print("\nCrossaints Ingredients:\n")
                for i in crossaints:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (M1 == "Spaghetti & Toast") or (M2 == "Spaghetti & Toast") or (M3 == "Spaghetti & Toast") or (M4 == "Spaghetti & Toast") or (M5 == "Spaghetti & Toast"):
                print("\nSpaghetti & Toast Ingredients:\n")
                for i in spaghetti_toast:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            print("\n----- Breakfast Menu for this week -----\n")
            print(M1)
            print(M2)
            print(M3)
            print(M4)
            print(M5)

            file = open("WOTM_MEALS_" + today + ".txt", "a")
            file.write("----- Breakfast Menu for this week -----\n\n" + M1 + "\n" + M2 + "\n" + M3 + "\n" + M4 + "\n" + M5 + "\n")
            file.close()

            Q4 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

            if (Q4 == "Y") or (Q4 == "y"):
                clear()
                main_menu()
            elif (Q4 == "N") or (Q4 == "n"):
                print("\nClosing application..")
                sys.exit(0)
            else:
                print("\nInvalid option. Please try again.")
                time.sleep(3)
                menu_breakfast()

        else:
            print("Invalid Option. Please try again.")
            menu_breakfast()
    elif (Q1 == "N") or (Q1 == "n"):
        clear()
        main_menu()
    else:
        print("Invalid option. Please try again.")
        menu_breakfast()

def menu_dinner():

    global M1, M2, M3, M4, M5

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
        "Cheddar Cheese"
        "Lettuce",
        "Tomatoes",
        "Red Onions",
    ]
    brown_stew_chicken_rice_salad = [
        "Chicken Breast",
        "Scotch Bonnet",
        "Bell Peppers",
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
        "Bell Peppers",
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
        "Red Bell Pepper",
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
        "Red Bell Pepper",
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
        "Bell Pepper",
        "Red Onion",
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
        "Red Pepper",
        "Toasted Sesame Seeds",
        "Olive Oil",
    ]
    chilli_con_carne = [
        "Beef Mince",
        "Olive Oil",
        "Chopped Tomatoes",
        "Red Onions",
        "Red Peppers",
        "Green Peppers",
        "Cumin Seeds",
        "Chilli Flakes",
        "Ground Black Pepper",
        "Mixed Herbs",
        "Salt",
    ]
    fried_chicken_homemade_oven_chips = [
        "Chicken Fillets",
        "Egg",
        "Breadcrumb Seasoning",
        "Olive Oil",
        "Potato",
        "Ground Pepper",
        "Salt",
        "Sage",
        "Olive Oil",
    ]
    homemade_oven_chips = [
        "Potato",
        "Ground Pepper",
        "Salt",
        "Sage",
        "Olive Oil",
    ]
    homemade_pizza = [
        "Plain Flour",
        "Salt",
        "Sugar",
        "Olive Oil",
        "Water",
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

    print("----- Dinner Menu: -----\n")

    for i in dinner:
        print(i)

    Q1 = input("\nWould you like to continue? (Enter Y or N): ")

    if (Q1 == "Y") or (Q1 == "y"):
        Q2 = input("\nAuto selection or Manual selection? (Enter A or M): ")
        if (Q2 == "A") or (Q2 == "a"):
            clear()

            print("--- Meals and Ingredients ---")
            A1 = random.choice(dinner)
            A2 = random.choice(dinner)
            A3 = random.choice(dinner)
            A4 = random.choice(dinner)
            A5 = random.choice(dinner)

            if (A1 == "Baked Chicken Breast & Rice") or (A2 == "Baked Chicken Breast & Rice") or (A3 == "Baked Chicken Breast & Rice") or (A4 == "Baked Chicken Breast & Rice") or (A5 == "Baked Chicken Breast & Rice"):
                print("\nBaked Chicken Breast & Rice Ingredients:\n")
                for i in baked_chicken_breast_rice:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Beef Steak Burgers & Salad") or (A2 == "Beef Steak Burgers & Salad") or (A3 == "Beef Steak Burgers & Salad") or (A4 == "Beef Steak Burgers & Salad") or (A5 == "Beef Steak Burgers & Salad"):
                print("\nBeef Steak Burgers & Salad Ingredients:\n")
                for i in beef_stake_burger:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Brown Stew Chicken, Rice & Salad") or (A2 == "Brown Stew Chicken, Rice & Salad") or (A3 == "Brown Stew Chicken, Rice & Salad") or (A4 == "Brown Stew Chicken, Rice & Salad") or (A5 == "Brown Stew Chicken, Rice & Salad"):
                print("\nBrown Stew Chicken, Rice & Salad Ingredients:\n")
                for i in brown_stew_chicken_rice_salad:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Brown Stew Chicken, Rice, Mac & Cheese") or (A2 == "Brown Stew Chicken, Rice, Mac & Cheese") or (A3 == "Brown Stew Chicken, Rice, Mac & Cheese") or (A4 == "Brown Stew Chicken, Rice, Mac & Cheese") or (A5 == "Brown Stew Chicken, Rice, Mac & Cheese"):
                print("\nBrown Stew Chicken, Rice, Mac & Cheese Ingredients:\n")
                for i in brown_stew_chicken_rice_mac_cheese:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Chicken Curry") or (A2 == "Chicken Curry") or (A3 == "Chicken Curry") or (A4 == "Chicken Curry") or (A5 == "Chicken Curry"):
                print("\nChicken Curry Ingredients:\n")
                for i in chicken_curry:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Chicken Enchiladas") or (A2 == "Chicken Enchiladas") or (A3 == "Chicken Enchiladas") or (A4 == "Chicken Enchiladas") or (A5 == "Chicken Enchiladas"):
                print("\nChicken Enchiladas Ingredients:\n")
                for i in chicken_enchiladas:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Chicken Fajitas") or (A2 == "Chicken Fajitas") or (A3 == "Chicken Fajitas") or (A4 == "Chicken Fajitas") or (A5 == "Chicken Fajitas"):
                print("\nChicken Fajitas Ingredients:\n")
                for i in chicken_fajitas:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Chicken Roast") or (A2 == "Chicken Roast") or (A3 == "Chicken Roast") or (A4 == "Chicken Roast") or (A5 == "Chicken Roast"):
                print("\nChicken Roast Ingredients:\n")
                for i in chicken_roast:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Chicken Stir Fry") or (A2 == "Chicken Stir Fry") or (A3 == "Chicken Stir Fry") or (A4 == "Chicken Stir Fry") or (A5 == "Chicken Stir Fry"):
                print("\nChicken Stir Fry Ingredients:\n")
                for i in chicken_stir_fry:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Chicken Wings") or (A2 == "Chicken Wings") or (A3 == "Chicken Wings") or (A4 == "Chicken Wings")or (A5 == "Chicken Wings"):
                print("\nChicken Wings Ingredients:\n")
                for i in chicken_wings:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Chilli Con Carne") or (A2 == "Chilli Con Carne") or (A3 == "Chilli Con Carne") or (A4 == "Chilli Con Carne") or (A5 == "Chilli Con Carne"):
                print("\nChilli Con Carne Ingredients:\n")
                for i in chilli_con_carne:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Fried Chicken & Homemade Oven Chips") or (A2 == "Fried Chicken & Homemade Oven Chips") or (A3 == "Fried Chicken & Homemade Oven Chips") or (A4 == "Fried Chicken & Homemade Oven Chips") or (A5 == "Fried Chicken & Homemade Oven Chips"):
                print("\nFried Chicken & Homemade Oven Chips Ingredients:\n")
                for i in fried_chicken_homemade_oven_chips:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Homemade Pizza") or (A2 == "Homemade Pizza") or (A3 == "Homemade Pizza") or (A4 == "Homemade Pizza") or (A5 == "Homemade Pizza"):
                print("\nHomemade Pizza Ingredients:\n")
                for i in homemade_pizza:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Homemade Roast Potatoes") or (A2 == "Homemade Roast Potatoes") or (A3 == "Homemade Roast Potatoes") or (A4 == "Homemade Roast Potatoes") or (A5 == "Homemade Roast Potatoes"):
                print("\nHomemade Roast Potatoes Ingredients:\n")
                for i in homemade_roast_potatoes:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Hot Dogs") or (A2 == "Hot Dogs") or (A3 == "Hot Dogs") or (A4 == "Hot Dogs") or (A5 == "Hot Dogs"):
                print("\nHot Dogs:\n")
                for i in hotdogs:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Pasta Bake") or (A2 == "Pasta Bake") or (A3 == "Pasta Bake") or (A4 == "Pasta Bake") or (A5 == "Pasta Bake"):
                print("\nPasta Bake Ingredients:\n")
                for i in pasta_bake:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Pasta Sauce & Garlic Bread") or (A2 == "Pasta Sauce & Garlic Bread") or (A3 == "Pasta Sauce & Garlic Bread") or (A4 == "Pasta Sauce & Garlic Bread") or (A5 == "Pasta Sauce & Garlic Bread"):
                print("\nPasta Sauce & Garlic Bread Ingredients:\n")
                for i in pasta_sauce_garlic_bread:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Sausage & Chips") or (A2 == "Sausage & Chips") or (A3 == "Sausage & Chips") or (A4 == "Sausage & Chips") or (A5 == "Sausage & Chips"):
                print("\nSausage & Chips Ingredients:\n")
                for i in sausage_chips:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Soup & Bread") or (A2 == "Soup & Bread") or (A3 == "Soup & Bread") or (A4 == "Soup & Bread"):
                print("\nSoup & Bread Ingredients:\n")
                for i in soup_bread:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            print("\n----- Dinner Menu for this week -----\n")
            print(A1)
            print(A2)
            print(A3)
            print(A4)
            print(A5)

            file = open("WOTM_MEALS_" + today + ".txt", "a")
            file.write("\n----- Dinner Menu for this week -----\n\n" + A1 + "\n" + A2 + "\n" + A3 + "\n" + A4 + "\n" + A5 + "\n")
            file.close()

            Q3 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

            if (Q3 == "Y") or (Q3 == "y"):
                clear()
                main_menu()
            elif (Q3 == "N") or (Q3 == "n"):
                print("\nClosing application..")
                sys.exit(0)
            else:
                print("\nInvalid option. Please try again.")
                time.sleep(3)
                menu_food_essentials()
        elif (Q2 == "M") or (Q2 == "m"):
            print("\nDinner Menu (Choose 5 from this menu):")

            M1 = input("\nEnter Meal 1: ")
            M2 = input("Enter Meal 2: ")
            M3 = input("Enter Meal 3: ")
            M4 = input("Enter Meal 4: ")
            M5 = input("Enter Meal 5: ")

        if (M1 == "Baked Chicken Breast") or (M2 == "Baked Chicken Breast") or (M3 == "Baked Chicken Breast") or (M4 == "Baked Chicken Breast") or (M5 == "Baked Chicken Breast"):
                print("\nBaked Chicken Breast Ingredients:\n")
                for i in baked_chicken_breast:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

        if (M1 == "Beef Steak Burgers & Salad") or (M2 == "Beef Steak Burgers & Salad") or (M3 == "Beef Steak Burgers & Salad") or (M4 == "Beef Steak Burgers & Salad") or (M5 == "Beef Steak Burgers & Salad"):
            print("\nBeef Steak Burgers & Salad Ingredients:\n")
            for i in beef_stake_burger:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Brown Stew Chicken & Rice") or (M2 == "Brown Stew Chicken & Rice") or (M3 == "Brown Stew Chicken & Rice") or (M4 == "Brown Stew Chicken & Rice") or (M5 == "Brown Stew Chicken & Rice"):
                print("\nBrown Stew Chicken & Rice Ingredients:\n")
                for i in brown_stew_chicken_rice:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

        if (M1 == "Chicken Curry") or (M2 == "Chicken Curry") or (M3 == "Chicken Curry") or (M4 == "Chicken Curry") or (M5 == "Chicken Curry"):
            print("\nChicken Curry Ingredients:\n")
            for i in chicken_curry:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Chicken Enchiladas") or (M2 == "Chicken Enchiladas") or (M3 == "Chicken Enchiladas") or (M4 == "Chicken Enchiladas") or (M5 == "Chicken Enchiladas"):
            print("\nChicken Enchiladas Ingredients:\n")
            for i in chicken_enchiladas:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Chicken Fajitas") or (M2 == "Chicken Fajitas") or (M3 == "Chicken Fajitas") or (M4 == "Chicken Fajitas") or (M5 == "Chicken Fajitas"):
            print("\nChicken Fajitas Ingredients:\n")
            for i in chicken_fajitas:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Chicken Roast") or (M2 == "Chicken Roast") or (M3 == "Chicken Roast") or (M4 == "Chicken Roast") or (M5 == "Chicken Roast"):
            print("\nChicken Roast Ingredients:\n")
            for i in chicken_roast:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Chicken Stir Fry") or (M2 == "Chicken Stir Fry") or (M3 == "Chicken Stir Fry") or (M4 == "Chicken Stir Fry") or (M5 == "Chicken Stir Fry"):
            print("\nChicken Stir Fry Ingredients:\n")
            for i in chicken_stir_fry:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Chicken Wings") or (M2 == "Chicken Wings") or (M3 == "Chicken Wings") or (M4 == "Chicken Wings")or (M5 == "Chicken Wings"):
            print("\nChicken Wings Ingredients:\n")
            for i in chicken_wings:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Chilli Con Carne") or (M2 == "Chilli Con Carne") or (M3 == "Chilli Con Carne") or (M4 == "Chilli Con Carne") or (M5 == "Chilli Con Carne"):
            print("\nChilli Con Carne Ingredients:\n")
            for i in chilli_con_carne:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Fried Chicken & Homemade Oven Chips") or (M2 == "Fried Chicken & Homemade Oven Chips") or (M3 == "Fried Chicken & Homemade Oven Chips") or (M4 == "Fried Chicken & Homemade Oven Chips") or (M5 == "Fried Chicken & Homemade Oven Chips"):
            print("\nFried Chicken & Homemade Oven Chips Ingredients:\n")
            for i in fried_chicken:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Homemade Oven Chips") or (M2 == "Homemade Oven Chips") or (M3 == "Homemade Oven Chips") or (M4 == "Homemade Oven Chips") or (M5 == "Homemade Oven Chips"):
            print("\nHomemade Oven Chips Ingredients:\n")
            for i in homemade_oven_chips:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Homemade Pizza") or (M2 == "Homemade Pizza") or (M3 == "Homemade Pizza") or (M4 == "Homemade Pizza") or (M5 == "Homemade Pizza"):
            print("\nHomemade Pizza Ingredients:\n")
            for i in homemade_pizza:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Homemade Roast Potatoes") or (M2 == "Homemade Roast Potatoes") or (M3 == "Homemade Roast Potatoes") or (M4 == "Homemade Roast Potatoes") or (M5 == "Homemade Roast Potatoes"):
            print("\nHomemade Roast Potatoes Ingredients:\n")
            for i in homemade_roast_potatoes:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Hot Dogs") or (M2 == "Hot Dogs") or (M3 == "Hot Dogs") or (M4 == "Hot Dogs") or (M5 == "Hot Dogs"):
            print("\nHot Dogs:\n")
            for i in hotdogs:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Mac & Cheese") or (M2 == "Mac & Cheese") or (M3 == "Mac & Cheese") or (M4 == "Mac & Cheese") or (M5 == "Mac & Cheese"):
            print("\nMac & Cheese Ingredients:\n")
            for i in mac_and_cheese:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Pasta Bake") or (M2 == "Pasta Bake") or (M3 == "Pasta Bake") or (M4 == "Pasta Bake") or (M5 == "Pasta Bake"):
            print("\nPasta Bake Ingredients:\n")
            for i in pasta_bake:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Pasta Sauce & Garlic Bread") or (M2 == "Pasta Sauce & Garlic Bread") or (M3 == "Pasta Sauce & Garlic Bread") or (M4 == "Pasta Sauce & Garlic Bread") or (M5 == "Pasta Sauce & Garlic Bread"):
            print("\nPasta Sauce & Garlic Bread Ingredients:\n")
            for i in pasta_sauce_garlic_bread:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Sausage & Chips") or (M2 == "Sausage & Chips") or (M3 == "Sausage & Chips") or (M4 == "Sausage & Chips") or (M5 == "Sausage & Chips"):
            print("\nSausage & Chips Ingredients:\n")
            for i in sausage_chips:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

        if (M1 == "Soup & Bread") or (M2 == "Soup & Bread") or (M3 == "Soup & Bread") or (M4 == "Soup & Bread"):
            print("\nSoup & Bread Ingredients:\n")
            for i in soup_bread:
                print(i)
                file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                file.write(i + "\n")
                file.close()

            print("\n----- Dinner Menu for this week -----\n")
            print(M1)
            print(M2)
            print(M3)
            print(M4)
            print(M5)

            file = open("WOTM_MEALS_" + today + ".txt", "a")
            file.write("----- Dinner Menu for this week -----\n\n" + M1 + "\n" + M2 + "\n" + M3 + "\n" + M4 + "\n" + M5 + "\n")
            file.close()

        Q4 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

        if (Q4 == "Y") or (Q4 == "y"):
            clear()
            main_menu()
        elif (Q4 == "N") or (Q4 == "n"):
            print("\nClosing application..")
            sys.exit(0)
        else:
            print("\nInvalid option. Please try again.")
            time.sleep(3)
            menu_dinner()

    elif (Q1 == "N") or (Q1 == "n"):
        clear()
        main_menu()
    else:
        print("Invalid option. Please try again.")
        menu_dinner()

def menu_baking():

    global M1, M2

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

    print("----- Baking Menu -----\n")

    for i in baking:
        print(i)

    Q1 = input("\nWould you like to continue? (Enter Y or N): ")

    if (Q1 == "Y") or (Q1 == "y"):
        Q2 = input("\nAuto selection or Manual selection? (Enter A or M): ")
        if (Q2 == "A") or (Q2 == "a"):
            clear()
            print("--- Meals and Ingredients ---")
            A1 = random.choice(baking)
            A2 = random.choice(baking)

            if (A1 == "Cinnamon & Almond Sponge Cake") or (A2 == "Cinnamon & Almond Sponge Cake"):
                print("\nCinnamon & Almond Sponge Cake Ingredients:\n")
                for i in cinnamon_almond_sponge_cake:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Flapjack") or (A2 == "Flapjack"):
                print("\nFlapjack Ingredients:\n")
                for i in flapjack:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Vanilla Cupcakes") or (A2 == "Vanilla Cupcakes"):
                print("\nVanilla Cupcakes Ingredients:\n")
                for i in vanilla_cupcakes:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (A1 == "Vanilla Sponge Cake") or (A2 == "Vanilla Sponge Cake"):
                print("\nVanilla Sponge Cake Ingredients:\n")
                for i in vanilla_sponge_cake:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            print("\n----- Baking Menu for this week -----\n")
            print(A1)
            print(A2)

            file = open("WOTM_MEALS_" + today + ".txt", "a")
            file.write("\n----- Baking Menu for this week -----\n\n" + A1 + "\n" + A2 + "\n")
            file.close()

            Q3 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

            if (Q3 == "Y") or (Q3 == "y"):
                clear()
                main_menu()
            elif (Q3 == "N") or (Q3 == "n"):
                print("\nClosing application..")
                sys.exit(0)
            else:
                print("\nInvalid option. Please try again.")
                time.sleep(3)
                menu_baking()
        elif (Q2 == "M") or (Q2 == "m"):
            print("\nBaking Menu (Choose 2 from this menu):")

            M1 = input("\nEnter Meal 1: ")
            M2 = input("Enter Meal 2: ")

            if (M1 == "Cinnamon & Almond Sponge Cake") or (M2 == "Cinnamon & Almond Sponge Cake"):
                print("\nCinnamon & Almond Sponge Cake Ingredients:\n")
                for i in cinnamon_almond_sponge_cake:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (M1 == "Flapjack") or (M2 == "Flapjack"):
                print("\nFlapjack Ingredients:\n")
                for i in flapjack:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (M1 == "Vanilla Cupcakes") or (M2 == "Vanilla Cupcakes"):
                print("\nVanilla Cupcakes Ingredients:\n")
                for i in vanilla_cupcakes:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

            if (M1 == "Vanilla Sponge Cake") or (M2 == "Vanilla Sponge Cake"):
                print("\nVanilla Sponge Cake Ingredients:\n")
                for i in vanilla_sponge_cake:
                    print(i)
                    file = open("WOTM_SHOPPING_LIST_" + today + ".txt", "a")
                    file.write(i + "\n")
                    file.close()

                print("\n----- Baking Menu for this week -----\n")
                print(M1)
                print(M2)

                file = open("WOTM_MEALS_" + today + ".txt", "a")
                file.write("----- Baking Menu for this week -----\n\n" + M1 + "\n" + M2)
                file.close()

            Q4 = input("\nWould you like to return to the main menu? (Enter Y or N): ")

            if (Q4 == "Y") or (Q4 == "y"):
                clear()
                main_menu()
            elif (Q4 == "N") or (Q4 == "n"):
                print("\nClosing application..")
                sys.exit(0)
            else:
                print("\nInvalid option. Please try again.")
                time.sleep(3)
                menu_baking()

    elif (Q1 == "N") or (Q1 == "n"):
        clear()
        main_menu()
    else:
        print("Invalid option. Please try again.")
        menu_baking()

main_menu()