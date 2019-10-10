from code1 import Account,Checking,Business,Customer,Savings

bob=Customer('bob',1)
bob.open_checking(1,500)

bob.open_saving(2,50)
bob.open_business(3,2500)
bob.get_deposits()

bob.make_deposit('B',4,500)
bob.get_deposits()