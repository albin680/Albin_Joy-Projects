def find_longest_word(word_list):
	longest_word = ""
	for word in word_list:
		if len(word) > len(longest_word):
			longest_word = word
	return len(longest_word)
word_list = input("Enter a list of words separated by spaces: ").split(" ")
longest_word_length = find_longest_word(word_list)
print("Length of the longest word:",longest_word_length)
