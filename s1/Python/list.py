numbers=input("Enter the list of integers,seperated by commas")
#numbers=[int(x) for x in numbers.split(",")]
for number in numbers:
	if number > 100:
		print("over")
	else:
		print(number)
