#label numbers 1 - 20 with descriptors
#4 and 13 are unlucky
#everything else is odd or even

for i in range(1,21):
	if i == 4 or i == 13:
		state = "unlucky"
	elif i % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{i} is {state}")