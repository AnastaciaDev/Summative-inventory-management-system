from flask import Blueprint, request

from services.openfoodfacts_service import (
    get_product_by_barcode
)

from data.inventory import inventory

from utilities.response import (
    success_response,
    not_found,
    server_error
)


product_routes = Blueprint(
    "product_routes",
    __name__
)

@product_routes.route(
    "/api/products/barcode/<barcode>",
    methods=["GET"]
)
def search_by_barcode(barcode):

    try:

        product = get_product_by_barcode(barcode)

        if product is None:
            return not_found(
                "Product not found on OpenFoodFacts"
            )

        return success_response(
            "Product found",
            product
        )

    except Exception:
        return server_error()

@product_routes.route(
    "/api/products/search",
    methods=["GET"]
)
def search_by_name():

    try:

        name = request.args.get(
            "name",
            ""
        ).lower().strip()

        if not name:
            return {
                "message": "Product name is required"
            }, 400

        results = []

        for product in inventory:

            if name in product["product_name"].lower():

                results.append(product)

        return success_response(
            "Search completed",
            results
        )

    except Exception:
        return server_error()

    