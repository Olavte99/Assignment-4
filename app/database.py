import psycopg2

def connect_to_database():
    """Connect to the PostgreSQL database."""
    try:
        conn = psycopg2.connect(
            dbname="your_database_name",
            user="your_username",
            password="your_password",
            host="localhost"
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

def create_tables():
    """Create necessary tables in the database."""
    conn = connect_to_database()
    if conn is not None:
        try:
            cur = conn.cursor()
            # Define SQL queries to create tables
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
            # Execute SQL queries
            cur.execute(create_table_users)
            cur.execute(create_table_orders)
            # Commit changes
            conn.commit()
            print("Tables created successfully.")
        except psycopg2.Error as e:
            print("Error creating tables:", e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Database connection failed.")

def add_user():
    """Add a new user to the database."""
    conn = connect_to_database()
    if conn is not None:
        try:
            cur = conn.cursor()
            # Define user data
            username = "admin"
            password = "admin"
            # Define SQL query to insert user
            insert_user_query = """
                INSERT INTO users (username, password)
                VALUES (%s, %s)
            """
            # Execute SQL query with user data
            cur.execute(insert_user_query, (username, password))
            # Commit the transaction
            conn.commit()
            print("User added successfully.")
        except psycopg2.Error as e:
            print("Error adding user:", e)
        finally:
            cur.close()
            conn.close()
    else:
        print("Database connection failed.")

if __name__ == "__main__":
    create_tables()  # Create tables when executed directly
    add_user()       # Add a user when executed directly
