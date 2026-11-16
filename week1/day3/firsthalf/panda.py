import pandas as pd
# Create orders.csv
data = """order_id,customer_id,amount
1,101,500
2,102,
3,101,700
3,101,700
4,103,300
5,104,900
"""

with open("./orders.csv", "w") as file:
    file.write(data)

# Load CSV
df = pd.read_csv("orders.csv")

print("Original Data:")
print(df)

# Find missing values
print("\nMissing Values:")
print(df.isna().sum())

# Find duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated())

# Remove duplicates
df = df.drop_duplicates()

# Convert amount to numeric
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

# Fill missing amount with median
median_amount = df["amount"].median()
df["amount"] = df["amount"].fillna(median_amount)

# Make order_id a string
df["order_id"] = df["order_id"].astype(str)

print("\nCleaned Data:")
print(df)

# Group by customer_id
result = df.groupby("customer_id").agg(
    total=("amount", "sum"),
    orders=("order_id", "count")
)

print("\nCustomer Summary:")
print(result)