import requests


BASE_URL = "http://127.0.0.1:5000/api"

def list_products():

    try:
        response = requests.get(f"{BASE_URL}/inventory")

        print("\n ALL PRODUCTS ")

        if response.ok:
            print(response.json())
        else:
            print("Error:", response.json())

    except requests.exceptions.ConnectionError:
        print("Could not connect to the Flask server.")

def get_product():

    product_id = input("Enter product ID: ")

    try:
        response = requests.get(
            f"{BASE_URL}/inventory/{product_id}"
        )

        print("\n===== PRODUCT =====")

        if response.ok:
            print(response.json())
        else:
            print("Error:", response.json())

    except requests.exceptions.ConnectionError:
        print("Could not connect to the Flask server.")

def add_product():

    print("\n ADD NEW PRODUCT ")

    product = {
        "product_name": input("Product name: "),
        "brands": input("Brand: "),
        "barcode": input("Barcode: "),
        "categories": input("Category: "),
        "ingredients_text": input("Ingredients: "),
        "quantity": int(input("Quantity: ")),
        "price": float(input("Price: "))
    }

    try:
        response = requests.post(
            f"{BASE_URL}/inventory",
            json=product
        )

        print("\n RESPONSE ")

        if response.ok:
            print("Product added successfully!")
            print(response.json())
        else:
            print("Failed to add product.")
            print(response.json())

    except requests.exceptions.ConnectionError:
        print("Could not connect to the Flask server.")

    except ValueError:
        print("Quantity must be a number and price must be a number.")

def update_product():

    product_id = input("Enter product ID to update: ")

    print("\n ENTER NEW PRODUCT DETAIL ")

    try:
        product = {
            "product_name": input("Product name: "),
            "brands": input("Brand: "),
            "barcode": input("Barcode: "),
            "categories": input("Category: "),
            "ingredients_text": input("Ingredients: "),
            "quantity": int(input("Quantity: ")),
            "price": float(input("Price: "))
        }

        response = requests.put(
            f"{BASE_URL}/inventory/{product_id}",
            json=product
        )

        print("\n===== RESPONSE =====")

        if response.ok:
            print("Product updated successfully!")
            print(response.json())
        else:
            print("Failed to update product.")
            print(response.json())

    except requests.exceptions.ConnectionError:
        print("Could not connect to the Flask server.")

    except ValueError:
        print("Quantity must be a number and price must be a number.")

def delete_product():

    product_id = input("Enter product ID to delete: ")

    confirm = input(
        f"Are you sure you want to delete product {product_id}? (y/n): "
    )

    if confirm.lower() != "y":
        print("Delete cancelled.")
        return

    try:
        response = requests.delete(
            f"{BASE_URL}/inventory/{product_id}"
        )

        if response.ok:
            print("Product deleted successfully!")
            print(response.json())
        else:
            print("Failed to delete product.")
            print(response.json())

    except requests.exceptions.ConnectionError:
        print("Could not connect to the Flask server.")

def search_barcode():

    barcode = input("Enter barcode: ")

    try:
        response = requests.get(
            f"{BASE_URL}/products/barcode/{barcode}"
        )

        print("\n===== SEARCH RESULT =====")

        if response.ok:
            print(response.json())
        else:
            print("Product not found.")
            print(response.json())

    except requests.exceptions.ConnectionError:
        print("Could not connect to the Flask server.")

def search_name():

    name = input("Enter product name: ")

    try:
        response = requests.get(
            f"{BASE_URL}/products/search",
            params={"name": name}
        )

        print("\n SEARCH RESULT ")

        if response.ok:
            print(response.json())
        else:
            print("Product not found.")
            print(response.json())

    except requests.exceptions.ConnectionError:
        print("Could not connect to the Flask server.")

def show_menu():

    print("\n")
    print(" INVENTORY CLI ")

    print("1. List all products")
    print("2. Get product by ID")
    print("3. Add new product")
    print("4. Update product")
    print("5. Delete product")
    print("6. Search by barcode")
    print("7. Search by name")
    print("8. Exit")

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            list_products()
        elif choice == "2":
            get_product()
        elif choice == "3":
            add_product()
        elif choice == "4":
            update_product()
        elif choice == "5":
            delete_product()
        elif choice == "6":
            search_barcode()
        elif choice == "7":
            search_name()
        elif choice == "8":
            print("Exiting Inventory CLI...")
            break
        else:
            print("Invalid option. Please choose 1-8.")

if __name__ == "__main__":
    main()

