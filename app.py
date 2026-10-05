from flask import Flask
from flask_cors import CORS

from routes.inventory_routes import inventory_routes
from routes.product_routes import product_routes

app = Flask(__name__)

CORS(app)

app.register_blueprint(inventory_routes)
app.register_blueprint(product_routes)


@app.route("/")
def home():
    return {
        "message": "E-commerce Admin API is running"
    }


if __name__ == "__main__":
    app.run(debug=True)

    