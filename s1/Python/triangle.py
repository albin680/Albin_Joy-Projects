num_row = 9
for i in range(1, num_row + 1):
	num_stars = min(i,num_row - i + 1)
	for j in range(num_stars):
		print("*",end=" ")
	print()
