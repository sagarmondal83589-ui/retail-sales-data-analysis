# Data Analytics & AI Internship Project
# Project: Retail Sales Analysis and Customer Insights
# Dataset: Synthetic retail sales dataset created for educational/project demonstration.

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("retail_sales_dataset.csv")
df["Date"] = pd.to_datetime(df["Date"])

print("Dataset shape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())
print("\nSummary statistics:\n", df.describe())

product_sales = df.groupby("Product")["Sales"].sum().sort_values(ascending=False)
region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Sales"].sum()

print("\nSales by product:\n", product_sales)
print("\nSales by region:\n", region_sales)
print("\nMonthly sales:\n", monthly_sales)

print("\nTotal sales: ₹{:,.2f}".format(df["Sales"].sum()))
print("Average order value: ₹{:,.2f}".format(df["Sales"].mean()))
print("Total units sold:", df["Quantity"].sum())
print("Top product:", product_sales.index[0])
print("Top region:", region_sales.index[0])

# Visualizations
product_sales.plot(kind="bar", title="Sales by Product")
plt.ylabel("Sales (INR)")
plt.tight_layout()
plt.show()

region_sales.plot(kind="bar", title="Sales by Region")
plt.ylabel("Sales (INR)")
plt.tight_layout()
plt.show()

monthly_sales.plot(marker="o", title="Monthly Sales Trend")
plt.ylabel("Sales (INR)")
plt.tight_layout()
plt.show()
