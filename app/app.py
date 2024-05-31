from flask import Flask, render_template, request, redirect, url_for
from database import connect_to_database, create_tables, add_user, authenticate

app = Flask(__name__)

# Database connection
conn = connect_to_database()

# Create tables and add user when the application starts
create_tables(conn)
add_user(conn)

def index():
    users = get_users()
    return render_template('index.html', users=users)

@app.route('/')
def index():
    return render_template('index.html')

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
    logged_in = True
    if logged_in:
        return render_template('dashboard.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
