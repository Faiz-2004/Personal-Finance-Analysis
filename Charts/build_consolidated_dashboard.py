import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns

# Set overall design aesthetics
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')
plt.rcParams['font.sans-serif'] = 'Segoe UI', 'DejaVu Sans', 'Arial'
plt.rcParams['font.size'] = 9.5

# Load datasets
df_tx = pd.read_csv('Dataset/transactions.csv')
df_budget = pd.read_csv('Dataset/monthly_budget.csv')

df_tx['Date'] = pd.to_datetime(df_tx['Date'])
df_income = df_tx[df_tx['Type'] == 'Income']
df_expenses = df_tx[df_tx['Type'] == 'Expense']

# 1. Core KPIs
total_income = df_income['Amount'].sum()
total_expenses = df_expenses['Amount'].sum()
total_savings = total_income - total_expenses
savings_rate = (total_savings / total_income) * 100
avg_monthly_exp = total_expenses / 12

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 
               'July', 'August', 'September', 'October', 'November', 'December']
month_short = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Monthly cash flows
monthly_pivot = df_tx.pivot_table(
    index='Month', columns='Type', values='Amount', aggfunc='sum', fill_value=0.0
).reindex(month_order)
monthly_pivot['Savings'] = monthly_pivot['Income'] - monthly_pivot['Expense']

# Category summary
cat_summary = df_expenses.groupby('Category')['Amount'].sum().sort_values(ascending=False)

# Budget vs Actual
actual_cat = df_expenses.groupby('Category')['Amount'].sum()
budget_cat = df_budget.groupby('Category')['Budget_Amount'].sum()
bva_df = pd.DataFrame({'Budget': budget_cat, 'Actual': actual_cat}).fillna(0.0)
bva_df = bva_df.sort_values('Actual', ascending=False)

# Payment method summary
pm_summary = df_expenses.groupby('Payment_Method')['Amount'].sum().sort_values(ascending=False)

# ==============================================================================
# CREATE POWER BI THEMED SINGLE-PAGE DASHBOARD CANVAS
# Canvas Size: 1920 x 1080 Aspect Ratio (20 x 11.25 inches @ 300 DPI)
# ==============================================================================
fig = plt.figure(figsize=(20, 11.25), facecolor='#0B132B') # Modern Deep Tech Navy Background

# Create Grid Layout
# Row 0: Top Header Banner
# Row 1: KPI Cards
# Row 2 & 3: Visual Analytics Grid
gs = gridspec.GridSpec(
    nrows=4, ncols=4, 
    height_ratios=[0.85, 1.1, 3.4, 3.4],
    hspace=0.38, wspace=0.25,
    top=0.96, bottom=0.04, left=0.03, right=0.97
)

# ------------------------------------------------------------------------------
# 1. HEADER BANNER
# ------------------------------------------------------------------------------
ax_head = fig.add_subplot(gs[0, :])
ax_head.axis('off')
ax_head.text(0.0, 0.75, "PERSONAL FINANCE & EXPENSE ANALYSIS DASHBOARD", 
             fontsize=20, fontweight='heavy', color='#FFFFFF', va='center')
ax_head.text(0.0, 0.20, "Annual Cash Flow, Expense Categorization, Payment Channels & Budget Variance Performance (FY 2026)", 
             fontsize=11.5, fontweight='normal', color='#90E0EF', va='center')

# Header Filter Badges (Mock Power BI Interactive Slicers)
slicer_box = dict(boxstyle='round,pad=0.5', facecolor='#1C2541', edgecolor='#3A506B', linewidth=1.2)
ax_head.text(0.66, 0.5, "Year: 2026", fontsize=9.5, color='#E0E1DD', bbox=slicer_box, va='center')
ax_head.text(0.77, 0.5, "Currency: INR (₹)", fontsize=9.5, color='#E0E1DD', bbox=slicer_box, va='center')
ax_head.text(0.89, 0.5, "View: Power BI Canvas", fontsize=9.5, color='#48CAE4', fontweight='bold', bbox=slicer_box, va='center')

# ------------------------------------------------------------------------------
# 2. KPI CARDS ROW (5 Interactive Metric Cards)
# ------------------------------------------------------------------------------
kpis = [
    ("TOTAL ANNUAL INCOME", f"₹ {total_income:,.0f}", "100% Cash Inflows", "#00B4D8", "#03045E"),
    ("TOTAL ANNUAL EXPENSES", f"₹ {total_expenses:,.0f}", f"Avg ₹ {avg_monthly_exp:,.0f} / mo", "#F72585", "#3F0024"),
    ("TOTAL NET SAVINGS", f"₹ {total_savings:,.0f}", "Net Liquid Capital Retained", "#4ADE80", "#064E3B"),
    ("ANNUAL SAVINGS RATE", f"{savings_rate:.1f}%", "Target Benchmark: >20.0%", "#FBBF24", "#451A03"),
    ("BUDGET DEFICIT / VARIANCE", f"-₹ {abs(bva_df['Budget'].sum() - bva_df['Actual'].sum()):,.0f}", "Over Budget (+4.7%)", "#FB7185", "#4C0519")
]

for idx, (title, val, sub, acc_color, bg_card) in enumerate(kpis):
    # Span 5 cards across 4 columns dynamically using inset subplots
    pass

# We create 5 card axes inside row 1
card_gs = gridspec.GridSpecFromSubplotSpec(1, 5, subplot_spec=gs[1, :], wspace=0.18)
for idx, (title, val, sub, acc_color, bg_card) in enumerate(kpis):
    ax_card = fig.add_subplot(card_gs[0, idx])
    ax_card.set_facecolor('#1C2541')
    ax_card.grid(False)
    for spine in ax_card.spines.values():
        spine.set_color('#3A506B')
        spine.set_linewidth(1.2)
    ax_card.set_xticks([])
    ax_card.set_yticks([])
    
    # Left accent indicator strip
    ax_card.axvline(x=0.03, ymin=0.1, ymax=0.9, color=acc_color, linewidth=4.5)
    
    # Texts
    ax_card.text(0.12, 0.75, title, fontsize=8.5, fontweight='bold', color='#90E0EF', va='center')
    ax_card.text(0.12, 0.44, val, fontsize=15.5, fontweight='heavy', color='#FFFFFF', va='center')
    ax_card.text(0.12, 0.18, sub, fontsize=8.0, fontweight='medium', color='#A0AAB2', va='center')

# ------------------------------------------------------------------------------
# 3. ROW 2 VISUALIZATIONS
# ------------------------------------------------------------------------------

# Chart 1: Monthly Income vs Expenses (Line Chart with Area Fill) - Col 0 to 2
ax1 = fig.add_subplot(gs[2, 0:2])
ax1.set_facecolor('#1C2541')
for spine in ax1.spines.values():
    spine.set_color('#3A506B')

x_pos = np.arange(len(month_order))
ax1.plot(x_pos, monthly_pivot['Income'], marker='o', linewidth=2.8, color='#00E5FF', label='Income (₹)', zorder=4)
ax1.plot(x_pos, monthly_pivot['Expense'], marker='s', linewidth=2.8, color='#FF5252', label='Expenses (₹)', zorder=4)
ax1.fill_between(x_pos, monthly_pivot['Income'], monthly_pivot['Expense'], 
                 where=(monthly_pivot['Income'] >= monthly_pivot['Expense']),
                 color='#00E5FF', alpha=0.15, label='Net Savings Margin')

ax1.set_title('Monthly Inflow (Income) vs Outflow (Expenses)', fontsize=11, fontweight='bold', color='#FFFFFF', pad=10, loc='left')
ax1.set_xticks(x_pos)
ax1.set_xticklabels(month_short, color='#E0E1DD', fontsize=8.5)
ax1.tick_params(colors='#A0AAB2', labelsize=8.5)
ax1.yaxis.set_major_formatter('₹{:,.0f}'.format)
ax1.grid(True, linestyle='--', color='#2D3B55', alpha=0.7)
ax1.legend(facecolor='#1C2541', edgecolor='#3A506B', labelcolor='#FFFFFF', fontsize=8.2, loc='upper left')

# Chart 2: Category Expense Breakdown (Donut Chart) - Col 2
ax2 = fig.add_subplot(gs[2, 2])
ax2.set_facecolor('#1C2541')
for spine in ax2.spines.values():
    spine.set_visible(False)

top_cats = cat_summary.head(6)
other_sum = cat_summary.iloc[6:].sum()
donut_data = pd.concat([top_cats, pd.Series({'Other (7 cats)': other_sum})])
donut_colors = ['#FF4081', '#7C4DFF', '#00E5FF', '#FFB300', '#00E676', '#FF6E40', '#607D8B']

pie_res2 = ax2.pie(
    donut_data, 
    labels=[f"{k[:9]}.." if len(k) > 10 else k for k in donut_data.index],
    autopct='%1.1f%%',
    pctdistance=0.78,
    startangle=140,
    colors=donut_colors,
    textprops=dict(color='#E0E1DD', fontsize=7.8),
    wedgeprops=dict(width=0.42, edgecolor='#1C2541', linewidth=2.5)
)
if len(pie_res2) == 3:
    wedges, texts, autotexts = pie_res2
    for at in autotexts:
        at.set_fontsize(7.5)
        at.set_weight('bold')
        at.set_color('#FFFFFF')
else:
    wedges, texts = pie_res2

ax2.set_title('Expense Distribution by Category', fontsize=11, fontweight='bold', color='#FFFFFF', pad=10, loc='center')

# Chart 3: Payment Method Analysis (Donut / Pie) - Col 3
ax3 = fig.add_subplot(gs[2, 3])
ax3.set_facecolor('#1C2541')
for spine in ax3.spines.values():
    spine.set_visible(False)

pm_colors = ['#00E5FF', '#7C4DFF', '#FF5252', '#FFB300', '#69F0AE']
pie_res3 = ax3.pie(
    pm_summary,
    labels=pm_summary.index,
    autopct='%1.1f%%',
    pctdistance=0.76,
    startangle=120,
    colors=pm_colors,
    textprops=dict(color='#E0E1DD', fontsize=8.0),
    wedgeprops=dict(width=0.42, edgecolor='#1C2541', linewidth=2.5)
)
if len(pie_res3) == 3:
    wedges_pm, texts_pm, autotexts_pm = pie_res3
    for at in autotexts_pm:
        at.set_fontsize(7.5)
        at.set_weight('bold')
        at.set_color('#FFFFFF')
else:
    wedges_pm, texts_pm = pie_res3

ax3.set_title('Payment Method Distribution', fontsize=11, fontweight='bold', color='#FFFFFF', pad=10, loc='center')

# ------------------------------------------------------------------------------
# 4. ROW 3 VISUALIZATIONS
# ------------------------------------------------------------------------------

# Chart 4: Monthly Expense Trend with Avg Baseline (Column Chart) - Col 0 & 1
ax4 = fig.add_subplot(gs[3, 0:2])
ax4.set_facecolor('#1C2541')
for spine in ax4.spines.values():
    spine.set_color('#3A506B')

bars = ax4.bar(x_pos, monthly_pivot['Expense'], color='#4361EE', width=0.6, edgecolor='#4895EF', linewidth=0.8, zorder=3)
ax4.axhline(avg_monthly_exp, color='#FF5252', linestyle='--', linewidth=1.8, 
            label=f'Average Monthly Spend: ₹{avg_monthly_exp:,.0f}', zorder=4)

for bar in bars:
    yval = bar.get_height()
    ax4.text(bar.get_x() + bar.get_width()/2.0, yval + 1200, f'₹{yval/1000:,.0f}K', 
             ha='center', va='bottom', fontsize=7.2, fontweight='bold', color='#90E0EF')

ax4.set_title('Monthly Outflow Progression & Mean Benchmark', fontsize=11, fontweight='bold', color='#FFFFFF', pad=10, loc='left')
ax4.set_xticks(x_pos)
ax4.set_xticklabels(month_short, color='#E0E1DD', fontsize=8.5)
ax4.tick_params(colors='#A0AAB2', labelsize=8.5)
ax4.yaxis.set_major_formatter('₹{:,.0f}'.format)
ax4.grid(True, linestyle='--', color='#2D3B55', alpha=0.7)
ax4.set_ylim(0, monthly_pivot['Expense'].max() * 1.15)
ax4.legend(facecolor='#1C2541', edgecolor='#3A506B', labelcolor='#FFFFFF', fontsize=8.2, loc='upper right')

# Chart 5: Budget vs Actual Variance (Clustered Horizontal Bar) - Col 2 & 3
ax5 = fig.add_subplot(gs[3, 2:4])
ax5.set_facecolor('#1C2541')
for spine in ax5.spines.values():
    spine.set_color('#3A506B')

top_bva = bva_df.head(9).iloc[::-1] # Top 9 categories reversed for barh
y_ind = np.arange(len(top_bva))
h = 0.38

bars_b = ax5.barh(y_ind + h/2, top_bva['Budget'], height=h, color='#3A86FF', label='Planned Budget', edgecolor='#1C2541', zorder=3)
bars_a = ax5.barh(y_ind - h/2, top_bva['Actual'], height=h, color='#FF006E', label='Actual Spent', edgecolor='#1C2541', zorder=3)

ax5.set_yticks(y_ind)
ax5.set_yticklabels(top_bva.index, color='#E0E1DD', fontsize=8.5)
ax5.tick_params(colors='#A0AAB2', labelsize=8.5)
ax5.xaxis.set_major_formatter('₹{:,.0f}'.format)
ax5.set_title('Budget vs Actual Expenditure by Category (Annual Aggregation)', fontsize=11, fontweight='bold', color='#FFFFFF', pad=10, loc='left')
ax5.grid(True, linestyle='--', color='#2D3B55', alpha=0.7)
ax5.legend(facecolor='#1C2541', edgecolor='#3A506B', labelcolor='#FFFFFF', fontsize=8.2, loc='lower right')

# Export Dashboard
output_path = 'Charts/powerbi_consolidated_dashboard.png'
plt.savefig(output_path, dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.close()
print(f"Power BI All-in-One Dashboard created successfully: {output_path}")
