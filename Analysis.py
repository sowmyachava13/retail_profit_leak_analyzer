import os
import pandas as pd 
from dotenv import load_dotenv
import urllib.parse
from sqlalchemy import create_engine


# 1. Define your credentials as strings
load_dotenv()
user = os.getenv('user')
password = urllib.parse.quote_plus(os.getenv('password')) # This handles the @ in your password
host = os.getenv('host')
port = os.getenv('port','5432')
database = os.getenv('database')# Ensure this matches your actual DB name in Postgres

# 2. Create the engine using the variables
engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{database}')

print("✅ Connection engine created successfully!")
query = "SELECT * FROM superstore_sales" # Make sure 'sales_data' is your table name
df = pd.read_sql_query(query, engine)

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
    #print("✅ Success! Data imported into 'superstore_sales' table.")
except Exception as e:
    print(f"❌ Error during import: {e}")
df=pd.read_sql_table('superstore_sales',engine)
# print(df.head())

import seaborn as sns
import matplotlib.pyplot as plt

# Set the visual style
sns.set_style("whitegrid")
custom_palette = sns.color_palette("viridis")

# 1. THE PERFORMANCE MATRIX: Sales vs Profit by Region
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='sales', y='profit', hue='region', size='discount', alpha=0.7)
plt.title('Profitability vs Sales Volume (Sized by Discount)')
plt.axhline(0, color='red', linestyle='--') # The "Break-even" line
plt.show()

# 2. THE CATEGORY DRILL-DOWN: Efficiency Check
# We calculate profit margin to see who is the most "efficient"
df['margin'] = (df['profit'] / df['sales']) * 100
plt.figure(figsize=(10, 5))
sns.barplot(data=df, x='category', y='margin', hue='category', palette='magma', errorbar=None, legend=False)
plt.title('Average Profit Margin % per Category')
plt.ylabel('Margin (%)')
plt.show()
plt.savefig('profit_analysis.png')
engine.dispose()
