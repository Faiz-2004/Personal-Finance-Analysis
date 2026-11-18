import random
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set fixed seed for reproducibility
random.seed(42)
np.random.seed(42)

print("Generating synthetic personal finance transactions...")

# Date range: Jan 1, 2026 to Dec 31, 2026
start_date = datetime(2026, 1, 1)
end_date = datetime(2026, 12, 31)

# Payment methods and accounts
payment_methods = ['UPI', 'Cash', 'Debit Card', 'Credit Card', 'Net Banking']
account_types = ['Salary Account', 'Savings Account', 'Credit Card Account', 'Cash Wallet']

# Method to account mapping preference
def get_account_for_payment(pm):
    if pm == 'Credit Card':
        return 'Credit Card Account'
    elif pm == 'Cash':
        return 'Cash Wallet'
    elif pm == 'Net Banking':
        return 'Salary Account'
    elif pm == 'UPI':
        return random.choice(['Salary Account', 'Savings Account'])
    else: # Debit Card
        return random.choice(['Salary Account', 'Savings Account'])

records = []
tx_counter = 1001

# 1. Guaranteed Monthly Incomes (Salary, Freelance, Interest, etc.)
months = range(1, 13)
month_names = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']

for m in months:
    m_name = month_names[m - 1]
    
    # Primary Salary (Credited around 1st-3rd of each month)
    salary_day = random.randint(1, 3)
    salary_date = datetime(2026, m, salary_day)
    # Salary between 75,000 and 85,000 INR
    salary_amt = 80000.0
    records.append({
        'Transaction_ID': f'TXN{tx_counter:05d}',
        'Date': salary_date.strftime('%Y-%m-%d'),
        'Description': 'Monthly Corporate Salary Credit',
        'Category': 'Salary',
        'Type': 'Income',
        'Amount': salary_amt,
        'Payment_Method': 'Net Banking',
        'Account_Type': 'Salary Account',
        'Month': m_name,
        'Year': 2026
    })
    tx_counter += 1

    # Freelance Income (In most months, 10 out of 12 months)
    if m not in [4, 9]:
        fl_day = random.randint(12, 22)
        fl_amt = float(random.randint(12, 28) * 1000)
        records.append({
            'Transaction_ID': f'TXN{tx_counter:05d}',
            'Date': datetime(2026, m, fl_day).strftime('%Y-%m-%d'),
            'Description': 'Freelance Web Design & Consulting',
            'Category': 'Freelance',
            'Type': 'Income',
            'Amount': fl_amt,
            'Payment_Method': random.choice(['UPI', 'Net Banking']),
            'Account_Type': 'Savings Account',
            'Month': m_name,
            'Year': 2026
        })
        tx_counter += 1

    # Quarterly Business / Interest Income
    if m in [3, 6, 9, 12]:
        int_day = random.randint(25, 28)
        int_amt = float(random.randint(35, 65) * 100)
        records.append({
            'Transaction_ID': f'TXN{tx_counter:05d}',
            'Date': datetime(2026, m, int_day).strftime('%Y-%m-%d'),
            'Description': 'Bank Savings & Fixed Deposit Interest',
            'Category': 'Interest',
            'Type': 'Income',
            'Amount': int_amt,
            'Payment_Method': 'Net Banking',
            'Account_Type': 'Savings Account',
            'Month': m_name,
            'Year': 2026
        })
        tx_counter += 1

    # Occasional Business / Other Income
    if m in [2, 7, 11]:
        oth_amt = float(random.randint(5, 15) * 1000)
        records.append({
            'Transaction_ID': f'TXN{tx_counter:05d}',
            'Date': datetime(2026, m, random.randint(10, 20)).strftime('%Y-%m-%d'),
            'Description': 'Affiliate & Digital Asset Revenue',
            'Category': random.choice(['Business Income', 'Other Income']),
            'Type': 'Income',
            'Amount': oth_amt,
            'Payment_Method': 'UPI',
            'Account_Type': 'Savings Account',
            'Month': m_name,
            'Year': 2026
        })
        tx_counter += 1

# 2. Guaranteed Fixed Monthly Expenses
for m in months:
    m_name = month_names[m - 1]
    
    # House Rent (around 5th)
    records.append({
        'Transaction_ID': f'TXN{tx_counter:05d}',
        'Date': datetime(2026, m, 5).strftime('%Y-%m-%d'),
        'Description': 'Apartment Monthly Rent',
        'Category': 'Rent',
        'Type': 'Expense',
        'Amount': 20000.0,
        'Payment_Method': 'Net Banking',
        'Account_Type': 'Salary Account',
        'Month': m_name,
        'Year': 2026
    })
    tx_counter += 1

    # Vehicle / Personal Loan EMI (around 10th)
    records.append({
        'Transaction_ID': f'TXN{tx_counter:05d}',
        'Date': datetime(2026, m, 10).strftime('%Y-%m-%d'),
        'Description': 'Car Loan EMI Auto-debit',
        'Category': 'EMI',
        'Type': 'Expense',
        'Amount': 10500.0,
        'Payment_Method': 'Net Banking',
        'Account_Type': 'Salary Account',
        'Month': m_name,
        'Year': 2026
    })
    tx_counter += 1

    # Electricity Bill
    elec_amt = float(random.randint(18, 32) * 100)
    records.append({
        'Transaction_ID': f'TXN{tx_counter:05d}',
        'Date': datetime(2026, m, random.randint(12, 16)).strftime('%Y-%m-%d'),
        'Description': 'Monthly State Electricity Board Bill',
        'Category': 'Electricity',
        'Type': 'Expense',
        'Amount': elec_amt,
        'Payment_Method': 'UPI',
        'Account_Type': 'Salary Account',
        'Month': m_name,
        'Year': 2026
    })
    tx_counter += 1

    # High-Speed Fiber Internet Bill
    records.append({
        'Transaction_ID': f'TXN{tx_counter:05d}',
        'Date': datetime(2026, m, random.randint(7, 11)).strftime('%Y-%m-%d'),
        'Description': 'High-Speed Broadband Subscription',
        'Category': 'Internet',
        'Type': 'Expense',
        'Amount': 1199.0,
        'Payment_Method': 'UPI',
        'Account_Type': 'Salary Account',
        'Month': m_name,
        'Year': 2026
    })
    tx_counter += 1

# 3. Variable Daily / Frequent Expenses across the year
expense_specs = [
    ('Food', 'Dining at Restaurant / Swiggy / Zomato order', (250, 2200), ['UPI', 'Credit Card', 'Debit Card'], 65),
    ('Groceries', 'Supermarket & Fresh Provisions', (800, 4500), ['UPI', 'Credit Card', 'Debit Card'], 45),
    ('Transportation', 'Metro card recharge / Auto / Fuel filling', (150, 1800), ['UPI', 'Cash', 'Credit Card'], 50),
    ('Shopping', 'Clothing, footwear & personal gear', (1200, 8500), ['Credit Card', 'Debit Card', 'UPI'], 28),
    ('Healthcare', 'Pharmacy medicines / Clinic consultation', (300, 3200), ['UPI', 'Cash', 'Debit Card'], 18),
    ('Education', 'Online certification / Technical books', (600, 4000), ['Credit Card', 'Net Banking'], 15),
    ('Entertainment', 'Movie tickets / OTT streaming subscriptions / Gaming', (300, 2500), ['Credit Card', 'UPI'], 30),
    ('Travel', 'Flight/Train tickets & weekend getaway stays', (2500, 14000), ['Credit Card', 'Net Banking'], 14),
    ('Other Expenses', 'Household repairs / Laundry / Miscellaneous', (200, 1500), ['Cash', 'UPI'], 22)
]

# Generate transactions across each month
for cat, desc_tmpl, (min_a, max_a), pms, count in expense_specs:
    for _ in range(count):
        # Pick random date within 2026
        rand_days = random.randint(0, 364)
        tx_date = start_date + timedelta(days=rand_days)
        m_name = month_names[tx_date.month - 1]
        
        amt = float(round(random.uniform(min_a, max_a), 2))
        pm = random.choice(pms)
        acc = get_account_for_payment(pm)
        
        records.append({
            'Transaction_ID': f'TXN{tx_counter:05d}',
            'Date': tx_date.strftime('%Y-%m-%d'),
            'Description': desc_tmpl,
            'Category': cat,
            'Type': 'Expense',
            'Amount': amt,
            'Payment_Method': pm,
            'Account_Type': acc,
            'Month': m_name,
            'Year': 2026
        })
        tx_counter += 1

df_tx = pd.DataFrame(records)
# Sort by Date
df_tx['Date'] = pd.to_datetime(df_tx['Date'])
df_tx = df_tx.sort_values('Date').reset_index(drop=True)
df_tx['Date'] = df_tx['Date'].dt.strftime('%Y-%m-%d')

# Re-assign strictly ordered unique Transaction IDs
df_tx['Transaction_ID'] = [f'TXN{i+1:05d}' for i in range(len(df_tx))]

# Save transactions.csv
df_tx.to_csv('Dataset/transactions.csv', index=False)
print(f"transactions.csv created with {len(df_tx)} records.")

# 4. Generate monthly_budget.csv
# Categories with monthly planned budget
budget_categories = [
    'Food', 'Rent', 'Transportation', 'Shopping', 'Electricity', 
    'Internet', 'Healthcare', 'Education', 'Entertainment', 
    'Groceries', 'EMI', 'Travel', 'Other Expenses'
]

# Standard baseline monthly budget per category
baseline_budgets = {
    'Rent': 20000.0,
    'EMI': 10500.0,
    'Groceries': 12000.0,
    'Food': 9000.0,
    'Transportation': 6000.0,
    'Shopping': 7000.0,
    'Electricity': 2500.0,
    'Internet': 1200.0,
    'Healthcare': 3000.0,
    'Education': 2500.0,
    'Entertainment': 3500.0,
    'Travel': 5000.0,
    'Other Expenses': 2000.0
}

budget_records = []
for m_name in month_names:
    for cat in budget_categories:
        b_amt = baseline_budgets[cat]
        # Slight realistic variation in budget for festive/travel months
        if cat in ['Shopping', 'Travel'] and m_name in ['October', 'November', 'December']:
            b_amt += 3000.0
        elif cat == 'Electricity' and m_name in ['April', 'May', 'June']:
            b_amt += 1000.0
            
        budget_records.append({
            'Month': m_name,
            'Category': cat,
            'Budget_Amount': float(b_amt)
        })

df_budget = pd.DataFrame(budget_records)
df_budget.to_csv('Dataset/monthly_budget.csv', index=False)
print(f"monthly_budget.csv created with {len(df_budget)} records ({len(month_names)} months x {len(budget_categories)} categories).")
