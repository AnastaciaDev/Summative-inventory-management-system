import { useEffect, useState } from "react";

import Navbar from "../components/Navbar";
import ProductForm from "../components/ProductForm";
import ProductCard from "../components/ProductCard";

import {
  getInventory,
  addProduct,
  updateProduct,
  deleteProduct,
} from "../services/api";

function Dashboard() {
  const [products, setProducts] = useState([]);
  const [editingProduct, setEditingProduct] = useState(null);
  const [showForm, setShowForm] = useState(false);

  useEffect(() => {
    loadProducts();
  }, []);

  const loadProducts = async () => {
    try {
      const result = await getInventory();

      setProducts(result.data);
    } catch (error) {
      console.error(error);
      alert("Failed to load inventory");
    }
  };

  const handleSave = async (product) => {
    try {
      if (editingProduct) {
        await updateProduct(
          editingProduct.id,
          product
        );
      } else {
        await addProduct(product);
      }

      await loadProducts();

      setEditingProduct(null);
      setShowForm(false);

    } catch (error) {
      console.error(error);
      alert("Failed to save product");
    }
  };

  const handleEdit = (product) => {
    setEditingProduct(product);
    setShowForm(true);
  };

  const handleDelete = async (id) => {
    try {
      await deleteProduct(id);

      await loadProducts();

    } catch (error) {
      console.error(error);
      alert("Failed to delete product");
    }
  };

  return (
    <div className="min-h-screen">

      <Navbar />

      <main className="max-w-6xl mx-auto p-6">

        {/* Header */}
        <div className="flex justify-between items-center mb-6">

          <h1 className="text-3xl font-bold">
            Inventory
          </h1>

          <button
            onClick={() => {
              setEditingProduct(null);
              setShowForm(!showForm);
            }}
            className="bg-blue-600 text-white px-4 py-2 rounded"
          >
            {showForm ? "Close Form" : "Add Product"}
          </button>

        </div>

        {showForm && (
          <ProductForm
            product={editingProduct}
            onSave={handleSave}
            onCancel={() => {
              setEditingProduct(null);
              setShowForm(false);
            }}
          />
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">

          {products.map((product) => (
            <ProductCard
              key={product.id}
              product={product}
              onEdit={handleEdit}
              onDelete={handleDelete}
            />
          ))}

        </div>

      </main>

    </div>
  );
}

export default Dashboard;

