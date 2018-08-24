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
