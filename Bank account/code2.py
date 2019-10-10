from code1 import Account,Checking,Business,Customer,Savings
xce=0
acct_number1=5

def opening_statement():
	print('Welcome to --Bank')
	print('What would you like to do?')
	print('To create a new account press 1')
	print('To make deposits press 2')
	print('To make withdrawal 3')
	
def checking_open():
	global acct_number1
	name,opendeposit=input('Enter name : '),int(input('How much would like to deposit : '))
	name=Customer(name)
	name.open_checking(acct_number1,opendeposit)
	name.get_deposits()
	acct_number1+=1
	return name

def business_open():
	global acct_number1
	name,opendeposit=input('Enter name : '),int(input('How much would like to deposit : '))
	name=Customer(name)
	name.open_business(acct_number1,opendeposit)
	name.get_deposits()
	acct_number1+=1
	return name

def savings_open():
	global acct_number1
	name,opendeposit=input('Enter name : '),int(input('How much would like to deposit : '))
	name=Customer(name)
	name.open_saving(acct_number1,opendeposit)
	name.get_deposits()
	acct_number1+=1
	return name

def open_account():

	print('\nCreating a new account')
	print('What type of account do you want?')
	type=input('Checking,Business,Savings : ')
	if type.lower()[0]=='c':
		c=checking_open()
		pass
	elif type.lower()[0]=='b':
		c=business_open()
		pass
	elif type.lower()[0]=='s':
		c=savings_open()
		pass
	else:
		pass
	return c

def verification(a):
			name=input('Enter name : ')
			for i in a:
				if i.name==name:
					return i
			return False

def main():
	global acct_number1
	l = [Customer('bob',1)]
	l[0].open_checking(1,500)
	l[0].open_saving(2,50)
	l[0].open_business(3,2500)
	l[0].get_deposits()
	while True:
		opening_statement()
		xce=int(input('Enter your choice :'))
		if xce==1:
			xcx=input('Do you already have a account y/n : ')
			if xcx=='y':
				name1=input('Name : ')
				mlm=-1
				for i in l:
					if i.name==name1:
						mlm+=1
					else:
						pass
				print('mlm = '+str(mlm))
				print(l[mlm].name)
				type=input('Checking,Business,Savings : ')
				deptamt1 = int(input('Deposit amount : '))
				if type.lower()[0]=='c':
					l[mlm].open_checking(acct_number1,deptamt1)
					acct_number1+=1
				elif type.lower()[0]=='s':
					l[mlm].open_saving(acct_number1,deptamt1)
					acct_number1+=1
				elif type.lower()[0]=='b':
					l[mlm].open_business(acct_number1,deptamt1)
					acct_number1+=1
				l[mlm].get_deposits()
			else:
				l.append(open_account())
		elif xce==2:
			type=input('Checking,Business,Savings : ')
			check = verification(l)
			if(check):
				deptamt = int(input('Deposit amount : '))
				axxt_nbr = int(input('Account number : '))
				if type.lower()[0]=='c':
					check.make_deposit( 'C' , axxt_nbr , deptamt)
				elif type.lower()[0]=='s':
					check.make_deposit('S',axxt_nbr,deptamt)
				elif type.lower()[0]=='b':
					check.make_deposit('B',axxt_nbr,deptamt)
				check.get_deposits()

		elif xce==3:
			type=input('Checking,Business,Savings : ')
			check = verification(l)
			if(check):
				deptamt = int(input('Enter withdraw amount : '))
				axxt_nbr = int(input('Account number : '))
				if type.lower()[0]=='c':
					check. make_withdrawal('C',axxt_nbr,deptamt)
				elif type.lower()[0]=='s':
					check. make_withdrawal('S',axxt_nbr,deptamt)
				elif type.lower()[0]=='b':
					check. make_withdrawal('B',axxt_nbr,deptamt)
				check.get_deposits()
		elif xce==4:
			check=verification(l)
			check.get_deposits()

main()
