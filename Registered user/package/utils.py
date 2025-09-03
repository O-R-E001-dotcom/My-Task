class Bank:
  def registered_user(self,name, account, balance=0):
    if account.exists:
      self.name = name
      self.account = account
      self.user = True
      self.__pin = 9876
      self.balance = balance
      self.account_number = generate_account_number()
    
  def __verify_pin(self, entered_pin):
    return entered_pin == self.__pin
  def deposit(self, pin, amount):
    if __verify_pin(pin):
      if deposit > 0:
        self.balance += amount
        return f"The amount of {amount} has been deposited into {self.account}. Your balance is {balance}"
      return "Invalid deposit amount"
    return "Incorrect pin"
  def withdraw(self, pin, amount):
    if __verify_pin(pin):
      if amount is > 0 and self.balance >= amount:
        self.balance -= amount
        return f"The amount of {amount} has been withdrawn. Your balance is {self.balance}"
      return "Insufficient fund"
    return "Incorrect pin"
  def transfer(self, pin, amount, recipient):
    if __verify_pin(pin):
      if amount is > 0 and self.balance >= amount:
        self.balance -= amount
        return f"The amount of {amount} has been transferred to {recipient}. New balance is {self.balance}"
      return "Insufficient fund"
    return "Incorrect pin"
  def check_balance(self, pin):
    if __verify_pin(pin):
      return f"Your current account balance is {self.balance}"