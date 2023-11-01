#!/usr/bin/python3
"""this module handles all default RESTFul API actions for the Category"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.category import Category
from models import storage


@app_views.route('/categories/', methods=['GET'])
def get_categories():
    """retrieves all Category objects"""
    dic = ([category.to_dict() for category in storage.all(Category).values()])
    return (jsonify(dic))


@app_views.route('/categories/<id>', methods=['GET'])
def get_category(id):
    """retrieves one Category object"""
    obj = storage.get(Category, id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/categories/<id>', methods=['DELETE'])
def delete_categories(id):
    """deletes a Category object"""
    obj = storage.get(Category, id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/categories/', methods=['POST'])
def create_category():
    """create a new Category object"""
    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")

    if 'name' not in req:
        abort("Missing name")

    new = Category(**req)
    storage.new(new)
    storage.save()

    return (jsonify(new.to_dict()), 201)


@app_views.route('/categories/<id>', methods=['PUT'])
def update_category(id):
    """update Category object"""
    dic = request.get_json()
    obj = storage.get(Category, id)
    if obj is None:
        abort(404)

    if not dic:
        abort(400, "Not a JSON")
    for key, value in dic.items():
        if key not in ["created_at", "updated_at", "id"]:
            setattr(obj, key, value)
    obj.save()
    return jsonify(obj.to_dict()), 200
