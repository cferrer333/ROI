class Income():
    def __init__(self, income, laundry, storage, misc):
        self.income = income
        self.laundry = laundry
        self.storage = storage
        self.misc = misc
        
    def totalIncome(self):
        self.totalIncome = sum([
            self.income,
            self.laundry,
            self.storage,
            self.misc
        ])
        return self.totalIncome

class Expenses:
    def __init__(self, tax, insurance, utilities, HOA, landscape, vacancy, repairs, cap_ex, mortgage, property_management):
        self.tax = tax
        self.insurance = insurance
        self.utilities = utilities
        self.HOA = HOA
        self.landscape = landscape
        self.vacancy = vacancy
        self.repairs = repairs
        self.cap_ex = cap_ex
        self.mortgage = mortgage
        self.property_management = property_management

    def calculateExpenses(self):
        self.total_expenses = sum([
            self.tax,
            self.insurance,
            self.utilities,
            self.HOA,
            self.landscape,
            self.vacancy,
            self.repairs,
            self.cap_ex,
            self.mortgage,
            self.property_management
        ])
        return self.total_expenses
    
class CashOnCash:
    def __init__(self, down_payment, closing_cost, rehab_budget, misc_other, total_investment):
        self.down_payment = down_payment
        self.closing_cost = closing_cost
        self.rehab_budget = rehab_budget
        self.misc_other = misc_other
        
    def calculateInvestment(self):
        self.total_investment = sum([
            self.down_payment,
            self.closing_cost,
            self.rehab_budget,
            self.misc_other
        ])
        return self.total_investment

# Driver code        
def cashFlow():
    cash_flow = duplex_income.totalIncome() - duplex_expenses.calculateExpenses()
    return cash_flow * 12

def calculateROI():
    ROI = cashFlow() / duplex_cashoncash.calculateInvestment()
    print(f'The ROI is {ROI}%')
    
duplex_income = Income(2000, 0, 0, 0)
duplex_expenses = Expenses(150, 100, 0, 0, 0, 100, 100, 100, 860, 200)
duplex_cashoncash = CashOnCash(40000, 3000, 7000, 0, 0)
calculateROI()