#!/usr/bin/python3
"""module for api endpoint"""

from api.v1.views import app_views
from flask import jsonify, abort, request
from models.product import Product
from models import storage


@app_views.route('/products/', methods=['GET'])
def get_products():
    """Retrieves all product objects."""
    dic = ([product.to_dict() for product in storage.all(Product).values()])
    return jsonify(dic)


@app_views.route('/products/<id>', methods=['GET'])
def get_product(id):
    """Retrieves one product object."""
    obj = storage.get(Product, id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    """Deletes a product object."""
    obj = storage.get(Product, id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@app_views.route('/products/', methods=['POST'])
def create_product():
    """Creates a new product object."""
    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")

    if 'product_name' not in req:
        abort(400, "Missing product_name")

    new = Product(**req)
    storage.new(new)
    storage.save()
    return jsonify(new.to_dict()), 201


@app_views.route('/products/<id>', methods=['PUT'])
def update_product(id):
    """Updates a product object."""
    dic = request.get_json()
    obj = storage.get(Product, id)
    if obj is None:
        abort(404)

    if not dic:
        abort(400, "Not a JSON")

    for key, value in dic.items():
        if key not in ["created_at", "updated_at", "id"]:
            setattr(obj, key, value)
    obj.save()
    return jsonify(obj.to_dict()), 200
