numbers = raw_input("Enter a list of numbers separated by spaces:")
numbers_list = list(map(int, numbers.split(",")))
total_sum = sum(numbers_list)
print("Sum of all items in the list:",total_sum)

