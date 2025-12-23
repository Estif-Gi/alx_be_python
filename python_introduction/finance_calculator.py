# finance_calculator.py
# Calculates monthly savings and projects annual savings with simple interest

# Get user input
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Project annual savings with 5% simple interest
annual_savings_without_interest = monthly_savings * 12
interest_earned = annual_savings_without_interest * 0.05
projected_savings = annual_savings_without_interest + interest_earned

# Alternative one-line calculation (same result):
# projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
# which simplifies to: monthly_savings * 12 * 1.05

# Display results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings}.")