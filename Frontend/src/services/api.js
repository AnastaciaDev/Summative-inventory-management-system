const API_URL = "http://127.0.0.1:5000/api";

export async function getInventory() {
  const response = await fetch(`${API_URL}/inventory`);

  const data = await response.json();

  if (!response.ok) {
    console.error("Get inventory error:", data);
    throw new Error(data.message || "Failed to get inventory");
  }

  return data;
}

export async function addProduct(product) {
  console.log("Product being sent:", product);

  const response = await fetch(`${API_URL}/inventory`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(product),
  });

  const data = await response.json();

  console.log("Backend response:", data);

  if (!response.ok) {
    throw new Error(data.message || "Failed to add product");
  }

  return data;
}

export async function updateProduct(id, product) {
  const response = await fetch(`${API_URL}/inventory/${id}`, {
    method: "PUT",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(product),
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.message || "Failed to update product");
  }

  return data;
}

export async function deleteProduct(id) {
  const response = await fetch(`${API_URL}/inventory/${id}`, {
    method: "DELETE",
  });

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.message || "Failed to delete product");
  }

  return data;
}

export async function searchBarcode(barcode) {
  const response = await fetch(
    `${API_URL}/products/barcode/${barcode}`
  );

  const data = await response.json();

  if (!response.ok) {
    throw new Error(data.message || "Product not found");
  }

  return data;
}

