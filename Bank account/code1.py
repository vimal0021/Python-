
class Account():
	def __init__(self,acct_nbr,open_depo):
		self.account_number=acct_nbr
		self.balance=open_depo
		
	def __str__(self):
		return f'{self.balance:.2f}'

	def deposit(self,dep_amt):
		self.balance+=dep_amt

	def withdraw(self,wth_amt):
		if (wth_amt>self.balance):
			print('Funds Unavailable')
		else:
			self.balance-=wth_amt

class Checking(Account):
	def __init__(self,acct_nbr,open_depo):
		super().__init__(acct_nbr,open_depo)

	def __str__(self):
		return f'Checking account: #{self.account_number} \n Balance: {Account.__str__(self)}'

class Business(Account):
	def __init__(self,acct_nbr,open_depo):
		super().__init__(acct_nbr,open_depo)

	def __str__(self):
		return f'Business account: #{self.account_number} \n Balance: {Account.__str__(self)}'

class Savings(Account):
	def __init__(self,acct_nbr,open_depo):
		super().__init__(acct_nbr,open_depo)

	def __str__(self):
		return f'Savings account: #{self.account_number} \n Balance: {Account.__str__(self)}'

class Customer():
	def __init__(self,name,PIN=0):
		self.name=name
		self.pin=PIN
		self.accts={'C':[],'S':[],'B':[]}


	def open_checking(self,acct_nbr,open_depo):
		self.accts['C'].append(Checking(acct_nbr,open_depo))

	def open_saving(self,acct_nbr,open_depo):
		self.accts['S'].append(Savings(acct_nbr,open_depo))

	def open_business(self,acct_nbr,open_depo):
		self.accts['B'].append(Business(acct_nbr,open_depo))

	def get_deposits(self):
		total=0
		print(f'Account Name : {self.name}')
		for acct in self.accts['C']:
			print(acct)
			total+=acct.balance
		for acct in self.accts['S']:
			print(acct)
			total+=acct.balance
		for acct in self.accts['B']:
			print(acct)
			total+=acct.balance
		print(f'\nTotal Balnce : {total:.2f}')

	def make_deposit(self,acct_type,acct_nbrr,dept_amt):
		"""
		acct_type - 'C' 'B' 'S'
		acct_nbrr : account number
		"""
		for acct in self.accts[acct_type]:
			if acct.account_number==acct_nbrr:
				acct.deposit(dept_amt)
			else:
				print(f'\n-----\nNo such account exist in {acct_type}\nThese are the currnt accounts ')

	def make_withdrawal(self,acct_type,acct_nbrr,dept_amt):
		"""
		acct_type - 'C' 'B' 'S'
		acct_nbrr : account number
		"""
		for acct in self.accts[acct_type]:
			if acct.account_number==acct_nbrr:
				acct.withdraw(dept_amt)
			else:
				print(f'\n-----\nNo such account exist in {acct_type}\nThese are the currnt accounts ')

