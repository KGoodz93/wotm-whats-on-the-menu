# WOTM - What's On The Menu!

WOTM (What's On The Menu) is an application which help choose meals automatically and lists the required ingredients. This then generates a shopping list for you to take to your local supermarket. The idea behind this application is to make easier and more convient when decided what to cook, and what igredients are required. This also has a scratchpad feature to add items or ingredients during the week which are also needed from your shop. All data is stored in SQLite3 Database.

## Home

This is the main application window on launch. This will allow the user the navigate to other features within the application.

![Screenshot 2022-05-30 140255](https://user-images.githubusercontent.com/82043281/170998069-e289b15e-01d0-40c8-a60b-a5c98f518081.png)

## View Menu

View Menu is a feature which shows all meals (Breakfast / Dinner) and Baking, which are available in WOTM. This is for viewing purposes only.

![view_menu](https://user-images.githubusercontent.com/82043281/148290890-f7a3f755-f1f1-479d-9ca2-f17caafa374c.png)

## Scratchpad

Scratchpad is a feature whoch allows the user to add in items or ingredients which are needed throughout the week. There are 3 columns for Quantity, Item and Price. Once entered into the entry, "Add" will add this row into the connected Database. When selecting an item or ingredient, "Delete" will remove the row from the Database.

![scratchpad](https://user-images.githubusercontent.com/82043281/148290912-b9277245-91fc-4960-8b95-d72a11c9f513.png)

## Generate Shopping

Generate Shopping is the feature which will choose 6 meals from the dinner menu automatically once this button is clicked. The ingredients for these meals will be added into the database and viewed in the treeview table. This will also show the estimated price and total items within this list. "Generate Shopping" button will prompt if the user would like an email to be sent. Ready to take on your food shop, including the quantity and ingredient/item name.

![generate_shopping](https://user-images.githubusercontent.com/82043281/148290925-875c5e15-200f-416c-8401-52b0eccaf8db.png)
