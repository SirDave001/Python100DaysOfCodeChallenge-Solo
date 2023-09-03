class Person:
    def __init__(self, IdNumber):
        self.IdNumber = IdNumber
    def PayTax(self, TaxableIncome, TaxRate):
        tax = TaxableIncome * TaxRate
        print(f'The tax is ${tax}')
        return tax
    
class Businessman(Person):
    def PayTax(self, TaxableIncome, BusinessAllowance, TaxRate):
        tax = (TaxableIncome - BusinessAllowance) * TaxRate
        print(f'The tax is ${tax}')
        return tax
    
class Employee(Person):
    def RefundTax(self, amount):
        print(f'The refund is ${amount}')
        return amount
    
    
businessman = Businessman('A123')
businessmanTax = businessman.PayTax(6000, 800, 0.3)

selfEmployed = Person('B456')
selfEmployedTax = selfEmployed.PayTax(5000, 0.25)

employee = Employee('C789')
employeeTax = employee.PayTax(23000, 0.5)
employeeRefund = employee.RefundTax(3000)