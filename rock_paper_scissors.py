print("...rock...")
print("...paper...")
print("...scissors...")
player1 = input("Enter Player 1's choice: ")

#check for valid input and continue
if player1 == "rock" or player1 == "paper" or player1 == "scissors":
	print("*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n")
else:
	print("Please enter 'rock', 'paper', or 'scissors' to play")
	player1 = input("Enter Player 1's choice: ")
	print("*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n*** NO CHEATING ***\n\n")

player2 = input("Enter Player 2's choice: ")

#determine winner
if player2 == "rock" or player2 == "paper" or player2 == "scissors":
	print("Shoot!")
	if player1 == player2:
		print("It's a tie!!! You both lose")
	elif player1 == "rock":
		if player2 == "scissors":
			print("Player 1 wins!!! Rock breaks scissors")
		elif player2 == "paper":
			print("Player 2 wins!!! Paper covers rock")
	elif player1 == "paper":
		if player2 == "rock":
			print("Player 1 wins!!! Paper covers rock")
		elif player2 == "scissors":
			print("Player 2 wins!!! Scissors cut paper")
	elif player1 == "scissors":
		if player2 == "paper":
			print("Player 1 wins!!! Scissors cut paper")
		elif player2 == "rock":
			print("Player 2 wins!!! Rock breaks scissors")
else:
	print("Please enter 'rock', 'paper', or 'scissors' to play")
	player2 = input("Enter Player 2's choice: ")
	if player2 == "rock" or player2 == "paper" or player2 == "scissors":
		print("Shoot!")
		if player1 == player2:
			print("It's a tie!!! You both lose")
		elif player1 == "rock":
			if player2 == "scissors":
				print("Player 1 wins!!! Rock breaks scissors")
			elif player2 == "paper":
				print("Player 2 wins!!! Paper covers rock")
		elif player1 == "paper":
			if player2 == "rock":
				print("Player 1 wins!!! Paper covers rock")
			elif player2 == "scissors":
				print("Player 2 wins!!! Scissors cut paper")
		elif player1 == "scissors":
			if player2 == "paper":
				print("Player 1 wins!!! Scissors cut paper")
			elif player2 == "rock":
				print("Player 2 wins!!! Rock breaks scissors")