# ask for age
age = input("How old are you? ")

#make sure they entered an age
if age:
	#convert age input to integer
	age = int(age)
	if age >= 21:
		print("You can enter and can drink!")
	elif age >= 18:
		print("You can enter but you'll be marked as underage")
	else:
		print("You cannot come in")
#prompt to enter an age
else:
	print("Please enter an age!")