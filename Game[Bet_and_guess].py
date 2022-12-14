#Main idea of the game is take 20 points.

#Each opponent has 10 points.

#Every turn one of the opponents make a bet from his points.
#The bid must be not more than the minimum of both opponets points.

#The other opponet must guess whether it is even or odd.
#If guess is right he takes the bet, in other case he gives it.



from os import system
from random import randint

#==================================================================================================================
def field(turn, u_p, c_p): # <- turn [who's turn] (1 - user, 2 - computer), u_p - user_points, c_p - computer_points
	system('cls||clear')   # <- clear console
	if turn == 1:
		print('\n >USER: ' + str(u_p) + (' ' * (1 - (u_p // 10))) +'<' + (' ' * 4)  + ' COMPUTER: ' + str(c_p) + '\n') # <- header render
		#-----------------------------------------------------------------------------------------------------
		try:
			bid = int(input('  bid (1 - ' + str(min(u_p, c_p)) + '): ')) # <- bid input with computer and user points limitation
		except:
			bid = 99
		while bid not in range(1, min(u_p, c_p) + 1):
			try:
				bid = int(input('\n  BAD INPUT!\n  bid (1 - ' + str(min(u_p, c_p)) + '): ')) # <- bind input request + bad input message
			except:
				bid = 99
		#--------------------------------------------------------------------------------------(bid input check)
		return 'b' + str(bid) # return value in the 'b5' form (b - bid) first letter allows to determinate that the next turn will make computer
	else:
		print('\n  USER: ' + str(u_p) + (' ' * (1 - (u_p // 10))) + ' ' * 4 + ' >COMPUTER: ' + str(c_p) + ' <' + '\n') # <- header render
		try:#----------------------------------------------------------------------------------------
			guess = int(input('  guess (0-even, 1-odd): ')) # <- guess input request + bad input message
		except:
			guess = 99
		while guess not in [0,1]:
			try:
				guess = int(input('\n  BAD INPUT!\n  guess (0-even, 1-odd): ')) # <- guess input request
			except:
				guess = 99 #---------------------------------------------------------(guess input check)
		return 'g' + str(guess) # return value in the 'g1' form (g - guess) first letter allows to determinate that the next turn will make user
#=========================================(game render and user actions depending on the turn order)
#________________________________________________________________
def comp_act(turn, u_p,c_p,):
	if turn == 1:
		if u_p == 1 or u_p == 19: # <- if user has 1 or 19 points, computer must define that user guess odd numder, because there is no other options
			return 1
		else:
			return randint(0,1)   # <- in other case computer must randomly define 'even' or 'odd'
	else:
		return randint(1, min(u_p, c_p)) # <- bid with user and computer points limitation
#__________________(computer actions depending on the turn order)

turn = randint(1,2)            		# <- who's turn first (1 - user, 2 - computer)
computer_points = user_points = 10  # <- start points
win_points = user_points * 2		# <- win points

game = 'continue'              		# <- game continue condition
#_________________________________________________________________________________
while game != 'game over':

	output = field(turn, user_points, computer_points)

	if output[0] == 'b': # <--------------------------------------------------- actions during user turn
		if comp_act(turn, user_points, computer_points) == int(output[1:]) % 2:
			print('\n\n  COMPUTER guessed!')
			computer_points += int(output[1:])
			user_points-= int(output[1:])
		else:
			print("\n\n  COMPUTER didn't guess!")
			computer_points -= int(output[1:])
			user_points += int(output[1:])
		turn = 2
	else:                # <---------------------------------------------------- actions during computer turn
		comp_bid = comp_act(turn, user_points, computer_points)
		if comp_bid % 2 == int(output[1:]):
			print('\n\n  USER guessed!')
			user_points += comp_bid
			computer_points -= comp_bid
		else:
			print("\n\n  USER didn't guess!")
			user_points -= comp_bid
			computer_points += comp_bid
		turn = 1

	input() # <- iterations cutoff

	if user_points == 0 or user_points == win_points:
		system('cls||clear')
		print('\n   USER: ' + str(user_points) + ' ' * 6 + 'COMPUTER: ' + str(computer_points) + '\n')
		game = 'game over'
else:
	print('   >>>>>>> game over <<<<<<<')
	input()
	#_________________________________________________________________________________(the game)