import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===================================
# STEP 1: LOAD DATASET
# ===================================

df = pd.read_csv("Superstore.xlsx.csv", encoding="cp1252")

print("Dataset Shape:", df.shape)


# ===================================
# STEP 2: CHECK MISSING VALUES
# ===================================

print("\nMissing Values:")
print(df.isnull().sum())


# ===================================
# STEP 3: DATA CLEANING
# ===================================

# Convert Order Date to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])

# Create Year-Month column
df["Year-Month"] = df["Order Date"].dt.to_period("M").astype(str)

print("\nFirst 5 rows after cleaning:")
print(df[["Order Date", "Year-Month", "Sales", "Profit", "Discount"]].head())


# ===================================
# STEP 4: MONTHLY SALES ANALYSIS
# ===================================

monthly_sales = df.groupby("Year-Month")["Sales"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

# Highest sales month
highest_month = monthly_sales.idxmax()
highest_sales = monthly_sales.max()

print("\nHighest Sales Month:")
print(highest_month, "=", highest_sales)

# Lowest sales month
lowest_month = monthly_sales.idxmin()
lowest_sales = monthly_sales.min()

print("\nLowest Sales Month:")
print(lowest_month, "=", lowest_sales)


# ===================================
# STEP 5: MONTHLY SALES GRAPH
# ===================================

plt.figure(figsize=(14, 6))

sns.lineplot(
    x=monthly_sales.index,
    y=monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Year-Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("monthly_sales.png")

plt.show()


# ===================================
# STEP 6: CATEGORY-WISE SALES & PROFIT
# ===================================

category_analysis = df.groupby("Category")[["Sales", "Profit"]].sum()

print("\nCategory-wise Sales and Profit:")
print(category_analysis)

# Highest sales category
highest_sales_category = category_analysis["Sales"].idxmax()
highest_category_sales = category_analysis["Sales"].max()

print("\nHighest Sales Category:")
print(highest_sales_category, "=", highest_category_sales)

# Highest profit category
highest_profit_category = category_analysis["Profit"].idxmax()
highest_category_profit = category_analysis["Profit"].max()

print("\nHighest Profit Category:")
print(highest_profit_category, "=", highest_category_profit)


# ===================================
# CATEGORY SALES GRAPH
# ===================================

plt.figure(figsize=(8, 5))

sns.barplot(
    data=category_analysis.reset_index(),
    x="Category",
    y="Sales"
)

plt.title("Sales by Product Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("category_sales.png")

plt.show()

# ===================================
# STEP 7: REGION-WISE ANALYSIS
# ===================================

region_analysis = df.groupby("Region")[["Sales", "Profit"]].sum()

print("\nRegion-wise Sales and Profit:")
print(region_analysis)

# Highest sales region
highest_sales_region = region_analysis["Sales"].idxmax()
highest_region_sales = region_analysis["Sales"].max()

print("\nHighest Sales Region:")
print(highest_sales_region, "=", highest_region_sales)

# Highest profit region
highest_profit_region = region_analysis["Profit"].idxmax()
highest_region_profit = region_analysis["Profit"].max()

print("\nHighest Profit Region:")
print(highest_profit_region, "=", highest_region_profit)


# ===================================
# STEP 7B: CUSTOMER SEGMENT ANALYSIS
# ===================================

segment_analysis = df.groupby("Segment")[["Sales", "Profit"]].sum()

print("\nCustomer Segment Sales and Profit:")
print(segment_analysis)

# Highest sales segment
highest_sales_segment = segment_analysis["Sales"].idxmax()
highest_segment_sales = segment_analysis["Sales"].max()

print("\nHighest Sales Segment:")
print(highest_sales_segment, "=", highest_segment_sales)

# Highest profit segment
highest_profit_segment = segment_analysis["Profit"].idxmax()
highest_segment_profit = segment_analysis["Profit"].max()

print("\nHighest Profit Segment:")
print(highest_profit_segment, "=", highest_segment_profit)


# ===================================
# REGION SALES GRAPH
# ===================================

plt.figure(figsize=(8, 5))

sns.barplot(
    data=region_analysis.reset_index(),
    x="Region",
    y="Sales"
)

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()

plt.savefig("region_sales.png")

plt.show()

# ===================================
# STEP 8: DISCOUNT VS PROFIT ANALYSIS
# ===================================

plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df,
    x="Discount",
    y="Profit",
    alpha=0.5
)

plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")

plt.tight_layout()

plt.savefig("discount_vs_profit.png")

plt.show()

# ===================================
# STEP 9: DISCOUNT LEVEL ANALYSIS
# ===================================

discount_analysis = df.groupby("Discount")[["Sales", "Profit"]].sum()

print("\nDiscount-wise Sales and Profit:")
print(discount_analysis)

# Highest profit discount level
best_discount = discount_analysis["Profit"].idxmax()
best_discount_profit = discount_analysis["Profit"].max()

print("\nDiscount Level with Highest Profit:")
print(best_discount, "=", best_discount_profit)

# Lowest profit discount level
worst_discount = discount_analysis["Profit"].idxmin()
worst_discount_profit = discount_analysis["Profit"].min()

print("\nDiscount Level with Lowest Profit:")
print(worst_discount, "=", worst_discount_profit)