from random import randint

player_wins = 0
computer_wins = 0
winning_games = 2

while player_wins < winning_games and computer_wins < winning_games:
	#generate computer's choice
	computer = randint(0,2)
	if computer == 0:
		computer = "rock"
	elif computer == 1:
		computer = "paper"
	else:
		computer = "scissors"

	#get player input
	print("...rock...")
	print("...paper...")
	print("...scissors...")
	player = input("Enter your choice: ").lower()
	if player == "quit" or player == "q":
		break
	print(f"Computer plays {computer}")

	#find winner
	if player == computer:
			print("It's a tie!!! You both lose")
	elif player == "rock":
		if computer == "scissors":
			print("Human wins!!! Rock breaks scissors")
			player_wins += 1
			print(f"Human: {player_wins} / Computer: {computer_wins}")
		elif computer == "paper":
			print("Computer wins!!! Paper covers rock")
			computer_wins += 1
			print(f"Human: {player_wins} / Computer: {computer_wins}")
	elif player == "paper":
		if computer == "rock":
			print("Human wins!!! Paper covers rock")
			player_wins += 1
			print(f"Human: {player_wins} / Computer: {computer_wins}")
		elif computer == "scissors":
			print("Computer wins!!! Scissors cut paper")
			computer_wins += 1
			print(f"Human: {player_wins} / Computer: {computer_wins}")
	elif player == "scissors":
		if computer == "paper":
			print("Human wins!!! Scissors cut paper")
			player_wins += 1
			print(f"Human: {player_wins} / Computer: {computer_wins}")
		elif computer == "rock":
			print("Computer wins!!! Rock breaks scissors")
			computer_wins += 1
			print(f"Human: {player_wins} / Computer: {computer_wins}")

if player_wins == winning_games:
	print("You beat the dumb computer!")
elif player_wins == computer_wins:
	print("I guess you quit while it was tied, you jerk quitter")
else:
	print("The computer beat you, you dumb human!")
print(f"Final score... Human: {player_wins} / Computer: {computer_wins}")
