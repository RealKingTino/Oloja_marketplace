from models import render_template, request, db, app, redirect
from models.user import User
from models import text

@app.route('/')
def Home():
    return render_template('home.html')

@app.route('/signup/', methods=["POST", "GET"])
def signup():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        address = request.form['address']
        payment = request.form['payment_info']
        user = User(user_name=username, email=email, password=password, shipping_address=address, payment_info=payment)

        db.session.add(user)
        db.session.commit()
        return redirect('/')

    return render_template('signup.html')

@app.route('/login/', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = db.session.query(User).filter(User.email == text("'" + email + "'")).first()
        print(user)
        if user.password == password:
            return render_template('account.html', user=user)
    return render_template('login.html')

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'user_id' in session:
        user_id = session['user_id']
        user = db.session.query(User).get(user_id)

        if user:
            if product_id in user.cart:
                user.cart[product_id] += 1
            else:
                user.cart[product_id] = 1

            db.session.commit()
            return redirect('/')
    
    return redirect('/login')

@app.route('/market')
def market():
    products = db.session.query(Product).all()
    return render_template('market.html', products=products)