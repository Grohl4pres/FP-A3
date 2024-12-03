# -*- coding: utf-8 -*-
"""FPA3

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IVaP58rX9FQ5TYAVC2LOlF8jXtCke7Q3
"""

# Google Colab Notebook: Data Preprocessing and KPI Calculation

# Install necessary libraries
!pip install pandas numpy matplotlib

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Hardcoded Sample P&L Data
data = pd.DataFrame({
    'Date': [
        '2024-01-01', '2024-01-15', '2024-02-01', '2024-02-15',
        '2024-03-01', '2024-03-15', '2024-04-01', '2024-04-15'
    ],
    'Description': [
        'Delivery Income', 'Fuel Expense', 'Vehicle Maintenance',
        'Insurance', 'Lease Costs', 'Bonuses', 'Depreciation', 'Miscellaneous'
    ],
    'Amount': [
        12000, -2000, -1500, -1000, -2500, 500, -1000, -300
    ],
    'Category': [
        'Revenue', 'Operating Expenses', 'Operating Expenses',
        'Operating Expenses', 'Fixed Costs', 'Revenue', 'Fixed Costs', 'Other'
    ]
})

# Step 2: KPI Calculation
# Aggregate Revenue and Expenses
total_revenue = data.loc[data['Category'] == 'Revenue', 'Amount'].sum()
operating_expenses = data.loc[data['Category'] == 'Operating Expenses', 'Amount'].sum()
fixed_costs = data.loc[data['Category'] == 'Fixed Costs', 'Amount'].sum()
total_expenses = operating_expenses + fixed_costs
net_profit = total_revenue + total_expenses
operating_profit_margin = (net_profit / total_revenue) * 100 if total_revenue > 0 else 0

# Display KPIs
print(f"Total Revenue: ${total_revenue:.2f}")
print(f"Operating Expenses: ${operating_expenses:.2f}")
print(f"Fixed Costs: ${fixed_costs:.2f}")
print(f"Net Profit: ${net_profit:.2f}")
print(f"Operating Profit Margin: {operating_profit_margin:.2f}%")

# Step 3: Visualization
# Bar chart for categories
category_totals = data.groupby('Category')['Amount'].sum()
category_totals.plot(kind='bar', title='P&L Breakdown by Category', xlabel='Category', ylabel='Amount ($)', color=['green', 'red', 'blue', 'orange'])
plt.grid(axis='y')
plt.show()

# Save processed data for Streamlit use
data.to_csv('processed_pnl_data.csv', index=False)

# File: app.py
# Streamlit Dashboard for P&L Analysis

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Load the Sample Data
st.title("Profit & Loss Dashboard")
st.write("Analyzing a sample P&L dataset")

# Load preprocessed data
data = pd.read_csv('processed_pnl_data.csv')

# Step 2: Display Raw Data
st.write("### Raw Data", data)

# Step 3: Calculate KPIs
total_revenue = data.loc[data['Category'] == 'Revenue', 'Amount'].sum()
operating_expenses = data.loc[data['Category'] == 'Operating Expenses', 'Amount'].sum()
fixed_costs = data.loc[data['Category'] == 'Fixed Costs', 'Amount'].sum()
total_expenses = operating_expenses + fixed_costs
net_profit = total_revenue + total_expenses
operating_profit_margin = (net_profit / total_revenue) * 100 if total_revenue > 0 else 0

# Display KPIs
st.metric("Total Revenue", f"${total_revenue:.2f}")
st.metric("Operating Expenses", f"${operating_expenses:.2f}")
st.metric("Fixed Costs", f"${fixed_costs:.2f}")
st.metric("Net Profit", f"${net_profit:.2f}")
st.metric("Operating Profit Margin", f"{operating_profit_margin:.2f}%")

# Step 4: Visualize P&L Breakdown
st.write("### P&L Breakdown by Category")
category_totals = data.groupby('Category')['Amount'].sum()

fig, ax = plt.subplots()
category_totals.plot(kind='bar', ax=ax, color=['green', 'red', 'blue', 'orange'])
ax.set_title('P&L Breakdown by Category')
ax.set_xlabel('Category')
ax.set_ylabel('Amount ($)')
st.pyplot(fig)

# Step 5: Save and Download Processed Data
if st.button("Download Processed Data"):
    st.download_button(
        label="Download CSV",
        data=open('processed_pnl_data.csv', 'rb'),
        file_name='processed_pnl_data.csv',
        mime='text/csv'
    )

pip install streamlit