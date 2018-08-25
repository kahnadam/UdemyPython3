from random import randint

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
print(f"Computer plays {computer}")

#find winner
if player == computer:
		print("It's a tie!!! You both lose")
elif player == "rock":
	if computer == "scissors":
		print("Human wins!!! Rock breaks scissors")
	elif computer == "paper":
		print("Computer wins!!! Paper covers rock")
elif player == "paper":
	if computer == "rock":
		print("Human wins!!! Paper covers rock")
	elif computer == "scissors":
		print("Computer wins!!! Scissors cut paper")
elif player == "scissors":
	if computer == "paper":
		print("Human wins!!! Scissors cut paper")
	elif computer == "rock":
		print("Computer wins!!! Rock breaks scissors")
