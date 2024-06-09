class Income:
    def __init__(self, rental, laundry=0, storage=0, misc=0):
        self.rental = rental
        self.laundry = laundry
        self.storage = storage
        self.misc = misc

    def total_income(self):
        return self.rental + self.laundry + self.storage + self.misc


class Expenses:
    def __init__(self, tax, insurance, utilities, hoa, lawn_snow, vacancy, repairs, capex, management, mortgage):
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.hoa = hoa
        self.lawn_snow = lawn_snow
        self.vacancy = vacancy
        self.repairs = repairs
        self.capex = capex
        self.management = management
        self.mortgage = mortgage

    def total_expenses(self):
        return (self.tax + self.insurance + self.utilities + self.hoa + self.lawn_snow +
                self.vacancy + self.repairs + self.capex + self.management + self.mortgage)


class CashFlow:
    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    def monthly_cashflow(self):
        return self.income.total_income() - self.expenses.total_expenses()

    def annual_cashflow(self):
        return self.monthly_cashflow() * 12


class ROICalculator:
    def __init__(self, down_payment, closing_costs, rehab_budget, misc_other, annual_cashflow):
        self.down_payment = down_payment
        self.closing_costs = closing_costs
        self.rehab_budget = rehab_budget
        self.misc_other = misc_other
        self.annual_cashflow = annual_cashflow

    def total_investment(self):
        return self.down_payment + self.closing_costs + self.rehab_budget + self.misc_other

    def cash_on_cash_roi(self):
        return (self.annual_cashflow / self.total_investment()) * 100

def main():
    # Example inputs
    income = Income(rental=2000, laundry=100, storage=50, misc=50)
    expenses = Expenses(tax=150, insurance=100, utilities=200, hoa=50, lawn_snow=30, vacancy=100, repairs=100, capex=100, management=200, mortgage=1000)
    
    cashflow = CashFlow(income, expenses)
    annual_cashflow = cashflow.annual_cashflow()
    
    roi_calculator = ROICalculator(down_payment=40000, closing_costs=3000, rehab_budget=7000, misc_other=1000, annual_cashflow=annual_cashflow)
    
    print(f"Total Monthly Income: ${income.total_income()}")
    print(f"Total Monthly Expenses: ${expenses.total_expenses()}")
    print(f"Monthly Cash Flow: ${cashflow.monthly_cashflow()}")
    print(f"Annual Cash Flow: ${cashflow.annual_cashflow()}")
    print(f"Total Investment: ${roi_calculator.total_investment()}")
    print(f"Cash on Cash ROI: {roi_calculator.cash_on_cash_roi():.2f}%")

if __name__ == "__main__":
    main()
