import { useState } from "react";
import { searchBarcode } from "../services/api";

function ProductCard({ product, onEdit, onDelete }) {
  const [barcode, setBarcode] = useState("");
  const [searchResult, setSearchResult] = useState(null);
  const [showConfirm, setShowConfirm] = useState(false);

  const handleSearch = async () => {
    if (!barcode) {
      alert("Please enter a barcode");
      return;
    }

    try {
      const result = await searchBarcode(barcode);
      setSearchResult(result.data);
    } catch (error) {
      alert("Product not found");
      setSearchResult(null);
    }
  };

  const handleDelete = () => {
    onDelete(product.id);
    setShowConfirm(false);
  };

  return (
    <div className="bg-white rounded-lg shadow p-5">

      <h2 className="text-xl font-bold mb-3">
        {product.product_name}
      </h2>

      <p>
        <strong>ID:</strong> {product.id}
      </p>

      <p>
        <strong>Brand:</strong> {product.brands}
      </p>

      <p>
        <strong>Barcode:</strong> {product.barcode}
      </p>

      <p>
        <strong>Category:</strong> {product.categories}
      </p>

      <p>
        <strong>Price:</strong> Ksh.{product.price}
      </p>

      <p>
        <strong>Quantity:</strong> {product.quantity}
      </p>

      <p className="mt-2">
        <strong>Ingredients:</strong>{" "}
        {product.ingredients_text}
      </p>

      <div className="mt-4 flex gap-2">
  <button
    type="button"
    onClick={() => onEdit(product)}
    className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
  >
    Edit
  </button>

  <button
    type="button"
    onClick={() => setShowConfirm(true)}
    className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700"
  >
    Delete
  </button>
  </div>

      {showConfirm && (
        <div className="border rounded p-4 mt-4 bg-gray-50">

          <p className="mb-3">
            Are you sure you want to delete this product?
          </p>

          <button
            onClick={handleDelete}
            className="bg-light-blue-600 text-white px-4 py-2 rounded mr-2"
          >
            Yes, Delete
          </button>

          <button
            onClick={() => setShowConfirm(false)}
            className="bg-gray-500 text-white px-4 py-2 rounded"
          >
            Cancel
          </button>

        </div>
      )}

      <div className="border-t mt-5 pt-5">

        <h3 className="font-bold mb-2">
          Search OpenFoodFacts
        </h3>

        <div className="flex gap-2">

          <input
            type="text"
            placeholder="Enter barcode"
            value={barcode}
            onChange={(e) => setBarcode(e.target.value)}
            className="border p-2 rounded flex-1"
          />

          <button
            onClick={handleSearch}
            className="bg-blue-600 text-white px-4 py-2 rounded"
          >
            Search
          </button>

        </div>

      </div>

      {searchResult && (
        <div className="bg-gray-100 rounded p-4 mt-4">

          <h3 className="font-bold text-lg">
            {searchResult.product_name}
          </h3>

          <p>
            <strong>Brand:</strong>{" "}
            {searchResult.brands}
          </p>

          <p>
            <strong>Category:</strong>{" "}
            {searchResult.categories}
          </p>

          <p>
            <strong>Ingredients:</strong>{" "}
            {searchResult.ingredients_text}
          </p>

        </div>
      )}

    </div>
  );
}

export default ProductCard;
