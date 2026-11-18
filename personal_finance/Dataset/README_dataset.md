# Dataset Documentation: Personal Finance and Expense Analysis

> **IMPORTANT DISCLAIMER**: The datasets in this directory (`transactions.csv` and `monthly_budget.csv`) are 100% **synthetic sample data** generated programmatically for academic, instructional, and portfolio demonstration purposes. They do **not** represent actual personal financial records of any real individual or entity.

---

## 1. Overview

The dataset simulates a complete year (January 1, 2026 to December 31, 2026) of personal income, expenses, and budgetary allocations for a working professional in India. All monetary figures are denominated in **Indian Rupees (INR - ₹)**.

---

## 2. Dataset Files

### A. `transactions.csv`
Contains 364 detailed transactions spanning the calendar year 2026.

| Column Name | Data Type | Description | Sample Value |
| :--- | :--- | :--- | :--- |
| `Transaction_ID` | String / Text | Unique identifier for each transaction | `TXN00001` |
| `Date` | Date (`YYYY-MM-DD`)| Date when transaction occurred | `2026-01-02` |
| `Description` | String / Text | Detailed narrative / purpose of transaction | `Monthly Corporate Salary Credit` |
| `Category` | String / Text | Financial category of the entry | `Salary`, `Food`, `Rent` |
| `Type` | Categorical | Entry direction: `Income` or `Expense` | `Income` / `Expense` |
| `Amount` | Float | Transaction value in INR (₹) | `80000.00` |
| `Payment_Method`| Categorical | Instrument used: `UPI`, `Debit Card`, `Credit Card`, `Net Banking`, `Cash` | `UPI` |
| `Account_Type` | Categorical | Source account: `Salary Account`, `Savings Account`, `Credit Card Account`, `Cash Wallet` | `Salary Account` |
| `Month` | Categorical | Month name (`January` to `December`) | `January` |
| `Year` | Integer | Calendar year | `2026` |

#### Categories Covered:
- **Income (5)**:
  - `Salary` (Primary monthly paycheck)
  - `Freelance` (Consulting and freelance project earnings)
  - `Business Income` (Side business revenues)
  - `Interest` (Fixed deposit and savings account interest)
  - `Other Income` (Affiliate and digital asset sales)
- **Expenses (13)**:
  - `Food` (Dining, restaurants, food delivery)
  - `Rent` (Monthly residential apartment rent)
  - `Transportation` (Fuel, metro, auto, cab commutes)
  - `Shopping` (Apparel, personal accessories, electronics)
  - `Electricity` (Monthly state utility power bills)
  - `Internet` (Fiber optic broadband subscription)
  - `Healthcare` (Pharmacy, health checkups, dental visits)
  - `Education` (Certifications, educational books, learning tools)
  - `Entertainment` (Cinema, streaming subscriptions, events)
  - `Groceries` (Supermarket, pantry, daily provisions)
  - `EMI` (Equated Monthly Installment for car loan)
  - `Travel` (Interstate vacations, flights, hotels)
  - `Other Expenses` (Repairs, home maintenance, laundry)

---

### B. `monthly_budget.csv`
Contains planned monthly budget limits for all 13 expense categories for each month of the year (12 months × 13 categories = 156 records).

| Column Name | Data Type | Description | Sample Value |
| :--- | :--- | :--- | :--- |
| `Month` | Categorical | Calendar month name | `January` |
| `Category` | Categorical | Expense category being budgeted | `Rent` |
| `Budget_Amount` | Float | Allocated budget cap in INR (₹) | `20000.00` |

---

## 3. Data Integrity & Reproducibility
- Generated using Python script `Dataset/generate_data.py`.
- Employs fixed pseudo-random seeds (`seed=42`) ensuring complete reproducibility.
- Zero duplicate `Transaction_ID` values.
- Clean formatting without missing values or negative amounts.
