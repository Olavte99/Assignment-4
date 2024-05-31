from flask import Flask, render_template, request, redirect, url_for
from database import connect_to_database, create_tables, add_user, authenticate

app = Flask(__name__)
conn = connect_to_database()

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
    """Authenticate user."""
    print("Authenticating user:", username)
    conn = connect_to_database()
    if conn is not None:
        try:
            cur = conn.cursor()
            # Query the database to check if the user exists and the password matches
            cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cur.fetchone()
            if user:
                print("Authentication successful for user:", username)
                return True  # Authentication successful
            else:
                print("Authentication failed for user:", username)
        except psycopg2.Error as e:
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
        print("Login attempt for user:", username)
        if authenticate(username, password):
            print("Redirecting to dashboard for user:", username)
            return redirect(url_for('dashboard'))
        else:
            print("Login failed for user:", username)
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
