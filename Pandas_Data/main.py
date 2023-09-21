from testing import get_bill, get_monthly_expense, calculations
import pandas as pd
bill_list = []
monthly_expense_list = []
final = []
for i in range(12):
    bill_amount = get_bill()
    monthly_expense_amount = get_monthly_expense()
    result = calculations(bill_amount, monthly_expense_amount)
    print(result)
    final.append(result)
    bill_list.append(bill_amount)
    monthly_expense_list.append(monthly_expense_amount)
print("Monthly Bill", bill_list)
print("Monthly Expense", monthly_expense_list)


months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

data = {
"Bill": bill_list,
    "Expense": monthly_expense_list,
    "Result": final

}

df = pd.DataFrame(data, index=months)
file = "data.csv"
df.to_csv(file)