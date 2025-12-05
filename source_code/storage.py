import csv
import os

# Define the file name. Keeping it in the same folder is safer for submission.
INVENTORY_FILE = "inventory.csv"

def add_product(product_id, name, quantity, price):
    # Check if the file exists to see if we need headers (optional, but good practice)
    file_exists = os.path.exists(INVENTORY_FILE)
    
    # Open file in append mode ('a') so we don't erase old data
    with open(INVENTORY_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        # Write the data as a new row
        writer.writerow([product_id, name, quantity, price])
        
    print(f"Product '{name}' added successfully.")

def view_products():
    print("\nCurrent Inventory:")
    
    # Check if file exists first to avoid crashing
    if not os.path.exists(INVENTORY_FILE):
        print("No inventory file found. Try adding a product first.")
        return

    # Open in read mode ('r')
    with open(INVENTORY_FILE, 'r') as file:
        reader = csv.reader(file)
        # Loop through each row in the CSV and print it
        for row in reader:
            # Formatting the output to make it look nice
            print(f"ID: {row[0]} | Name: {row[1]} | Qty: {row[2]} | Price: {row[3]}")

def update_product(product_id, name=None, quantity=None, price=None):
    updated = False
    rows = []
    
    # Check if file exists before trying to read
    if not os.path.exists(INVENTORY_FILE):
        print("Inventory is empty.")
        return

    # Read all data into a list first
    with open(INVENTORY_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Check if this is the row we want to update
            if row[0] == product_id:
                # Update specific fields if the user provided new data
                if name: 
                    row[1] = name
                if quantity: 
                    row[2] = quantity
                if price: 
                    row[3] = price
                updated = True
            # Add the row (updated or original) to our list
            rows.append(row)
    
    # If we found and updated the product, write everything back to the file
    if updated:
        with open(INVENTORY_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Product {product_id} updated successfully.")
    else:
        print(f"Product {product_id} not found.")

def delete_product(product_id):
    deleted = False
    rows = []
    
    if not os.path.exists(INVENTORY_FILE):
        print("Inventory is empty.")
        return

    # Read the file to find the item to remove
    with open(INVENTORY_FILE, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # If the ID does NOT match, keep the row
            if row[0] != product_id:
                rows.append(row)
            else:
                # If it matches, we don't append it (effectively deleting it)
                deleted = True
    
    # Rewrite the file with the remaining rows
    if deleted:
        with open(INVENTORY_FILE, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print(f"Product {product_id} deleted successfully.")
    else:
        print(f"Product {product_id} not found.")