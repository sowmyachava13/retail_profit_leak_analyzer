import pandas as pd 
import urllib.parse
from sqlalchemy import create_engine


# 1. Define your credentials as strings
user = 'postgres'
password = urllib.parse.quote_plus('Ramsow@1813') # This handles the @ in your password
host = '127.0.0.1'
port = '5432'
database = 'postgres' # Ensure this matches your actual DB name in Postgres

# 2. Create the engine using the variables
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

print("✅ Connection engine created successfully!")
# 1. Load the data
df = pd.read_csv(r'C:\SalesDashboard\RetailOrders_SuperStore.csv')

# 2. RENAME HYPHENS TO UNDERSCORES
# This changes 'sub-category' to 'sub_category' automatically
df.columns = [c.replace('-', '_').replace(' ', '_').lower() for c in df.columns]

# 3. Proceed with date cleaning and export
df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
df['ship_date'] = pd.to_datetime(df['ship_date'], errors='coerce')

# Use 'replace' for the first run to ensure columns match exactly
df.to_sql('superstore_sales', engine, if_exists='replace', index=False)

# 3. PUSH TO TABLE
try:
    # Use if_exists='append' if you want to keep the current empty table structure
    df.to_sql('superstore_sales', engine, if_exists='append', index=False)
    print("✅ Success! Data imported into 'superstore_sales' table.")
except Exception as e:
    print(f"❌ Error during import: {e}")