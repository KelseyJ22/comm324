import numpy as np

def pad(array, n):
	while len(array) < n:
		array.append('0')
	return array


def split_data(line, n, x, y, win_lose, index):
	words = line.split() # break into words

	for start_index in range(0, len(words) - n):
		new = np.array(words[start_index:start_index + n])
		#x = np.vstack((x, new))
		x[index:] = new
		y.append(win_lose)
		index += 1

	remainder = len(words) % n
	if remainder > 0:
		last = np.array(pad(words[(len(words) - remainder):], n)) # fill in the last <n-length ngram
		#x = np.vstack((x, last))
		x[index:] = last
		y.append(win_lose)
		index += 1

	return x, y, index


# construct a tuple (x, y) consisting of a n_samples * n_features length
# numpy array x and an array of length n_samples containing the targets y
def load_data(n):
	winner = open('winner.txt', 'r')
	loser = open('loser.txt', 'r')
	
	x = np.chararray([16808, 5], itemsize=10)
	print x.shape
	y = list()
	index = 0
	print 'loading winner.txt'
	for line in winner:
		x, y, index = split_data(line, n, x, y, 1, index)

	print 'loading loser.txt'
	for line in loser:
		x, y, index = split_data(line, n, x, y, 0, index)

	winner.close()
	loser.close()

	print x
	#print y
	return (x, np.array(y))