print("...rock...")
print("...paper...")
print("...scissors...")
player_1 = input("Enter Player 1's choice: ")

#check for valid input and continue
if player_1 == "rock" or player_1 == "paper" or player_1 == "scissors":
	print("*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n")
else:
	print("Please enter 'rock', 'paper', or 'scissors' to play")
	player_1 = input("Enter Player 1's choice: ")
	print("*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n")

player_2 = input("Enter Player 2's choice: ")

#determine winner
if player_2 == "rock" or player_2 == "paper" or player_2 == "scissors":
	if player_1 == "rock" and player_2 == "scissors":
		print("Shoot!")
		print("Player 1 wins!!! Rock breaks scissors")
	elif player_1 == "rock" and player_2 == "paper":
		print("Shoot!")
		print("Player 2 wins!!! Paper covers rock")
	elif player_1 == "rock" and player_2 == "rock":
		print("Shoot!")
		print("It's a tie!!! You both lose.")
	elif player_1 == "paper" and player_2 == "scissors":
		print("Shoot!")
		print("Player 2 wins!!! Scissors cut paper")
	elif player_1 == "paper" and player_2 == "paper":
		print("Shoot!")
		print("It's a tie!!! You both lose.")
	elif player_1 == "paper" and player_2 == "rock":
		print("Shoot!")
		print("Player 1 wins!!! Paper covers rock")
	elif player_1 == "scissors" and player_2 == "scissors":
		print("Shoot!")
		print("It's a tie!!! You both lose.")
	elif player_1 == "scissors" and player_2 == "paper":
		print("Shoot!")
		print("Player 1 wins!!! Scissors cut paper")
	elif player_1 == "scissors" and player_2 == "rock":
		print("Shoot!")
		print("Player 2 wins!!! Rock breaks scissors")
else:
	print("Please enter 'rock', 'paper', or 'scissors' to play")
	player_2 = input("Enter Player 2's choice: ")
	if player_2 == "rock" or player_2 == "paper" or player_2 == "scissors":
		if player_1 == "rock" and player_2 == "scissors":
			print("Shoot!")
			print("Player 1 wins!!! Rock breaks scissors")
		elif player_1 == "rock" and player_2 == "paper":
			print("Shoot!")
			print("Player 2 wins!!! Paper covers rock")
		elif player_1 == "rock" and player_2 == "rock":
			print("Shoot!")
			print("It's a tie!!! You both lose.")
		elif player_1 == "paper" and player_2 == "scissors":
			print("Shoot!")
			print("Player 2 wins!!! Scissors cut paper")
		elif player_1 == "paper" and player_2 == "paper":
			print("Shoot!")
			print("It's a tie!!! You both lose.")
		elif player_1 == "paper" and player_2 == "rock":
			print("Shoot!")
			print("Player 1 wins!!! Paper covers rock")
		elif player_1 == "scissors" and player_2 == "scissors":
			print("Shoot!")
			print("It's a tie!!! You both lose.")
		elif player_1 == "scissors" and player_2 == "paper":
			print("Shoot!")
			print("Player 1 wins!!! Scissors cut paper")
		elif player_1 == "scissors" and player_2 == "rock":
			print("Shoot!")
			print("Player 2 wins!!! Rock breaks scissors")
