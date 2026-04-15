def factorial_loop(n):
	factorial=1
	for i in range(1,n+1):
		factorial *= i
	return factorial
num = int(input("Enter a number:"))
result = factorial_loop(num)
print("factorial of",num,"is",result)

#using recursion
def factorial_recursive(n):
	if n == 0:
		return 1
	else:
		return n * factorial_recursive(n-1)

num = int(input("Enter a number:"))
result = factorial_recursive(num)
print("factorial of",num,"is",result)
