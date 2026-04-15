def write_to_file(file_path, content):
	with open(file_path, 'w') as file:
		file.write(content)
		
def read_file_to_list(file_path):
	lines = []
	with open(file_path, 'r') as file:
		for line in file:
			lines.append(line.strip())
	return lines
	
file_path = 'example.txt'

content_to_write = """Line 1: This is the first line.
Line 2: This is the second line.
Line 3: This is the third line.
Line 4: This is the fourth line.
Line 5: This is the fifth line.
Line 6: This is the sixth line.
Line 7: This is the seventh line.
Line 8: This is the eighth line.
Line 9: This is the nineth line.
Line 10: This is the tenth line."""

write_to_file(file_path, content_to_write)
lines_read = read_file_to_list(file_path)

print("Lines read from the file:")
for line in lines_read:
	print(line)

