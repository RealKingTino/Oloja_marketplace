#!/usr/bin/python3
"""module for review endpoint"""

from api.v1.views import app_views
from flask import jsonify, request, abort
from models import storage
from models.product import Product
from models.review import Review


@app_views.route('/products/<review_id>/cart', methods=['GET'])
def get_review_linked_to_product(user_id):
    """ get information for review """
    product = storage.get(Product, product_id)
    if product is None:
        abort(404)
    reviews = [review.to_dict() for review in product.reviews]
    return jsonify(cart)


@app_views.route('/reviews/<review_id>', methods=['GET'])
def get_review(review_id):
    """ get information for all review """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route('/reviews/<reviews_id>', methods=['DELETE'])
def delete_review(review_id):
    """ delete review base on review_id """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 200


@app_views.route('/products/<product_id>/reviews', methods=['POST'])
def create_review(user_id):
    """ create new review """
    product = storage.get(Product, product_id)
    if product is None:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    data['product_id'] = product_id
    new_review = review(**data)
    new_review.save()
    return jsonify(new_city.to_dict()), 201


@app_views.route('/review/<review_id>', methods=['PUT'])
def update_review(review_id):
    """ update review """
    review = storage.get(Review, review_id)
    if review is None:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, 'Not a JSON')
    for key, value in data.items():
        if key not in ['id', 'state_id', 'created_at', 'updated_at']:
            setattr(review, key, value)
    review.save()
    return jsonify(cart.to_dict()), 200
