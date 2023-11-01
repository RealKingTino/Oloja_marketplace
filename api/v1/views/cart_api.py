#!/usr/bin/python3
"""module for cart endpoint"""

from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.user import User
from models.cart import Cart


@app_views.route('/users/<user_id>/cart', methods=['GET'])
def get_cart_linked_to_user(user_id):
    """ get information for cart """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    cart = [cart.to_dict() for cart in user.cart]
    return jsonify(cart)


@app_views.route('/carts/<cart_id>', methods=['GET'])
def get_cart(city_id):
    """ get information for all cart """
    cart = storage.get(Cart, cart_id)
    if cart is None:
        abort(404)
    return jsonify(cart.to_dict())


@app_views.route('/carts/<cart_id>', methods=['DELETE'])
def delete_cart(cart_id):
    """ delete cart base on cart_id """
    cart = storage.get(Cart, cart_id)
    if cart is None:
        abort(404)
    storage.delete(cart)
    storage.save()
    return jsonify({}), 200


@app_views.route('/users/<users_id>/carts', methods=['POST'])
def create_cart(user_id):
    """ create new city """
    user = storage.get(User, user_id)
    if user is None:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    data['user_id'] = user_id
    new_cart = Cart(**data)
    new_cart.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/carts/<cart_id>', methods=['PUT'])
def update_cart(city_id):
    """ update cart """
    cart = storage.get(Cart, cart_id)
    if cart is None:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(cart, key, value)
    cart.save()
    return jsonify(cart.to_dict()), 200
