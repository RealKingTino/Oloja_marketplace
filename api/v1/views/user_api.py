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
    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")

    if 'name' not in req:
        abort("Missing name")
    if 'password' not in req:
        abort("Missing password")
    if 'email' not in req:
        abort("Missing email")

    users = storage.all(User).value()
    for user in users:
        if user.email == req['email']:
            abort("Email already in use")

    new = User(**req)
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
        if key != "created_at" and key != "updated_at" and key != "id":
            setattr(obj, key, value)
    storage.save()
    return jsonify(obj.to_dict()), 200
