from functools import reduce

class Loan:
    def __init__(self, principal, annual_rate, years):
        self.principal = principal
        self.annual_rate = annual_rate
        self.years = years
        self.monthly_rate = annual_rate / 12
        self.total_payments = years * 12
        self.schedule = self.generate_schedule()

    def calculate_monthly_payment(self):
        if self.monthly_rate == 0:
            return self.principal / self.total_payments
        return self.principal * (self.monthly_rate * (1 + self.monthly_rate) ** self.total_payments) / \
               ((1 + self.monthly_rate) ** self.total_payments - 1)

    def generate_schedule(self):
        monthly_payment = self.calculate_monthly_payment()
        balance = self.principal
        schedule = []

        for month in range(1, self.total_payments + 1):
            interest_payment = balance * self.monthly_rate
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment

            schedule.append({
                'Month': month,
                'Payment': round(monthly_payment, 2),
                'Principal': round(principal_payment, 2),
                'Interest': round(interest_payment, 2),
                'Balance': round(balance, 2)
            })

        return schedule

    def total_interest_paid(self):
        total_paid = reduce(lambda acc, payment: acc + payment['Payment'], self.schedule, 0)
        total_interest = total_paid - self.principal
        return round(total_interest, 2)

    def display_schedule(self):
        print(f"{'Month':<10}{'Payment':<15}{'Principal':<15}{'Interest':<15}{'Balance':<15}")
        for payment in self.schedule:
            print(f"{payment['Month']:<10}{payment['Payment']:<15}{payment['Principal']:<15}{payment['Interest']:<15}{payment['Balance']:<15}")

    def early_payoff(self, payoff_month):
        if payoff_month < 1 or payoff_month > self.total_payments:
            print("Invalid month for early payoff.")
            return
        
        remaining_balance = self.schedule[payoff_month - 1]['Balance']
        print(f"Remaining balance after {payoff_month - 1} payments: {remaining_balance}")
        print("You can pay off the loan early by paying this remaining balance.")

    def generate_schedule_variable_rates(self, interest_rates):
        balance = self.principal
        schedule = []

        for month in range(1, self.total_payments + 1):
            monthly_rate = interest_rates[month - 1] / 12
            if month == 1:
                monthly_payment = self.calculate_monthly_payment()
            else:
                monthly_payment = self.calculate_monthly_payment()
            interest_payment = balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment

            schedule.append({
                'Month': month,
                'Payment': round(monthly_payment, 2),
                'Principal': round(principal_payment, 2),
                'Interest': round(interest_payment, 2),
                'Balance': round(balance, 2)
            })

        return schedule


# Example usage
principal = 10000
annual_rate = 0.05
years = 3
loan = Loan(principal, annual_rate, years)
loan.display_schedule()
print(f"Total Interest Paid: {loan.total_interest_paid()}")

loan.early_payoff(12)

variable_interest_rates = [0.05, 0.045, 0.04, 0.035, 0.03, 0.025, 0.03, 0.04, 0.045, 0.05, 0.055, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.11, 0.1, 0.09, 0.08, 0.07, 0.06, 0.05, 0.045, 0.04, 0.035, 0.03, 0.025, 0.03, 0.04, 0.045, 0.05, 0.055, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.11, 0.1, 0.09, 0.08]
loan_with_variable_rates = Loan(principal, annual_rate, years)
loan_with_variable_rates.schedule = loan_with_variable_rates.generate_schedule_variable_rates(variable_interest_rates)
loan_with_variable_rates.display_schedule()
print(f"Total Interest Paid with Variable Rates: {loan_with_variable_rates.total_interest_paid()}")
