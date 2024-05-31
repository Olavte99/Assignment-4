import psycopg2

def connect_to_database():
    """Connect to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname="A_db-name",
            user="A_user",
            password="A_password",
            host="DB_HOSTNAME",
            port="5432"
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

def create_tables(conn):
    """Create necessary tables in the database."""
    if conn is not None:
        try:
            cur = conn.cursor()
            create_table_users = """
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(100) NOT NULL
                )
            """
            create_table_orders = """
                CREATE TABLE IF NOT EXISTS orders (
                    id SERIAL PRIMARY KEY,
                    user_id INTEGER REFERENCES users(id),
                    product VARCHAR(100) NOT NULL,
                    quantity INTEGER NOT NULL,
                    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """
            cur.execute(create_table_users)
            cur.execute(create_table_orders)
            conn.commit()
            print("Tables created successfully.")
        except psycopg2.Error as e:
            print("Error creating tables:", e)
        finally:
            cur.close()

def add_user(conn):
    """Add a new user to the database."""
    if conn is not None:
        try:
            cur = conn.cursor()
            username = "admin"
            password = "admin"
            insert_user_query = """
                INSERT INTO users (username, password)
                VALUES (%s, %s)
                ON CONFLICT (username) DO NOTHING
            """
            cur.execute(insert_user_query, (username, password))
            conn.commit()
            print("User added successfully or already exists.")
        except psycopg2.Error as e:
            print("Error adding user:", e)
        finally:
            cur.close()

def authenticate(username, password):
    """Authenticate user."""
    conn = connect_to_database()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
            user = cur.fetchone()
            if user:
                return True  # Authentication successful
        except psycopg2.Error as e:
            print("Error authenticating user:", e)
        finally:
            cur.close()
            conn.close()
    return False  # Authentication failed

def get_users():
    """Fetch all users from the database."""
    conn = connect_to_database()
    if conn is not None:
        try:
            cur = conn.cursor()
            cur.execute("SELECT username FROM users")
            users = cur.fetchall()
            return [user[0] for user in users]
        except psycopg2.Error as e:
            print("Error fetching users:", e)
            return []
        finally:
            cur.close()
            conn.close()
    return []
