import numpy as np

word_ids = dict()
word_count = 0

def lookup_word(word):
	if word in word_ids:
		word_id = word_ids[word]
	else:
		word_count += 1
		word_ids[word] = word_count
		word_id = word_count
	return word_id


def load_train():
	winner = open('winner_train.txt', 'r')
	loser = open('loser_train.txt', 'r')
	x = list()
	y = list()

	print 'loading winner_train.txt...'
	lines = winner.readlines()
	split = lines.split(' ')
	for word in split:
		word_id = lookup_word(word)
		x.append(word_id)
		y.append(1)

	print 'loading loser_train.txt...'
	lines = loser.readlines()
	split = lines.split(' ')
	for word in split:
		word_id = lookup_word(word)
		x.append(word_id)
		y.append(0)

	print len(x)
	winner.close()
	loser.close()
	return (x, y)


def load_test():
	winner = open('winner_test.txt', 'r')
	loser = open('loser_test.txt', 'r')
	x = list()
	y = list()

	print 'loading winner_test.txt...'
	lines = winner.readlines()
	split = lines.split(' ')
	for word in split:
		word_id = lookup_word(word)
		x.append(word_id)
		y.append(1)

	print 'loading loser_test.txt...'
	lines = loser.readlines()
	split = lines.split(' ')
	for word in split:
		word_id = lookup_word(word)
		x.append(word_id)
		y.append(0)

	print len(x)
	winner.close()
	loser.close()
	return (x, y)