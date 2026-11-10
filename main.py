# Banking Transaction Analytics using NoSQL
# College Project - Vellore
# Tools: Python, Pandas, NoSQL Concept, GitHub Actions

import pandas as pd
import os

print("=== BANKING TRANSACTION ANALYTICS ===")
print("College Project | NoSQL + Python + Power BI")

# MODULE 1: DATA COLLECTION
if not os.path.exists("data/transactions.csv"):
    os.makedirs("data", exist_ok=True)
    data = {
        'trans_id': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20],
        'merchant': ['Amazon','Flipkart','Swiggy','Amazon','DMart','Swiggy','Amazon','Zomato','Flipkart','DMart','Amazon','BigBasket','Swiggy','Myntra','DMart','Zomato','Amazon','Flipkart','Swiggy','DMart'],
        'category': ['shopping','shopping','food','shopping','grocery','food','shopping','food','shopping','grocery','shopping','grocery','food','shopping','grocery','food','shopping','shopping','food','grocery'],
        'amt': [1200,850,450,2000,1500,600,999,350,2500,1800,3200,1100,750,1800,2200,500,4500,1300,650,1900],
        'is_fraud': [0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0],
        'trans_date': ['2024-01-01','2024-01-02','2024-01-02','2024-01-03','2024-01-03','2024-01-04','2024-01-05','2024-01-05','2024-01-06','2024-01-06','2024-01-07','2024-01-07','2024-01-08','2024-01-08','2024-01-09','2024-01-09','2024-01-10','2024-01-10','2024-01-11','2024-01-11']
    }
    df = pd.DataFrame(data)
    df.to_csv("data/transactions.csv", index=False)
else:
    df = pd.read_csv("data/transactions.csv")

# MODULE 2: NOSQL STORAGE
nosql_db = df.to_dict('records')
print(f"\n[Module 2] NoSQL Storage: {len(nosql_db)} records stored")

# MODULE 3: ANALYTICS
print(f"\n[Module 3] Total Transactions: {len(df)}")
print(f"Total Amount: Rs.{df['amt'].sum()}")
print(f"Average: Rs.{df['amt'].mean():.2f}")

print("\n--- 1. Category Wise Spend ---")
cat_spend = df.groupby('category')['amt'].sum().sort_values(ascending=False)
print(cat_spend)

print("\n--- 2. Fraud Detection ---")
fraud = df[df['is_fraud']==1]
print(f"Fraud Count: {len(fraud)} / {len(df)}")
print(f"Fraud Amount: Rs.{fraud['amt'].sum()}")
print(f"Fraud %: {len(fraud)/len(df)*100:.1f}%")
print(fraud[['merchant','category','amt']])

print("\n--- 3. Top 5 Merchants ---")
print(df.groupby('merchant').size().sort_values(ascending=False).head(5))

print("\n--- 4. Daily Trend ---")
print(df.groupby('trans_date')['amt'].sum())

print("\n--- 5. High Value Transactions ---")
print(f"Amount > 2000: {len(df[df['amt']>2000])} transactions")

# MODULE 4: OUTPUT FOR POWER BI
os.makedirs("output", exist_ok=True)
cat_spend.to_csv("output/category_spend.csv")
df.groupby('merchant').size().to_csv("output/top_merchants.csv")
print("\n[Module 4] Output Saved to output/ folder")
print("=== PROJECT RUN SUCCESSFULLY ===")
