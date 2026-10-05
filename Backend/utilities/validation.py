def validate_product(data):

    if not data:
        return False, "Request body is required"

    if "product_name" not in data:
        return False, "Product name is required"

    if "barcode" not in data:
        return False, "Barcode is required"

    if "categories" not in data:
        return False, "Category is required"

    if "price" not in data:
        return False, "Price is required"

    if "quantity" not in data:
        return False, "Quantity is required"

    if not isinstance(data["price"], (int, float)):
        return False, "Price must be a number"

    if not isinstance(data["quantity"], int):
        return False, "Quantity must be a whole number"

    if data["price"] < 0:
        return False, "Price cannot be negative"

    if data["quantity"] < 0:
        return False, "Quantity cannot be negative"

    return True, None

