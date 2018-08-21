#label numbers 1 - 20 with descriptors
#4 and 13 are unlucky
#everything else is odd or even

for i in range(1,21):
	if i == 4 or i == 13:
		print(f"{i} is unlucky")
	elif i % 2 == 0:
		print(f"{i} is even")
	else:
		print(f"{i} is odd")