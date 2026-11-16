import pandas as pd

orders_data = {
    "order_id": ["1", "2", "3", "4", "5"],
    "customer_id": [101, 102, 101, 103, 104],
    "amount": [500, 600, 700, 300, 900]
}

orders_df = pd.DataFrame(orders_data)

# -------------------------
# Create customers.csv
# -------------------------
customers_data = {
    "customer_id": [101, 102, 103, 105],
    "name": ["Arun", "Priya", "Rahul", "Divya"],
    "city": ["Chennai", "Mumbai", "Chennai", "Bangalore"]
}

customers_df = pd.DataFrame(customers_data)

customers_df.to_csv("customers.csv", index=False)

print("Customers Data:")
print(customers_df)


# Inner Join

inner_join = pd.merge(
    orders_df,
    customers_df,
    on="customer_id",
    how="inner"
)

print("\nInner Join:")
print(inner_join)

# -------------------------
# Left Join
# -------------------------
left_join = pd.merge(
    customers_df,
    orders_df,
    on="customer_id",
    how="left"
)

print("\nLeft Join:")
print(left_join)

# Customers with no orders
no_orders = left_join[left_join["order_id"].isna()]

print("\nCustomers With No Orders:")
print(no_orders[["customer_id", "name"]])


# Outer Join

outer_join = pd.merge(
    orders_df,
    customers_df,
    on="customer_id",
    how="outer",
    indicator=True
)

print("\nOuter Join:")
print(outer_join)

# Orders without customer record
no_customer = outer_join[outer_join["_merge"] == "left_only"]

print("\nOrders Without Customer Record:")
print(no_customer[["customer_id", "order_id"]])