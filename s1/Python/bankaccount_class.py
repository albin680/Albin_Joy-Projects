class BankAccount:
	def __init__(self, account_number, account_holder_name, account_type, balance=0.0):
		self.account_number = account_number
		self.account_holder_name = account_holder_name
		self.account_type = account_type
		self.balance = balance
		
	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print(f"Deposit of ${amount} successful. New balance: ${self.balance}")
		else:
			print("Invalid deposit amount. Please enter a positive value.")
	
	def withdraw(self,amount):
		if 0 < amount <= self.balance:
			self.balance -= amount
			print(f"Withdrawal of ${amount} successful. New balance: ${self.balance}")
		else:
			print("Invalid withdrawal amount or insufficient funds.")
	
	def display_account_info(self):
		print(f"Account Number: {self.account_number}")
		print(f"Account Holder: {self.account_holder_name}")
		print(f"Account Type: {self.account_type}")
		print(f"Current Balance: ${self.balance}")
		
account1 = BankAccount("123456","John Doe","Savings",1000.0)
account1.display_account_info()
account1.deposit(500.0)
account1.withdraw(200.0)
account1.display_account_info()



