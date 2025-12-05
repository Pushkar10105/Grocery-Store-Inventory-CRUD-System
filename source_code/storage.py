import csv
import os

# defining the path to the csv file. 
# using ".." to go up one level and look into the 'data' folder so code and data are separate.
INVENTORY_FILE = os.path.join("..", "data", "inventory.csv") 

def add_product(product_id, name, quantity, price):
    # check if the data folder exists, if not, create it so the program doesn't crash
    folder_path = os.path.dirname(INVENTORY_FILE)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # open file in append mode ('a') so we add to the list instead of overwriting it
    with open(INVENTORY_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([product_id, name, quantity, price])
    print(f"Product {name} added successfully.")

def view_products():
    print("\nCurrent Inventory:")
    # using try-except to handle the case where the file doesn't exist yet (first run)
    try:
        with open(INVENTORY_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    except FileNotFoundError:
        print("No inventory file found. Try adding a product first!")

def update_product(product_id, name=None, quantity=None, price=None):
    updated = False
    rows = []
    
    try:
        # read all the rows from the file into a list
        with open(INVENTORY_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # check if this is the product we want to update
                if row[0] == product_id:
                    # update the fields only if the user provided new info
                    if name: row[1] = name
                    if quantity: row[2] = quantity
                    if price: row[3] = price
                    updated = True
                rows.append(row) # add the row (updated or not) to our list
        
        # if we found the product, rewrite the whole file with the updated list
        if updated:
            with open(INVENTORY_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print(f"Product {product_id} updated successfully.")
        else:
            print(f"Product {product_id} not found.")
            
    except FileNotFoundError:
        print("Inventory is empty.")

def delete_product(product_id):
    deleted = False
    rows = []
    
    try:
        # read the file to find the item to remove
        with open(INVENTORY_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                # if the ID does NOT match, we keep the row
                if row[0] != product_id:
                    rows.append(row)
                else:
                    # if it matches, we don't add it to 'rows', effectively deleting it
                    deleted = True
        
        # write the remaining rows back to the file
        if deleted:
            with open(INVENTORY_FILE, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            print(f"Product {product_id} deleted successfully.")
        else:
            print(f"Product {product_id} not found.")
            
    except FileNotFoundError:
        print("Inventory is empty.")