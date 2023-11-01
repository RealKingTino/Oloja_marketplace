from models.user import User
from flask import jsonify
from api.v1.views import app_views


def signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        payment = request.form['payment_info']
        user = User(user_name=username, email=email, password=password, shipping_address=address, payment_info=payment)
        from api.models import storage

        storage.new(user)
        storage.save()
        return (jsonify(user.to_dict()))

    return render_template('signup.html')
