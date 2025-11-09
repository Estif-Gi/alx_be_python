income = int(input("Enter your monthly income:"))

monthly_expanses = int(input("Enter your total monthly expenses:"))

monthly_savings = income - monthly_expanses

Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("This is your monthly saving" , monthly_savings)

print("And this is your annual saving including 5% interest" ,Projected_Savings )