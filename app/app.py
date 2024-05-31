from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    products = get_products()
    return render_template('index.html', products=products)

@app.route('/login')
def login():
    # Implement login logic (placeholder for now)
    return "Login Page"

@app.route('/order')
def order():
    # Implement order logic (placeholder for now)
    return "Order Page"

if __name__ == '__main__':
    app.run(debug=True)
