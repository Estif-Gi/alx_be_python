income = int(input("Enter your monthly income:"))

monthly_expanses = int(input("Enter your total monthly expenses:"))

monthly_savings = income - monthly_expanses

Projected_Savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

print("Your monthly savings are" , monthly_savings)

print("Projected savings after one year, with interest, is:" ,Projected_Savings )