import { useEffect, useState } from "react";

function ProductForm({ product, onSave, onCancel }) {
  const [formData, setFormData] = useState({
    product_name: "",
    brands: "",
    barcode: "",
    categories: "",
    ingredients_text: "",
    price: "",
    quantity: "",
  });

  useEffect(() => {
    if (product) {
      setFormData({
        product_name: product.product_name || "",
        brands: product.brands || "",
        barcode: product.barcode || "",
        categories: product.categories || "",
        ingredients_text: product.ingredients_text || "",
        price: product.price ?? "",
        quantity: product.quantity ?? "",
      });
    } else {
      setFormData({
        product_name: "",
        brands: "",
        barcode: "",
        categories: "",
        ingredients_text: "",
        price: "",
        quantity: "",
      });
    }
  }, [product]);

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData((previous) => ({
      ...previous,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const productData = {
      barcode: formData.barcode,
      product_name: formData.product_name,
      brands: formData.brands,
      categories: formData.categories,
      ingredients_text: formData.ingredients_text,
      quantity: Number(formData.quantity),
      price: Number(formData.price),
    };

    await onSave(productData);
  };

  return (
    <form
      onSubmit={handleSubmit}
      className="bg-white p-6 rounded-lg shadow mb-6"
    >
      <h2 className="text-xl font-bold mb-4">
        {product ? "Edit Product" : "Add Product"}
      </h2>

      <input
        name="product_name"
        placeholder="Product name"
        value={formData.product_name}
        onChange={handleChange}
        className="border p-2 w-full mb-3 rounded"
        required
      />

      <input
        name="brands"
        placeholder="Brand"
        value={formData.brands}
        onChange={handleChange}
        className="border p-2 w-full mb-3 rounded"
      />

      <input
        name="barcode"
        placeholder="Barcode"
        value={formData.barcode}
        onChange={handleChange}
        className="border p-2 w-full mb-3 rounded"
        required
      />

      <input
        name="categories"
        placeholder="Category"
        value={formData.categories}
        onChange={handleChange}
        className="border p-2 w-full mb-3 rounded"
        required
      />

      <textarea
        name="ingredients_text"
        placeholder="Ingredients"
        value={formData.ingredients_text}
        onChange={handleChange}
        className="border p-2 w-full mb-3 rounded"
      />

      <input
        name="price"
        type="number"
        step="0.01"
        placeholder="Price"
        value={formData.price}
        onChange={handleChange}
        className="border p-2 w-full mb-3 rounded"
        required
      />

      <input
        name="quantity"
        type="number"
        min="0"
        placeholder="Quantity"
        value={formData.quantity}
        onChange={handleChange}
        className="border p-2 w-full mb-3 rounded"
        required
      />

      <button
        type="submit"
        className="bg-blue-600 text-white px-4 py-2 rounded mr-2"
      >
        {product ? "Update Product" : "Add Product"}
      </button>

      {product && (
        <button
          type="button"
          onClick={onCancel}
          className="bg-gray-500 text-white px-4 py-2 rounded"
        >
          Cancel
        </button>
      )}
    </form>
  );
}

export default ProductForm;

