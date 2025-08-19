# Using input and integer function
store = {"Book": 6, "Pen": 12, "Bags": 10}
user = input(f"item you want to buy {store}; ").title()
quant = int(input(f"the quantity: {user} : "))
store[user] -= quant
print(store) # {'Book': 4, 'Pen': 12, 'Bags': 10}

