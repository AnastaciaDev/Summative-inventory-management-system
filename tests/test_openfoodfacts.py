from services.openfoodfacts_service import (
    get_product_by_barcode
)


def test_openfoodfacts_function():

    product = get_product_by_barcode(
        "3017624010701"
    )

    assert product is None or isinstance(
        product,
        dict
    )
    