from random import randint

play = "y"

while play == "y":
	random_number = randint(1,10)
	prompt = int(input("Choose a number between 1 and 10: "))
	while prompt != random_number:
		if prompt < random_number:
			print("Too low! Guess again")
			prompt = int(input())
		elif prompt > random_number:
			print("Too high! Guess again")
			prompt = int(input())
	play = input("You got it! Do you want to play again? (y/n) ")

print("Okay! Goodbye!")

#another way to do it, with a break:
"""
from random import randint

random_number = randint(1,10)

while True:
	guess = int(input("Choose a number between 1 and 10: "))
	if guess < random_number:
		print("Too low! Guess again")
	elif guess > random_number:
		print("Too high! Guess again")
	else:
		print("You got it!")
		play_again = input("Do you want to play again? (y/n) ")
		if play_again == "y":
			random_number = randint(1,10)
			guess = None
		else:
			print("Okay! Goodbye!")
			break
"""
