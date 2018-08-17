animal = input("Enter your favorite animal: ")

#an empty string is inherently false
#that's why we can say --> if animal:
#instead of something else to check if the string is empty
if animal:
	print(animal + " is my favorite too!")
else:
	print("You didn't say anything")