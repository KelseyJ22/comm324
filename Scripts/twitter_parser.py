def parse():
	f = open('tweets.csv', 'r')
	clinton = list()
	trump = list()
	for line in f:
		split = line.split(':')[0].split(',')
		if len(split) > 3:
			tweet = split[2].rstrip().replace('"', '').replace('@', '').replace('#', '')
			label = split[1]
			if label == 'realDonaldTrump':
				trump.append(tweet)
			else:
				clinton.append(tweet)
	f.close()
	clinton_out = open('clinton_tweets.txt', 'w')
	trump_out = open('trump_tweets.txt', 'w')
	for tweet in trump:
		trump_out.write(tweet)
		trump_out.write('\n')
	for tweet in clinton:
		clinton_out.write(tweet)
		clinton_out.write('\n')

	clinton_out.close()
	trump_out.close()	

parse()