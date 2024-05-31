from flask import Flask, render_template, request, redirect, url_for
from database import connect_to_database, create_tables, add_user

app = Flask(__name__)

# Database connection
def get_db_connection():
    try:
        conn = connect_to_database()
        return conn
    except Exception as e:
        print("Error connecting to the database:", e)
        return None

# Create tables and add user
conn = get_db_connection()
if conn is not None:
    create_tables(conn)
    add_user(conn)
    conn.close()

# User authentication
def authenticate(username, password):
    conn = get_db_connection()
    if conn is not None:
        try:
            cur = conn.cursor()
            # Query the database to check if the user exists and the password matches
            cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cur.fetchone()
            if user:
                return True  # Authentication successful
        except Exception as e:
            print("Error authenticating user:", e)
        finally:
            cur.close()
            conn.close()
    return False  # Authentication failed

@app.route('/')
def index():
    return render_template('index.html')

# User authentication
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
    # Check if user is logged in
    # For testing purposes, always assume user is logged in
    logged_in = True
    if logged_in:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
