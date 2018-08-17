# ask for age
age = input("How old are you? ")

#make sure they entered an age
if age:
	#convert age input to integer
	age = int(age)
	# 18-20 gets marked as underage
	if age >= 18 and age <= 20:
		print("You can enter but you'll be marked as underage")
	# 21+ gets wristband to drink
	elif age >= 21:
		print("You can enter and can drink!")
	# < 18 is too young
	else:
		print("You cannot come in")
else:
	print("Please enter an age!")