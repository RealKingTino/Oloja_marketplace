from views import app, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template("login.html")

"""
@app.route('/customer')
def customer():
    return render_template("customer/details.html")
"""

@app.route('/product')
def customer():
    return render_template("market.html")