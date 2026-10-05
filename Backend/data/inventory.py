import json
import os

DATA_FILE = os.path.join(
    os.path.dirname(__file__),
    "inventory.json"
)


def load_inventory():
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        return []


inventory = load_inventory()


def save_inventory():
    with open(DATA_FILE, "w") as file:
        json.dump(inventory, file, indent=4)


def get_all_products():
    return inventory


def get_product_by_id(product_id):
    for product in inventory:
        if product["id"] == product_id:
            return product

    return None


def add_product(product):
    if inventory:
        new_id = max(product["id"] for product in inventory) + 1
    else:
        new_id = 1

    product["id"] = new_id

    inventory.append(product)

    save_inventory()

    return product


def update_product(product_id, updated_data):
    product = get_product_by_id(product_id)

    if not product:
        return None

    product.update(updated_data)
    product["id"] = product_id

    save_inventory()

    return product


def delete_product(product_id):
    product = get_product_by_id(product_id)

    if not product:
        return None

    inventory.remove(product)

    save_inventory()

    return product
