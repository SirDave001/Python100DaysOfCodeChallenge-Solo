def GetPrice(product, quantity):
    SubTotal = PriceDict[product] * quantity
    print(f'{product}: {PriceDict[product]} X {quantity} = ${SubTotal}')
    return SubTotal
    
def GetDiscount(BillPrice, membership):
    discount = 0
    if BillPrice >= 25:
        if membership == 'Gold':
            BillPrice *= 0.75
            discount = 25
        elif membership == 'Silver':
            BillPrice *= 0.85
            discount = 15
        elif membership == 'Bronze':
            BillPrice *= 0.95
            discount = 5
        print(f'{discount} % off for {membership} membership at total price no less than $25')
    return BillPrice

BuyingDict = {'Biscuit': 2, 'Chicken': 3, 'Egg': 20}
PriceDict = {'Biscuit': 2, 'Fish': 3, 'Chicken': 5, 'Cabbage': 2, 'Egg': 0.2}
BillPrice = 0

for key, value in BuyingDict.items():
    BillPrice += GetPrice(key, value)
    
membership = 'Gold'
BillPrice = GetDiscount(BillPrice, membership)
print(f'The total price is ${BillPrice:.2f}.')