from models.user import User
from flask import jsonify, request
from models import storage
from api.v1.views import app_views


def login_user():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        users = storage.all(User)
        for user in users.values():
            if user.email == email and user.password == password:
                print(user)
                return render_template('account.html', user=user)
        return ("Incoirrect email or password")
    return render_template('login.html')
