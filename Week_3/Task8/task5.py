# Using input and integer function
store = {"Book": 6, "Pen": 12, "Bags": 10}

user = input(f"item you want to buy {store}; ").title()     # Book
quant = int(input(f"the quantity: {user} : "))          # 2
store[user] -= quant
print(f"Before purchase:", store)
print(f"After purchase:", store[user]) # {'Book': 4, 'Pen': 12, 'Bags': 10}



# 