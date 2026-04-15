filename = input("Enter a filename; ")
if "." in filename:
	name, extension = filename.split(".")
	print("The extension of the file is: " + extension)
else:
	print("invalid filename format.Please include the file extension(e.g, filename.txt)")
