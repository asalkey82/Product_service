from flask import Flask, jsonify, request
app = Flask(__name__)

products = [
    {"id": 1, "name": "banana", "price": 0.23, "quantity": 5},
    {"id": 2, "name": "apple", "price": 0.25, "quantity": 10},
    {"id": 3, "name": "beef", "price": 8.00, "quantity": 9}
]


BASE_URL = "https://carl-mart.onrender.com"

@app.route(f'{BASE_URL}/products', methods=['GET'])
def get_products():
    return jsonify({"products": products})
    
@app.route(f'{BASE_URL}/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        if product["quantity"] != 0:
            return jsonify({"product": product})
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route(f'{BASE_URL}/products', methods=['POST'])
def add_products():
    new_product = {
        "id": len(products) + 1,
        "name": request.json.get('name'),
        "price": request.json.get('price'),
        "quantity": request.json.get('quantity')
    }
    products.append(new_product)
    return jsonify({"message": "Product added", "product": new_product}), 201

@app.route(f'{BASE_URL}/remove/<int:product_id>', methods=['POST'])
def remove_quantity(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        products[product_id-1]['quantity'] -= 1
        return jsonify({"message": "Product added to cart"})

@app.route(f'{BASE_URL}/add/<int:product_id>', methods=['POST'])
def add_quantity(product_id):
    product = next((product for product in products if product["id"] == product_id), None)
    if product:
        products[product_id-1]['quantity'] += 1
        return jsonify({"message": "Product put back"}) 

if __name__ == '__main__':
    app.run(debug=True)
