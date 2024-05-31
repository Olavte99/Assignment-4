from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

# Database connection
conn = psycopg2.connect(
    dbname="your_database_name",
    user="your_username",
    password="your_password",
    host="localhost"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        # Authenticate user
        # Redirect to dashboard if login successful
        return redirect(url_for('dashboard'))
    return render_template('login.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        # Handle order submission
        # Insert order into database
        return redirect(url_for('order_confirmation'))
    return render_template('order.html')

@app.route('/order_confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
