from flask import Blueprint, request

from data.inventory import inventory

from utilities.response import (
    success_response,
    created_response,
    deleted_response,
    validation_error,
    not_found,
    server_error
)

from utilities.validation import validate_product


inventory_routes = Blueprint(
    "inventory_routes",
    __name__
)

@inventory_routes.route("/api/inventory", methods=["GET"])
def get_inventory():

    try:
        return success_response(
            "Inventory retrieved successfully",
            inventory
        )

    except Exception:
        return server_error()

@inventory_routes.route("/api/inventory/<int:product_id>", methods=["GET"])
def get_product(product_id):

    try:

        for product in inventory:

            if product["id"] == product_id:

                return success_response(
                    "Product retrieved successfully",
                    product
                )

        return not_found(
            f"Product with ID {product_id} not found"
        )

    except Exception:
        return server_error()

@inventory_routes.route("/api/inventory", methods=["POST"])
def add_product():

    try:

        data = request.get_json()

        if not data:
            return validation_error(
                "Request body is required"
            )

        valid, error = validate_product(data)

        if not valid:
            return validation_error(error)

        if len(inventory) == 0:
            new_id = 1
        else:
            new_id = max(
                product["id"]
                for product in inventory
            ) + 1

        new_product = {
            "id": new_id,
            "barcode": data["barcode"],
            "product_name": data["product_name"],
            "brands": data.get("brands", ""),
            "categories": data["categories"],
            "ingredients_text": data.get(
                "ingredients_text",
                ""
            ),
            "quantity": data["quantity"],
            "price": data["price"]
        }

        inventory.append(new_product)
        # Persist to a json file by convert inventpory list to json
        # write to file

        return created_response(
            "Product added successfully",
            new_product
        )

    except Exception:
        return server_error()

@inventory_routes.route(
    "/api/inventory/<int:product_id>",
    methods=["PUT"]
)
def update_product(product_id):

    try:

        data = request.get_json()

        if not data:
            return validation_error(
                "Request body is required"
            )

        valid, error = validate_product(data)

        if not valid:
            return validation_error(error)

        for product in inventory:

            if product["id"] == product_id:

                product["barcode"] = data["barcode"]

                product["product_name"] = data["product_name"]

                product["brands"] = data.get(
                    "brands",
                    ""
                )

                product["categories"] = data["categories"]

                product["ingredients_text"] = data.get(
                    "ingredients_text",
                    ""
                )

                product["quantity"] = data["quantity"]

                product["price"] = data["price"]

                return success_response(
                    "Product updated successfully",
                    product
                )

        return not_found(
            f"Product with ID {product_id} not found"
        )

    except Exception:
        return server_error()

@inventory_routes.route(
    "/api/inventory/<int:product_id>",
    methods=["DELETE"]
)
def delete_product(product_id):

    try:

        for product in inventory:

            if product["id"] == product_id:

                inventory.remove(product)

                return deleted_response(
                    "Product deleted successfully"
                )

        return not_found(
            f"Product with ID {product_id} not found"
        )

    except Exception:
        return server_error()

    