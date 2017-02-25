def get_ngrams(split):
	ngrams = list()
	for i in range(0, len(split)-5): # getting 5-grams
		ngrams.append(split[i:i+5])
	return ngrams


def process():
	dataset = list()
	loser = open('loser_train.txt', 'r')
	winner = open('winner_train.txt', 'r')

	for line in loser:
		split = line.split()
		if len(split) > 1: # success
			label = 'loser'
			strings = get_ngrams(split)

			for string in strings:
				for word in string:
					dataset.append(word + '\t' + label)
				dataset.append('\n') # extra new line for .conll format to indicate new example

	for line in winner:
		split = line.split()
		if len(split) > 1: # success
			label = 'winner'
			strings = get_ngrams(split)

			for string in strings:
				for word in string:
					dataset.append(word + '\t' + label)
				dataset.append('\n') # extra new line for .conll format to indicate new example

	o = open('train.conll', 'w')
	o.write('-DOCSTART- \t O\n\n')
	for line in dataset:
		o.write(line + '\n')
	o.close()
	winner.close()
	loser.close()

process()
