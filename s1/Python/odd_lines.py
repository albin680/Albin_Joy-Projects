def copy_odd_lines(input_file_path, output_file_path):
	odd_lines = []
	with open(input_file_path, 'r') as input_file:
		with open(output_file_path, 'w') as output_file:
			for index, line in enumerate(input_file):
				if index % 2 == 0:
					output_file.write(line)
					odd_lines.append(line.strip())
					
	print("Odd lines copied from '{}' to '{}'".format(input_file_path,output_file_path))
	print("Lines read from the file:")
	for line in odd_lines:
		print(line)
	
					
input_file_path = 'example.txt'
output_file_path = 'newexample.txt'

copy_odd_lines(input_file_path, output_file_path)
