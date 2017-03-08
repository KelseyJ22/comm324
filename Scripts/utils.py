import numpy as np

def load_train():
	winner = open('winner_train.txt', 'r')
	loser = open('loser_train.txt', 'r')
	x = list()
	y = list()

	print 'loading winner_train.txt...'
	for line in winner:
		split = line.split(' ')
		for word in split:
			if len(x) < 200000:
				x.append(word)
				y.append(1)

	print 'loading loser_train.txt...'
	for line in loser:
		split = line.split(' ')
		for word in split:
			if len(x) < 400000:
				x.append(word)
				y.append(0)

	winner.close()
	loser.close()
	return (x, y)


def load_test():
	winner = open('winner_test.txt', 'r')
	loser = open('loser_test.txt', 'r')
	x = list()
	y = list()

	print 'loading winner_test.txt...'
	for line in winner:
		split = line.split(' ')
		for word in split:
			if len(x) < 10000:
				x.append(word)
				y.append(1)

	print 'loading loser_test.txt...'
	for line in loser:
		split = line.split(' ')
		for word in split:
			if len(x) < 20000:
				x.append(word)
				y.append(0)

	winner.close()
	loser.close()
	return (x, y)