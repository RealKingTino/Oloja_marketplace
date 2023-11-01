#!/usr/bin/python3
"""this module handles all default RESTFul API actions for the Order"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User
from models import storage


@app_views.route('/orders/', methods=['GET'])
def get_orders():
    """retrieves all orders objects"""
    dic = ([order.to_dict() for order in storage.all(Order).values()])
    return (jsonify(dic))


@app_views.route('/orders/<id>', methods=['GET'])
def get_order(id):
    """retrieves one orders object"""
    obj = storage.get(Orders, id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/orders/<id>', methods=['DELETE'])
def delete_order(id):
    """deletes a Order object"""
    obj = storage.get(Order, id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/orders/', methods=['POST'])
def create_order():
    """create a new Order object"""
    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")

    if 'products' not in req:
        abort("Missing products")

    new = Order(**req)
    storage.new(new)
    storage.save()

    return (jsonify(new.to_dict()), 201)


@app_views.route('/order/<id>', methods=['PUT'])
def update_order(id):
    """update Order object"""
    dic = request.get_json()
    obj = storage.get(Order, id)
    if obj is None:
        abort(404)

    if not dic:
        abort(400, "Not a JSON")
    for key, value in dic.items():
        if key not in ["created_at", "updated_at", "id"]:
            setattr(obj, key, value)
    obj.save()
    return jsonify(obj.to_dict()), 200
