# 📊 Superstore Sales & Profitability Analysis

## 🎯 Project Objective
This project analyzes retail sales data to identify "profit leaks"—areas where the company is losing money despite high sales volume. The goal is to provide actionable insights for regional managers to optimize their discount strategies and shipping logistics.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Database:** PostgreSQL (Connected via SQLAlchemy & Psycopg2)
- **Libraries:** Pandas (Data Wrangling), Seaborn/Matplotlib (Visualization), Python-Dotenv (Security)
- **Environment:** Visual Studio Code

## 🚀 How to Run
1. Clone this repository.
2. Install dependencies:  
   `pip install -r requirements.txt`
3. Create a `.env` file in the root directory and add your database credentials:
   ```text
   DB_HOST=your_host
   DB_NAME=your_db
   DB_USER=your_user
   DB_PASS=your_password
4.Run the analysis:
   python analysis.py

📈 Key Insights
The Discount Trap: Analysis showed that discounts exceeding 20% lead to a net loss in 85% of cases.

Product Profitability: The "Tables" sub-category is the biggest profit drain due to high return rates and shipping costs.

Regional Performance: The West region outperformed all others in profit margin, while the Central region struggled with inefficient discounting.