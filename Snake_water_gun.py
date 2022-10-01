n=''
print("WELCOME TO THE GAME OF 'SNAKE,WATER AND GUN'")
print()
def name():
	global n
	
	n=input('Enter your name: ')
	print()
	
def rules():
	print('This game will take place between you and the computer')
	print('and will continue till someone completes 6 points')
	print()
	print('And the first one to do so will win')
	print()
	print('"Snake beats Water"')
	print()
	print('"Water beats Gun" and')
	print()
	print('"Gun beats Snake"')
	print()
	print('All the best')
	print()
def main():
	global m
	global n
	import random as r
	if m==0:
		print ("Hi,",n,"here are the rules:-")
		print()
		rules()
	else:
		ask=input('Would you like to repeat the rules(y/n): ')
		print()
		if ask=='y':
			print('Hi',n,'so, the rules were:')
			print()
			rules()
		elif ask=='n':
			print('So, Lets start if you know the rules')
			print()
	
	comp=0
	player=0
	while True:
		if player==6 or comp==6:
			break
		x=r.randrange(1,4)
		print('#########Choices#########')
		print()
		print('CHOICES''\t\tFUNCTIONS')
		print()
		print('1.>''\t\tSNAKE')
		print()
		print('2.>''\t\tWATER')
		print()
		print('3.>''\t\tGun')
		print()
		print('q.>''\t\tQUIT')
		print()
		# print(x)

		a=input('Enter your choice: ')
		print()
		if a=='1' and x==1:
			print('Its a tie')
			print()
			print('The current scores are:')
			print(n,':',player,'\tComputer :',comp)
			print()
		elif a=='1' and x==2:
			print(n,'WON this time :}')
			player+=1
			
			print()
			print('The current scores are:')
			print(n,':',player,'\tComputer :',comp)
			print()
		elif a=='1' and x==3:
			print('You LOST this time :{')
			
			comp+=1
			print()
			print('The current scores are:')
			print(n,':',player,'\tComputer :',comp)
			print()
		elif a=='2' and x==1:
			print('You LOST this time :{')
			
			
			comp+=1
			print()
			print('The current scores are:')
			print(n,':',player,'\tComputer :',comp)
			print()
		elif a=='2' and x==2:
			print('Its a tie')
			print()
			print('The current scores are:')
			print(n,':',player,'\tComputer :',comp)
			print()
		elif a=='2' and x==3:
			print(n,'WON this time :}')
			player+=1
			print()
			print('The current scores are:')
			print(n,':',player,'\tComputer :',comp)
			print()
		elif a=='3' and x==1:
			print(n,'WON this time :}')
			player+=1
			print()
			print('The current scores are:')
			print(n,':',player,'\tComputer :',comp)
			print()
		elif a=='3' and x==2:
			print('You LOST this time :{')
			comp+=1

			print()
			print('The current scores are:')
			print(n,':',player,'\tComputer :',comp)
			print()
		elif a=='3'and x==3:
			print('Its a tie')
			print()
			print('The current scores are:')
			print(n,':',player,'\tComputer :',comp)
			print()
		elif a=='q':
			quit()
		else:
			print('Invalid Input :( ')
			print()
	if player ==6:
		print('CONGRATULATIONS ',n,' YOU WON THE GAME ;}',sep='"')
		print()
	elif comp==6:
		print('OOPS, SORRY ',n,' BUT YOU LOST THIS TIME :(',sep='"')
		print()
		print('BETTER LUCK NEXT TIME')
		print()
	m+=1
	c=input('Would you like to play again(y/n): ')
	choice(c)
m=0

def choice(h):
	if h=='y':
		print()
		t=input('Would you like to change your name(y/n): ')
		print()
		if t=='y':
			name()
			main()

		elif t=='n':
			main()
	elif h=='n':
		print()
		print('Thanks for playing')
		quit()


		
name()
main()

#code ends here
