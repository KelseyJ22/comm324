import numpy as np
import string

def load_train_wordlevel():
	winner = open('winner_train.txt', 'r')
	loser = open('loser_train.txt', 'r')
	x = list()
	y = list()

	print 'loading winner_train.txt...'
	for line in winner:
		split = line.split(' ')
		for word in split:
			if len(x) < 20000:
				x.append(word.lower().translate(None, string.punctuation))
				y.append(1)

	print 'loading loser_train.txt...'
	for line in loser:
		split = line.split(' ')
		for word in split:
			if len(x) < 40000:
				x.append(word.lower().translate(None, string.punctuation))
				y.append(0)

	winner.close()
	loser.close()
	return (x, y)


def load_pronouns():
	pronouns = set(['I', 'i', 'we', 'We', 'You', 'you', 'mine', 'Mine', 'Ours', 'ours', 'yours', 'Yours', 'my', 'My'])
	loser = open('trump_train.txt', 'r')
	winner = open('clinton_train.txt', 'r')
	x1 = list()
	y1 = list()

	print 'loading trump_train.txt...'
	for line in winner:
		split = line.split(' ')
		for word in split:
			if word in pronouns:
				x1.append(word.lower().translate(None, string.punctuation))
				y1.append(1)

	print 'loading clinton_train.txt...'
	for line in loser:
		split = line.split(' ')
		for word in split:
			if word in pronouns:
				x1.append(word.lower().translate(None, string.punctuation))
				y1.append(0)

	winner.close()
	loser.close()

	loser = open('trump_tweets.txt', 'r')
	winner = open('clinton_tweets.txt', 'r')
	x2 = list()
	y2 = list()

	print 'loading trump_tweets.txt...'
	for line in winner:
		split = line.split(' ')
		for word in split:
			if word in pronouns:
				x2.append(word.lower().translate(None, string.punctuation))
				y2.append(1)

	print 'loading clinton_tweets.txt...'
	for line in loser:
		split = line.split(' ')
		for word in split:
			if word in pronouns:
				x2.append(word.lower().translate(None, string.punctuation))
				y2.append(0)

	winner.close()
	loser.close()
	return ((x1, y1), (x2, y2))


def load_train_sentence():
	winner = open('winner_train.txt', 'r')
	loser = open('loser_train.txt', 'r')
	x = list()
	y = list()

	print 'loading winner_train.txt...'
	for line in winner:
		x.append(line.lower().translate(None, string.punctuation))
		y.append(1)

	print 'loading loser_train.txt...'
	for line in loser:
		x.append(line.lower().translate(None, string.punctuation))
		y.append(0)

	winner.close()
	loser.close()
	return (x, y)


def load_train_2016():
	loser = open('clinton_train.txt', 'r')
	winner = open('trump_train.txt', 'r')
	x = list()
	y = list()

	print 'loading clinton_train.txt...'
	written = 0
	for line in winner:
		split = line.split(' ')
		for word in split:
			while(written < 20000):
				x.append(word.lower().translate(None, string.punctuation))
				y.append(1)
				written += 1

	print 'loading trump_train.txt...'
	written = 0
	for line in loser:
		split = line.split(' ')
		for word in split:
			while(written < 20000):
				x.append(word.lower().translate(None, string.punctuation))
				y.append(0)
				written += 1
	winner.close()
	loser.close()
	return (x, y)


def load_test_tweet():
	loser = open('trump_tweets.txt', 'r')
	winner = open('clinton_tweets.txt', 'r')
	x = list()
	y = list()

	print 'loading trump_tweets.txt...'
	for line in winner:
		split = line.split(' ')
		for word in split:
			x.append(word.lower().translate(None, string.punctuation))
			y.append(1)

	print 'loading clinton_tweets.txt...'
	for line in loser:
		split = line.split(' ')
		for word in split:
			x.append(word.lower().translate(None, string.punctuation))
			y.append(0)

	winner.close()
	loser.close()
	return (x, y)



def load_test_wordlevel():
	winner = open('winner_test.txt', 'r')
	loser = open('loser_test.txt', 'r')
	x = list()
	y = list()

	print 'loading winner_test.txt...'
	for line in winner:
		split = line.split(' ')
		for word in split:
			if len(x) < 10000:
				x.append(word.lower().translate(None, string.punctuation))
				y.append(1)

	print 'loading loser_test.txt...'
	for line in loser:
		split = line.split(' ')
		for word in split:
			if len(x) < 20000:
				x.append(word.lower().translate(None, string.punctuation))
				y.append(0)

	winner.close()
	loser.close()
	return (x, y)