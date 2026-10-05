export function validateProduct(product) {

  if (!product.product_name) {
    return "Product name is required";
  }

  if (!product.barcode) {
    return "Barcode is required";
  }

  if (!product.categories) {
    return "Category is required";
  }

  if (product.price === "" || product.price < 0) {
    return "Price must be a valid number";
  }

  if (product.quantity === "" || product.quantity < 0) {
    return "Quantity must be a valid number";
  }

  return null;
}
