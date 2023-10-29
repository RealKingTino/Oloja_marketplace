#!/usr/bin/python3
"""this module handles all default RESTFul API actions for the Marketer"""
from api.v1.views import app_views
from flask import jsonify, abort, request
from models.marketer import Marketer
from models import storage


@app_views.route('/marketers/', methods=['GET'])
def get_marketer():
    """retrieves all Marketer objects"""
    dic = ([marketer.to_dict() for marketer in storage.all(Marketer).values()])
    return (jsonify(dic))


@app_views.route('/marketers/<id>', methods=['GET'])
def get_marketers(id):
    """retrieves one marketer object"""
    obj = storage.get(Marketer, id)
    if obj is None:
        abort(404)
    return jsonify(obj.to_dict())


@app_views.route('/marketers/<id>', methods=['DELETE'])
def delete_marketer(id):
    """deletes a marketer object"""
    obj = storage.get(Marketer, id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return (jsonify({}), 200)


@app_views.route('/marketers/', methods=['POST'])
def create_marketer():
    """create a new marketer object"""
    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")

    if 'name' not in req:
        abort("Missing name")
    if 'password' not in req:
        abort("Missing password")
    if 'email' not in req:
        abort("Missing email")

    marketers = storage.all(Marketer).value()
    for marketer in marketers:
        if marketer.email == req['email']:
            abort("Email already in use")

    new = Marketer(**req)
    storage.new(new)
    storage.save()

    return (jsonify(new.to_dict()), 201)


@app_views.route('/marketers/<id>', methods=['PUT'])
def update_marketer(id):
    """update marketer object"""
    dic = request.get_json()
    obj = storage.get(Marketer, id)
    if obj is None:
        abort(404)

    if not dic:
        abort(400, "Not a JSON")
    for key, value in dic.items():
        if key not in ["created_at", "updated_at", "id"]:
            setattr(obj, key, value)
    obj.save()
    return jsonify(obj.to_dict()), 200
