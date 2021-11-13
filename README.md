# WOTM - What's On The Menu!

WOTM (What's On The Menu) is an application which help choose meals automatically and lists the required ingredients. This then generates a shopping list for you to take to your local supermarket. The idea behind this application is to make easier and more convient when decided what to cook, and what igredients are required. This also has a scratchpad feature to add items or ingredients during the week which are also needed from your shop. All data is stored in SQLite3 Database.

## Home

This is the main application window on launch. This will allow the user the navigate to other features within the application.

![Screenshot 2021-11-08 15 32 49](https://user-images.githubusercontent.com/82043281/140820157-9f397ff0-a700-4ce6-b100-712b3986ae64.png)

## View Menu

View Menu is a feature which shows all meals (Breakfast / Dinner) and Baking, which are available in WOTM. This is for viewing purposong only.

<img width="447" alt="Screenshot 2021-11-12 23 57 47" src="https://user-images.githubusercontent.com/82043281/141597560-54976749-ec59-41c5-8bca-ed43af971559.png">

## Scratchpad

Scratchpad is a feature whoch allows the user to add in items or ingredients which are needed throughout the week. There are 3 columns for Quantity, Item and Price. Once entered into the entry, "Add" will add this row into the connected Database. When selecting an item or ingredient, "Delete" will remove the row from the Database.

<img width="447" alt="Screenshot 2021-11-12 23 57 18" src="https://user-images.githubusercontent.com/82043281/141597568-09b2daa7-68a3-4784-8be4-a53685c52177.png">

## Generate Shopping

Generate Shopping is the feature which will choose 4 meals from the dinner menu automatically once this button is clicked. The ingredients for these meals will be added into the treeview. This will also show the estimated price and total items within this list. "Generate Shopping" button will save this shopping list into a text file, ready to take on your food shop, including the quantity and ingredient/item name.

<img width="447" alt="Screenshot 2021-11-12 23 57 04" src="https://user-images.githubusercontent.com/82043281/141597587-01db9126-e3fe-4011-93c0-493cbb3835f5.png">
