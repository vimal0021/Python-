import random
print('welcome to rock paper scissors')
scoreP=0
scoreC=0
comp=""

def computerchoice():
	global comp
	xv=random.randint(0,2)
	if xv==0:
		comp='r'
	if xv==1:
		comp='p'
	if xv==2:
		comp='s'

def scoring():
	global scoreP
	global scoreC
	if choice=='r':
		if comp=='p':
			scoreC+=1
		elif comp=='r':
			pass
		else :
			scoreP+=1
	if choice=='p':
		if comp=='s':
			scoreC+=1
		elif comp=='p':
			pass
		else :
			scoreP+=1
	if choice=='s':
		if comp=='r':
			scoreC+=1
		elif comp=='s':
			pass
		else :
			scoreP+=1

def plays():
	play=input('Play again? y/n : ')
	if play=='y':
		playing=True
	elif play=='n':
		playing=False
	else :
		pass

playing = True
while playing:
	choice=input("\nChoose 'r' 'p' 's' 'break' : ")
	if choice.lower()[0]=='b':
		break
	else:
		computerchoice()
		scoring()
		print(f'Player score = {scoreP}')
		print(f'Computer score = {scoreC}')
		if scoreP==10:
			playing=False
			print('Player wins \n')
			plays()
		elif scoreC==10:
			playing=False
			print('Çomputer wins \n')
			plays()
		else:
			pass
