import psycopg2
# from psycopg2 import ExtrasCursor

# 1. Connection Configuration
# Replace these with the credentials you set up in Visual Studio
db_config = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "Ramsow@1813", # Replace with your actual password
    "port": "5432"
}

def manage_sales_data():
    conn = None
    try:
        # 2. Establish connection
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()

        print("Connected to PostgreSQL successfully!")

        # 3. Create a simple table
        cur.execute("""
            CREATE TABLE IF NOT EXISTS quick_sales (
                id SERIAL PRIMARY KEY,
                item_name VARCHAR(50),
                price DECIMAL(10, 2)
            );
        """)

        # 4. Insert data
        cur.execute("INSERT INTO quick_sales (item_name, price) VALUES (%s, %s)", ("Mechanical Keyboard", 89.99))
        cur.execute("INSERT INTO quick_sales (item_name, price) VALUES (%s, %s)", ("USB-C Cable", 15.50))

        # Commit changes
        conn.commit()
        print("Data inserted successfully into table.")

        # 5. Query the data
        cur.execute("SELECT * FROM quick_sales;")
        rows = cur.fetchall()

        print("\n--- Current Sales Inventory tabless ---")
        for row in rows:
            print(f"ID: {row[0]} | Item: {row[1]} | Price: ${row[2]}")

    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        # 6. Close the connection
        if conn:
            cur.close()
            conn.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    manage_sales_data()
# test comment