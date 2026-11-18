# Personal Finance and Expense Analysis Using Python and Power BI

[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-orange.svg)](https://pandas.pydata.org/)
[![Power BI Desktop](https://img.shields.io/badge/Power_BI-Desktop-yellow.svg)](https://powerbi.microsoft.com/)
[![Kernel](https://img.shields.io/badge/Jupyter_Kernel-finance--analysis-green.svg)](https://jupyter.org/)

---

## 1. Project Introduction

**"Personal Finance and Expense Analysis Using Python and Power BI"** is an end-to-end, beginner-friendly yet professionally architected data analytics project. It provides an automated analytical workflow to track, clean, explore, visualize, and budget personal finances across digital payment channels (UPI, Credit Cards, Net Banking, Debit Cards, and Cash) using **Indian Rupees (INR - ₹)**.

The project seamlessly bridges **Python exploratory data analysis (EDA)** in Jupyter Notebook with an enterprise-grade **Power BI Business Intelligence Dashboard** architecture.

> **DISCLAIMER**: All transaction and budget records provided in this repository are **programmatically generated synthetic sample data** created for academic demonstration, learning, and portfolio presentation.

---

## 2. Project Objectives

- Ingest, validate, and audit a year-long personal financial transaction ledger (Jan 2026 – Dec 2026).
- Perform data cleaning, type casting, schema consistency checks, and outlier detection.
- Compute fundamental personal finance KPIs: **Total Income, Total Expenses, Net Savings, Savings Rate (%), and Average Monthly Expenses**.
- Benchmark actual category outflows against planned monthly budgets to identify overruns.
- Render and export publication-ready statistical visualizations with Matplotlib & Seaborn.
- Provide a full blueprint for building an interactive **Power BI Desktop Dashboard** with a Date Dimension and DAX measures.

---

## 3. Key Features

- **Automated Virtual Environment**: One-click batch scripts (`setup_venv.bat` and `run_notebook.bat`) for isolated dependencies and automated Jupyter kernel registration.
- **Reproducible Data Generation**: Parameterized Python generator (`generate_data.py`) with fixed pseudo-random seeds.
- **Thorough Jupyter Notebook**: 8 systematically organized sections with rich Markdown documentation, formulas, and code comments.
- **Seven Core Visual Analytics**: Line charts, donut distributions, trend columns, budget variance bars, and correlation heatmaps exported as high-resolution PNGs.
- **Single-Canvas Power BI Dashboard**: Complete consolidated executive dashboard ([powerbi_consolidated_dashboard.png](file:///d:/parvam%20training/data_analytics/personal_finance/Charts/powerbi_consolidated_dashboard.png)) and interactive web viewer ([powerbi_dashboard_view.html](file:///d:/parvam%20training/data_analytics/personal_finance/PowerBI/powerbi_dashboard_view.html)).
- **Power BI DAX Blueprint**: Production-grade DAX measures and complete data modeling instructions.

---

## 4. Technologies Used

- **Python**: Version 3.10 / 3.11
- **Virtual Environment**: Python `venv`
- **Data Manipulation**: `pandas`, `numpy`
- **Data Visualization**: `matplotlib`, `seaborn`, `plotly`
- **Notebook Interface**: `jupyter`, `ipykernel`, `nbformat`
- **Business Intelligence**: `Power BI Desktop`

---

## 5. Folder Structure

```
personal_finance/
│
├── venv/                              # Isolated Python virtual environment (ignored in git)
│
├── Dataset/                           # Financial datasets & generation script
│   ├── transactions.csv               # 364 Transaction records (Jan 2026 - Dec 2026)
│   ├── monthly_budget.csv             # Planned monthly category budget limits
│   ├── generate_data.py               # Synthetic data generation script
│   └── README_dataset.md              # Dataset metadata & data dictionary
│
├── Notebooks/                         # Jupyter notebooks & builders
│   ├── Personal_Finance_Analysis.ipynb# Fully executed analysis notebook with outputs
│   └── build_notebook.py              # Programmatic notebook constructor
│
├── Charts/                            # High-resolution generated visual charts (PNG)
│   ├── monthly_income_vs_expenses.png # Dual line chart: Income vs Outflow
│   ├── category_wise_expenses.png     # Donut chart: Category spending breakdown
│   ├── monthly_expense_trend.png      # Column chart: Monthly spending vs average
│   ├── savings_analysis.png           # Trend line: Net monthly savings
│   ├── payment_method_analysis.png    # Column chart: Outflows across payment channels
│   ├── budget_vs_actual.png           # Clustered bar chart: Planned vs actual by category
│   └── expense_category_correlation.png # Correlation heatmap: Spending co-movement
│
├── PowerBI/                           # Power BI setup assets & instructions
│   ├── dax_measures.txt               # Ready-to-copy DAX measure definitions
│   └── PowerBI_Dashboard_Guide.md     # Step-by-step canvas layout and data model guide
│
├── Reports/                           # Academic & professional summary reports
│   └── project_summary.md             # Executive problem, findings, and strategy report
│
├── requirements.txt                   # Frozen package dependencies
├── .gitignore                         # Git exclusion rules
├── setup_venv.bat                     # Automated Windows setup script
├── run_notebook.bat                   # One-click notebook launcher
└── README.md                          # Primary project documentation
```

---

## 6. Virtual Environment & Quick Start Guide

### Step 1: Automated Setup (Recommended on Windows)
Simply double-click:
```cmd
setup_venv.bat
```
*This script automatically verifies Python, creates `venv`, upgrades pip, installs `requirements.txt`, and registers the `Python (Finance Analysis)` Jupyter kernel.*

### Step 2: Manual Terminal Setup (Alternative)
Open PowerShell or Command Prompt inside the project folder:
```powershell
# 1. Create virtual environment
python -m venv venv

# 2. Activate virtual environment
.\venv\Scripts\activate

# 3. Upgrade pip and install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

# 4. Register the custom Jupyter kernel
python -m ipykernel install --user --name finance-analysis --display-name "Python (Finance Analysis)"
```

### Step 3: Run Jupyter Notebook
Double-click `run_notebook.bat` or run:
```powershell
.\venv\Scripts\activate
jupyter notebook Notebooks/Personal_Finance_Analysis.ipynb
```
Select the **Python (Finance Analysis)** kernel when prompted in Jupyter.

---

## 7. How to Load Data into Power BI Desktop

1. Launch **Power BI Desktop**.
2. Click **Get Data** > **Text/CSV** and select `Dataset/transactions.csv`. Click **Transform Data**.
3. In Power Query, click **New Source** > **Text/CSV** and select `Dataset/monthly_budget.csv`.
4. Click **Close & Apply**.
5. Create the Date Dimension table in the **Modeling** tab > **New Table**:
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
6. Link `Calendar[Date]` to `Transactions[Date]` in **Model View**.
7. Copy the pre-built DAX measures from [PowerBI/dax_measures.txt](file:///d:/parvam%20training/data_analytics/personal_finance/PowerBI/dax_measures.txt) into `Transactions`.
8. Follow [PowerBI/PowerBI_Dashboard_Guide.md](file:///d:/parvam%20training/data_analytics/personal_finance/PowerBI/PowerBI_Dashboard_Guide.md) to place KPI Cards, Donut Charts, Clustered Bars, and interactive Slicers.

---

## 8. Expected Outputs & Analytical Results

| Metric | Output Value | Description |
| :--- | :--- | :--- |
| **Total Annual Income** | **₹ 11,76,600.00** | Cumulative gross earnings across all income channels |
| **Total Annual Expenses** | **₹ 10,80,041.31** | Cumulative outflows across 13 expense categories |
| **Total Net Savings** | **₹ 96,558.69** | Net unspent liquidity retained across 2026 |
| **Overall Savings Rate** | **8.21%** | Savings as percentage of gross income |
| **Average Monthly Expenses** | **₹ 90,003.44** | Baseline monthly operational cost of living |
| **Dominant Category** | **Rent (₹ 2,40,000.00)** | Consumes 22.22% of total annual expenditure |
| **Top Payment Instrument** | **UPI (₹ 4,37,185.00)** | Preferred payment method for frequent daily transactions |
| **Budget Variance** | **-₹ 48,641.31 (Deficit)** | Expenditure overshot budget ceiling by 4.7% |

---

## 9. Project Limitations

1. **Synthetic Nature**: Data is generated programmatically using realistic statistical distributions and does not reflect real-time external macroeconomic shocks or individual credit profiles.
2. **Fixed Inflation Assumption**: The analysis assumes static baseline recurring costs (e.g. constant rent and EMI) across 12 months without adjusting for intra-year inflation adjustments.
3. **PBIX Automation Constraint**: Direct creation of proprietary `.pbix` binaries requires interactive compilation inside Power BI Desktop; hence, full data schemas, clean datasets, DAX measures, and configuration guides are provided.

---

## 10. Final Verification Checklist

- [x] Python Virtual Environment (`venv`) initialized and verified.
- [x] Package dependencies pinned in `requirements.txt`.
- [x] Reproducible synthetic transaction and budget datasets generated.
- [x] Jupyter Notebook (`Personal_Finance_Analysis.ipynb`) completely executed end-to-end with all cell outputs saved.
- [x] All 7 required statistical charts generated and saved in `Charts/`.
- [x] Power BI DAX formulas provided in `PowerBI/dax_measures.txt`.
- [x] Step-by-step Power BI creation guide documented in `PowerBI/PowerBI_Dashboard_Guide.md`.
- [x] Comprehensive project summary report in `Reports/project_summary.md`.
- [x] Windows automation scripts `setup_venv.bat` and `run_notebook.bat` tested.
