singular_pronouns = ['I', 'me', 'my', 'mine']
collective_pronouns = ['we', 'ours', 'us']
def get_pronoun_counts():
	total_words = 0
	singular = 0
	collective = 0
	f = open('loser_train.txt')
	for line in f:
		words = line.split(' ')
		for word in words:
			word = word.strip()
			print word
			if word in singular_pronouns:
				singular += 1
			elif word in collective_pronouns:
				collective += 1
			total_words += 1
	f.close()
	f2 = open('loser_test.txt')
	for line in f2:
		words = line.split(' ')
		for word in words:
			word = word.strip()
			print word
			if word in singular_pronouns:
				singular += 1
			elif word in collective_pronouns:
				collective += 1
			total_words += 1
	print 'Singular pronoun percent: ' + str(float(singular)/float(total_words))
	print 'Collective pronoun percent: ' + str(float(collective)/float(total_words))
	f2.close()

get_pronoun_counts()