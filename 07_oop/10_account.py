class Bank:
  def __init__(self):
    self.customers = {}

  def create_account(self, account_number,initial_balance =0):
    if account_number in self.customers:
      print("Account already exists")
    else:
      self.customers[account_number] = initial_balance
      print("Account created successfully")

  def make_deposit(self, account_number, amount):
    if account_number in self.customers:
      self.customers[account_number] += amount
      print("Amount deposited successfully")
    else:
      print("Account does not exist")

  def make_widthdrawal(self, account_number, amount):
    if account_number in self.customer:
      if self.customers[account_number] >= amount:
        self.customers[account_number] -= amount
        print("Amount withdrawn successfully")
      else:
        print("Insufficient balance")
    else:
      print("Account does not exist")

  def check_balance(self,account_number):
    if account_number in self.customers:
      balance = self.customers[account_number]
      print(f"Your balance is {balance}")
    else:
      print("Account does not exist")

bank = Bank()

acno1 = "SB-123"
damt1 = 1000
print("New A/C No: ", acno1, "Deposit Amount: ", damt1)
bank.create_account(acno1, damt1)

acno2 = "SB-124"
damt2 = 2000
print("New A/C No: ", acno2, "Deposit Amount: ", damt2)
bank.create_account(acno2, damt2)

acno3 = "SB-125"
damt3 = 3000
print("New A/C No: ", acno3, "Deposit Amount: ", damt3)
bank.create_account(acno3, damt3)

wamt1 = 600
print("A/C No: ", acno1, "Withdrawal Amount: ", wamt1)

wamt2 = 700
print("A/C No: ", acno2, "Withdrawal Amount: ", wamt2)

print("A/C No: ", acno2)
bank.check_balance(acno2)

print("A/C No: ", acno1)
bank.check_balance(acno1)

wamt3 = 1200
print("A/C No: ", acno3, "Withdrawal Amount: ", wamt3)
bank.make_widthdrawal(acno3, wamt3)

acno3 = "SB-125"
print("A/C No: ", acno3)
bank.check_balance(acno3)