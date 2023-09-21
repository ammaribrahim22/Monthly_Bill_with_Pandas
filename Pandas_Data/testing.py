def get_bill():
    bill_amount = int(input("Enter your bill: "))
    return bill_amount

def get_monthly_expense():
    monthly_expense_amount = int(input("Enter your monthly spending: "))
    return monthly_expense_amount

def calculations(bill_amount, monthly_expense_amount):
    if bill_amount < monthly_expense_amount:
        bill_paid = bill_amount - monthly_expense_amount
        bill_paid = bill_paid * -1
        return f"Congratulations! You have successfully paid the bill. Balance is {bill_paid}"
    else:
        loan_amount_everyday = -1 * bill_amount / 365
        loan_amount_monthly = -1 * bill_amount / 12
        return f"Loan of your bill on everyday: {loan_amount_everyday}, Loan amount of your bill on every month: {loan_amount_monthly}"
