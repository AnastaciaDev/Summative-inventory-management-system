import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

import pytest

from app import app


@pytest.fixture
def client():

    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_get_inventory(client):

    response = client.get("/api/inventory")

    assert response.status_code == 200


def test_get_product(client):

    response = client.get("/api/inventory/1")

    assert response.status_code == 200


def test_product_not_found(client):

    response = client.get("/api/inventory/999")

    assert response.status_code == 404


def test_add_product(client):

    product = {
        "product_name": "Test Milk",
        "barcode": "111111111",
        "brands": "Test Brand",
        "categories": "Milk",
        "ingredients_text": "Milk",
        "price": 5.00,
        "quantity": 10
    }

    response = client.post(
        "/api/inventory",
        json=product
    )

    assert response.status_code == 201


def test_delete_product(client):

    response = client.delete(
        "/api/inventory/1"
    )

    assert response.status_code in [200, 404]