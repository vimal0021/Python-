from code1 import Account,Checking,Business,Customer,Savings
d={}
x=input('+=')
x=Customer(x)
x.open_business(1,500)
d[1]=x
print(d[1])
name=input('name')
for c in d:
	if name==c:
		print(c)