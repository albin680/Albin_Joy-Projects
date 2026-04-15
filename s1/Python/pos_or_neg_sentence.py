positive = ["good","excellent","great","congratulation","yes","happy"]
negative = ["no","not","bad","worst","sad","worse"]
pos_count = 0
neg_count = 0
sentence = input("Enter the sentence: ")
sentence_list = list(map(str,sentence.split(" ")))
for word in sentence_list:
	for pos in positive:
		if word == pos:
			pos_count += 1
	for neg in negative:
		if word == neg:
			neg_count += 1
print("Positive Words: ",pos_count)
print("Negative Words: ",neg_count)
