#!/usr/bin/python3
"""this module handles all default RESTFul API actions for the User"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.user import User
from models import storage


@app_views.route('/users/', methods=['GET'])
def get_users():
    """retrieves all User objects"""
    dic = ([user.to_dict() for user in storage.all(User).values()])
    return (jsonify(dic))


@app_views.route('/users/<id>', methods=['GET'])
def get_user(id):
    """retrieves one User object"""
    obj = storage.get(User, id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    """deletes a User object"""
    obj = storage.get(User, id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/users/', methods=['POST'])
def create_user():
    """create a new user object"""
    if not request.get_json():
        abort(400, "Not a JSON")

    if 'name' not in request.get_json():
        abort("Missing name")

    new = User()
    new.name = request.get_json()['name']
    storage.new(new)
    storage.save()

    return (jsonify(new.to_dict()), 201)


@app_views.route('/users/<id>', methods=['PUT'])
def update_user(id):
    """update user object"""
    dic = request.get_json()
    obj = storage.get(User, id)
    if obj is None:
        abort(404)

    if not dic:
        abort(400, "Not a JSON")
    for key, value in dic.items():
        if key is not "created_at" and key is not "updated_at":
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict()), 200
