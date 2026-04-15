names=input("Enter a list of first names: ")
names=[str(x) for x in names.split(",")]
count=0
for name in names:
	if 'a' in name:
		count += 1
print(count)
