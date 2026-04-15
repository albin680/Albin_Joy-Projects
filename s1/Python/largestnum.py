num1=input("Enter First Number")
num2=input("Enter Second Number")
num3=input("Enter the third Number")
if num1 > num2:
	if num1 > num3:
		print "Largest Number is"+str(num1)
	else:
		print "Largest Number is"+str(num3)
else:
	if num2 > num3:
		print "Largest Number is"+str(num2)
	else:
		print "Largest Number is"+str(num3)
		

