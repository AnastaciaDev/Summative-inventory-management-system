import requests


BASE_URL = "https://world.openfoodfacts.org"


def get_product_by_barcode(barcode):

    url = f"{BASE_URL}/api/v2/product/{barcode}.json"

    response = requests.get(
        url,
        timeout=10
    )

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("status") != 1:
        return None

    product = data.get("product", {})

    return {
        "barcode": barcode,
        "product_name": product.get("product_name", ""),
        "brands": product.get("brands", ""),
        "categories": product.get("categories", ""),
        "ingredients_text": product.get(
            "ingredients_text",
            ""
        ),
        "image_url": product.get(
            "image_url",
            ""
        )
    }
