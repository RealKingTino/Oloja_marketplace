from models import render_template, request, storage, app, redirect
from models.user import User
from models import text
from flask import jsonify

@app.route('/api')
def Home():
    return render_template('home.html')

@app.route('/api/signup/', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        payment = request.form['payment_info']
        user = User(user_name=username, email=email, password=password, shipping_address=address, payment_info=payment)

        storage.new(user)
        storage.save()
        return redirect('/')

    return render_template('signup.html')

@app.route('/api/login/', methods=["POST", "GET"])
def login():
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

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'user_id' in session:
        user_id = session['user_id']
        users = storage.all(User)
        for _user in users:
            if user.id == user_id:
                user = _user

        if user:
            if product_id in user.cart:
                user.cart[product_id] += 1
            else:
                user.cart[product_id] = 1

            storage.save()
            return redirect('/')
    
    return redirect('/login')

@app.route('/api/market', methods=["GET", "POST"])
def market():
    products = storage.all(Product)

    return jsonify([product.to_dict() for product in storage.all(Product).values()])
@app.route('/api/users', methods=["GET", "POST"])
@app.route('/api/users/<id>', methods=["GET", "POST"])
def user(id=None):
    if id is None:
        dic = [user.to_dict() for user in storage.all(User).values()]
        return jsonify(dic)
    else:
        return (storage.get(User, id).to_dict())


@app.route('/api/reviews', methods=["GET", "POST"])
def reviews():
    pass

@app.route('/api/carts', methods=["GET", "POST"])
def cart():
    pass

@app.route('/api/marketers', methods=["GET", "POST"])
def marketer():
    pass

@app.route('/api/orders', methods=["GET", "POST"])
def order():
    pass

@app.route('/api/categories', methods=["GET", "POST"])
def categories():
    pass
