import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

from app import app


def test_barcode_route():

    app.config["TESTING"] = True

    with app.test_client() as client:

        response = client.get(
            "/api/products/barcode/3017624010701"
        )

        assert response.status_code in [200, 404]
        