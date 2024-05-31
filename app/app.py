from flask import Flask, render_template, request, redirect, url_for
from database import connect_to_database

app = Flask(__name__)

# Database connection
conn = connect_to_database()

# User authentication (you'll need to implement this)
def authenticate(username, password):
    # Authenticate user against database or any other method
    # Return True if authentication is successful, False otherwise
    # Example:
    # if username == "valid_username" and password == "valid_password":
    #     return True
    # else:
    #     return False
    return True  # For testing purposes, always return True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if authenticate(username, password):
            # Redirect to dashboard if authentication is successful
            return redirect(url_for('dashboard'))
        else:
            # Authentication failed, redirect back to login page
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Check if user is logged in (you'll need to implement this)
    # For testing purposes, always assume user is logged in
    logged_in = True
    if logged_in:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
