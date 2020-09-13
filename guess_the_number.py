print('WELCOME TO THE "GAME OF GUESSING NUMBERS"')
print()

def choice():
	global g
	global l	
	print('Type "easy", "med" or "hard"')
	print()
	l=input('In which mode would you like to play the game: ')
	print()
	if l =='med':
		if g==0:
			g+=1
		game_med()
	elif l=='easy':
		if g==0:
			g+=1
		game_easy()
	elif l=='hard':
		if g==0:
			g+=1
		game_hard()
	
def play_med():
	global y
	b=input('WOULD YOU LIKE TO PLAY AGAIN(y/n): ')
	print()
	if b=='y':
		y+=1
		game_med()

	elif b=='n':
        
		quit()
		
def play_easy():
	global y
	b=input('WOULD YOU LIKE TO PLAY AGAIN(y/n): ')
	print()
	if b=='y':
		y+=1
		game_easy()

	elif b=='n':
        
		quit()

def play_hard():
	global y
	b=input('WOULD YOU LIKE TO PLAY AGAIN(y/n): ')
	print()
	if b=='y':
		y+=1
		game_hard()

	elif b=='n':
        
		quit()
			


def game_med():	
	global y
	global g
	import random as r
	if g!=1:
		g-=1
		choice()	
	x=r.randrange(1,101)
	if y==0:
		
		print('SO THE RULES ARE:')
		print()
	def rules_med():
				
			global y
			print('A RANDOM NUMBER BETWEEN 1 AND 100 IS SELECTED BY THE SYSTEM ')
			print()
			print('YOUR TASK IS TO GUESS THE NUMBER, YOU WILL GET 7 CHANCES FOR THIS')
			print()
			print('ALL THE BEST AND HAVE FUN :)')
			print()	
	if y ==0:

		rules_med()

	else:
		print("WElCOME BACK, YOU KNOW THE RULES DON'T YOU")
		print()
		z=input('WOULD YOU LIKE TO REPEAT THEM(y/n): ')
		print()
		if z=='y':
			rules_med()
		elif z=='n':
			print('SO , YOU KNOW THE RULES. THEN WHY WASTE TIME LETS START :}')
			print()
	# print(x)
	i=1
	while i<8:
		a= int(input('Enter your choice: '))
		print()
		j=8-i
		if j!=0:

			if a==x:
				print('WELLDONE, YOU WON THE GAME ;)')
				print()
					
					
				break
			elif a<x :
				print("The entered number is smaller than the system's number")
				print()
					
				if j >1:
					print("Don't give up, try again")
					print()
					print ('You still have', j-1,'tries left, keep trying')
					print()
						
				i+=1
			elif a>x and a<=100:
				print("The entered number is greater than the system's number")
				print()
					
				if j >1:
					print("Don't give up, try again")
					print()
					print ('You still have', j-1,'tries left, keep trying')
					print()
						
					
				i+=1

			elif a>100:
				print('You are exceeding the value limit ')
				print()
				if j >1:
					print('You now have',j-1,'tries left, keep trying')
					print()
					
				i+=1
	if i==8:
			print('SORRY, BUT YOU LOST :{')
			print()
			print('THE NUMBER WAS:',x)
			print()
			print('BETTER LUCK NEXT TIME')
			print()
	g+=1
	play_med()
		

def game_easy():	
	global y
	global g
	global v
	import random as r
	if g!=1:
		g-=1
		choice()	
	x=r.randrange(1,51)
	if y==0:
		
		print('SO THE RULES ARE:')
		print()
	def rules_easy():
				
			global y
			print('A RANDOM NUMBER BETWEEN 1 AND 50 IS SELECTED BY THE SYSTEM ')
			print()
			print('YOUR TASK IS TO GUESS THE NUMBER, YOU WILL GET 9 CHANCES FOR THIS')
			print()
			print('ALL THE BEST AND HAVE FUN :)')
			print()	
	if y ==0:

		rules_easy()

	else:
		print("WElCOME BACK, YOU KNOW THE RULES DON'T YOU")
		print()
		z=input('WOULD YOU LIKE TO REPEAT THEM(y/n): ')
		print()
		if z=='y':
			rules_easy()
		elif z=='n':
			print('SO , YOU KNOW THE RULES. THEN WHY WASTE TIME LETS START :}')
			print()
	# print(x)
	i=1
	while i<10:
		a= int(input('Enter your choice: '))
		print()
		j=10-i
		if j!=0:

			if a==x:
				print('WELLDONE, YOU WON THE GAME ;)')
				print()
					
					
				break
			elif a<x :
				print("The entered number is smaller than the system's number")
				print()
					
				if j >1:
					print("Don't give up, try again")
					print()
					print ('You still have', j-1,'tries left, keep trying')
					print()
						
				i+=1
			elif a>x and a<=50:
				print("The entered number is greater than the system's number")
				print()
					
				if j >1:
					print("Don't give up, try again")
					print()
					print ('You still have', j-1,'tries left, keep trying')
					print()
						
					
				i+=1

			elif a>50:
				print('You are exceeding the value limit ')
				print()
				if j >1:
					print('You now have',j-1,'tries left, keep trying')
					print()
					
				i+=1
	if i==10:
			print('SORRY, BUT YOU LOST :{')
			print()
			print('THE NUMBER WAS:',x)
			print()
			print('BETTER LUCK NEXT TIME')
			print()
	g+=1
	play_easy()
	
def game_hard():	
	global y
	global g
	import random as r
	if g!=1:
		g-=1
		choice()
		
	x=r.randrange(1,101)
	if y==0:
		
		print('SO THE RULES ARE:')
		print()
	def rules_hard():
				
			global y
			print('A RANDOM NUMBER BETWEEN 1 AND 100 IS SELECTED BY THE SYSTEM ')
			print()
			print('YOUR TASK IS TO GUESS THE NUMBER, YOU WILL GET 5 CHANCES FOR THIS')
			print()
			print('ALL THE BEST AND HAVE FUN :)')
			print()	
	if y ==0:

		rules_hard()

	else:
		print("WElCOME BACK, YOU KNOW THE RULES DON'T YOU")
		print()
		z=input('WOULD YOU LIKE TO REPEAT THEM(y/n): ')
		print()
		if z=='y':
			rules_hard()
		elif z=='n':
			print('SO , YOU KNOW THE RULES. THEN WHY WASTE TIME LETS START :}')
			print()
	# print(x)
	i=1
	while i<6:
		a= int(input('Enter your choice: '))
		print()
		j=6-i
		if j!=0:

			if a==x:
				print('WELLDONE, YOU WON THE GAME ;)')
				print()
					
					
				break
			elif a<x :
				print("The entered number is smaller than the system's number")
				print()
					
				if j >1:
					print("Don't give up, try again")
					print()
					print ('You still have', j-1,'tries left, keep trying')
					print()
						
				i+=1
			elif a>x and a<=100:
				print("The entered number is greater than the system's number")
				print()
					
				if j >1:
					print("Don't give up, try again")
					print()
					print ('You still have', j-1,'tries left, keep trying')
					print()
						
					
				i+=1

			elif a>100:
				print('You are exceeding the value limit ')
				print()
				if j >1:
					print('You now have',j-1,'tries left, keep trying')
					print()
					
				i+=1
	if i==6:
			print('SORRY, BUT YOU LOST :{')
			print()
			print('THE NUMBER WAS:',x)
			print()
			print('BETTER LUCK NEXT TIME')
			print()
	g+=1
	play_hard()
y=0
g=0	
v=0
l=''
choice()
