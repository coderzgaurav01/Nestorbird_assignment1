
import psycopg2

# PostgreSQL credentials (update as needed)
DB_NAME = "assignment"
DB_USER = "postgres"
DB_PASSWORD = "1234ajay@"  # ← Change this to your actual password
DB_HOST = "localhost"
DB_PORT = "5432"

# Function to connect to PostgreSQL
def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

# Function to create the table if it doesn't exist
def create_table():
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS wiki_headings (
                id SERIAL PRIMARY KEY,
                tag TEXT,
                title TEXT
            )
        """)
        conn.commit()
    except Exception as e:
        print(f"[DB ERROR] Table creation failed: {e}")
    finally:
        conn.close()
