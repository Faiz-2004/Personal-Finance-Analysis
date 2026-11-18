# Power BI Dashboard Creation Guide: Personal Finance & Expense Analysis

---

## 1. Overview & Setup Prerequisites

This step-by-step guide walks you through building the interactive **"Personal Finance and Expense Analysis Dashboard"** in **Power BI Desktop**.

### Source Data Files:
- `Dataset/transactions.csv` (Primary Fact Table)
- `Dataset/monthly_budget.csv` (Budget Target Table)

---

## 2. Step 1: Data Import & Power Query Transformation

1. Open **Power BI Desktop**.
2. Click **Get Data** > **Text/CSV**.
3. Select and import `Dataset/transactions.csv`:
   - Click **Transform Data** to open Power Query.
   - Verify data types:
     - `Transaction_ID`: Text
     - `Date`: Date (`yyyy-mm-dd`)
     - `Description`: Text
     - `Category`: Text
     - `Type`: Text (`Income` / `Expense`)
     - `Amount`: Decimal Number / Fixed Decimal (Currency)
     - `Payment_Method`: Text
     - `Account_Type`: Text
     - `Month`: Text
     - `Year`: Whole Number
   - Rename query to: `Transactions`.
4. Import `Dataset/monthly_budget.csv`:
   - In Power Query, click **New Source** > **Text/CSV**.
   - Select `monthly_budget.csv`.
   - Verify data types:
     - `Month`: Text
     - `Category`: Text
     - `Budget_Amount`: Decimal Number / Currency
   - Rename query to: `Monthly_Budget`.
5. Click **Close & Apply**.

---

## 3. Step 2: Create Date Dimension & Data Modeling

### 3.1 Create Calculated Calendar Table
In Power BI Desktop, navigate to the **Modeling** tab, select **New Table**, and enter:

```dax
Calendar = 
ADDCOLUMNS(
    CALENDAR(DATE(2026, 1, 1), DATE(2026, 12, 31)),
    "Year", YEAR([Date]),
    "Month Number", MONTH([Date]),
    "Month", FORMAT([Date], "MMMM"),
    "Month Short", FORMAT([Date], "MMM"),
    "MonthYear", FORMAT([Date], "yyyy-MM"),
    "Quarter", "Q" & FORMAT([Date], "Q")
)
```

**Important**: Select the column `Month` in the `Calendar` table, go to **Column Tools** > **Sort by Column** and choose **Month Number**. This ensures charts sort months chronologically (January to December) instead of alphabetically.

### 3.2 Establish Relationships (Data Model)
Navigate to the **Model View** tab:
1. Drag `Calendar[Date]` to `Transactions[Date]` (Relationship: `1-to-Many (1:*)`, Single direction).
2. For linking Budget:
   - You can connect `Calendar[Month]` to `Monthly_Budget[Month]` (Many-to-Many relationship or via a dedicated Month Dimension / Inactive bridge).
   - Alternatively, keep `Monthly_Budget` linked via Category bridge table, or create measure comparisons grouped by `Category` and `Month`.

---

## 4. Step 3: Create DAX Measures

In the **Modeling** tab, select **New Measure** on the `Transactions` table and add the measures below (also available in [dax_measures.txt](file:///d:/parvam%20training/data_analytics/personal_finance/PowerBI/dax_measures.txt)):

```dax
Total Income = 
CALCULATE(
    SUM(Transactions[Amount]),
    Transactions[Type] = "Income"
)
```

```dax
Total Expenses = 
CALCULATE(
    SUM(Transactions[Amount]),
    Transactions[Type] = "Expense"
)
```

```dax
Total Savings = 
[Total Income] - [Total Expenses]
```

```dax
Savings Rate = 
DIVIDE([Total Savings], [Total Income], 0) * 100
```

```dax
Average Monthly Expenses = 
AVERAGEX(
    VALUES('Calendar'[MonthYear]),
    [Total Expenses]
)
```

```dax
Total Budget = 
SUM(Monthly_Budget[Budget_Amount])
```

```dax
Budget Variance = 
[Total Budget] - [Total Expenses]
```

---

## 5. Step 4: Canvas Layout & Theme Settings

### Theme & Colors:
- **Canvas Background**: Light Gray (`#F8F9FA` or `#F4F6F9`).
- **Cards/Containers**: White background (`#FFFFFF`) with 8px corner radius and subtle shadow.
- **Header Banner**: Dark Navy Blue (`#0F2537`).
- **Income & Savings Palette**: Forest Green (`#2E7D32`), Mint (`#A5D6A7`).
- **Expense Palette**: Crimson Red (`#C62828`), Coral (`#E57373`).
- **Neutral / Accent**: Royal Blue (`#1565C0`), Slate Grey (`#546E7A`).

---

## 6. Step 5: Visualizations & Slicers Layout

### 6.1 Header Section
- **Title Text Box**: "Personal Finance and Expense Analysis Dashboard" (Font: Segoe UI Bold, 20pt, Dark Blue).
- **Subtitle Text Box**: "Annual Cash Flow, Expense Distribution, and Budget Performance Monitoring (2026)".

### 6.2 Top Slicers Row
Create Horizontal / Dropdown Slicers:
1. `Calendar[Year]`
2. `Calendar[Month]`
3. `Transactions[Category]`
4. `Transactions[Type]`
5. `Transactions[Payment_Method]`

### 6.3 KPI Cards Row (5 Cards)
Place 5 single-value **Card** or **New Card** visuals:
1. **Total Income**: Measure = `[Total Income]`, Display Unit = Thousands/Lakhs, Text Color = Green (`#2E7D32`).
2. **Total Expenses**: Measure = `[Total Expenses]`, Display Unit = Thousands/Lakhs, Text Color = Red (`#C62828`).
3. **Total Savings**: Measure = `[Total Savings]`, Display Unit = Thousands/Lakhs, Text Color = Dark Green.
4. **Savings Rate**: Measure = `[Savings Rate]`, Format = `0.0%`, Text Color = Blue (`#1565C0`).
5. **Avg Monthly Expenses**: Measure = `[Average Monthly Expenses]`, Display Unit = Thousands, Text Color = Charcoal (`#37474F`).

### 6.4 Core Visuals Matrix (Grid of Charts)

| Visual # | Chart Type | Fields Configuration | Formatting Notes |
| :--- | :--- | :--- | :--- |
| **Visual 1** | **Line Chart** | X-Axis: `Calendar[Month]`<br>Y-Axis: `[Total Income]`, `[Total Expenses]` | Green line for Income, Red line for Expenses. Markers turned ON. |
| **Visual 2** | **Donut Chart** | Legend: `Transactions[Category]`<br>Values: `[Total Expenses]` | Filter visual to `Type = Expense`. Show Percent of Total in data labels. |
| **Visual 3** | **Clustered Column Chart** | X-Axis: `Calendar[Month]`<br>Y-Axis: `[Total Expenses]` | Dark Blue columns with data labels on top. |
| **Visual 4** | **Line Chart** | X-Axis: `Calendar[Month]`<br>Y-Axis: `[Total Savings]` | Emerald Green line with average reference line. |
| **Visual 5** | **Clustered Bar Chart** | Y-Axis: `Monthly_Budget[Category]`<br>X-Axis: `[Total Budget]`, `[Total Expenses]` | Dual bar comparing Budget vs Actual side-by-side. |
| **Visual 6** | **Donut Chart** | Legend: `Transactions[Payment_Method]`<br>Values: `[Total Expenses]` | Color distinct payment methods (UPI, Credit Card, etc.). |
| **Visual 7** | **Bar Chart** | Y-Axis: `Transactions[Category]`<br>X-Axis: `[Total Expenses]` | Ranked from highest expense to lowest. |

---

## 7. Step 6: Testing & Interactivity Verification

1. **Cross-Filtering**: Clicking on any category in the Donut Chart (e.g., `Shopping`) should filter the monthly expense trend and payment methods used for shopping.
2. **Month Slicer**: Selecting `March` should dynamically update all KPI cards, budget variance, and method breakdowns for March 2026.
3. **Payment Method Filter**: Filtering by `UPI` should isolate daily retail groceries, food, and utility transactions.

---

## 8. Summary of Deliverables in PowerBI/

- [dax_measures.txt](file:///d:/parvam%20training/data_analytics/personal_finance/PowerBI/dax_measures.txt)
- [PowerBI_Dashboard_Guide.md](file:///d:/parvam%20training/data_analytics/personal_finance/PowerBI/PowerBI_Dashboard_Guide.md)
