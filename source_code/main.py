# main.py
from storage import add_product, view_products, update_product, delete_product

def menu():
    while True:
        print("\n--- Grocery Store Inventory ---")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            view_products()

        elif choice == "2":
            product_id = input("Enter Product ID: ")
            name = input("Enter Product Name: ")
            
            try:
                quantity = int(input("Enter Quantity: ")) # Convert to Integer
                price = float(input("Enter Price: "))     # Convert to Float
                add_product(product_id, name, quantity, price)
            except ValueError:
                print("Error: Quantity must be a whole number and Price must be a decimal.")

        elif choice == "3":
            product_id = input("Enter Product ID to update: ")
            name = input("Enter new Name (or press Enter to skip): ")
            quantity_str = input("Enter new Quantity (or press Enter to skip): ")
            price_str = input("Enter new Price (or press Enter to skip): ")

            kwargs = {}
            if name: 
                kwargs['name'] = name
            
            if quantity_str:
                try:
                    kwargs['quantity'] = int(quantity_str)
                except ValueError:
                    print("Skipping invalid quantity update.")
            
            if price_str:
                try:
                    kwargs['price'] = float(price_str)
                except ValueError:
                    print("Skipping invalid price update.")

            if kwargs:
                update_product(product_id, **kwargs)
            else:
                print("No changes detected.")

        elif choice == "4":
            product_id = input("Enter Product ID to delete: ")
            delete_product(product_id)

        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    menu()
