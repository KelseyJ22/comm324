import os

def parse():
	moderator = open('moderator.txt', 'w')
	winner = open('winner.txt', 'w')
	loser = open('loser.txt', 'w')
	audience = open('audience.txt', 'w')

	for filename in os.listdir(os.getcwd()):
		if '.txt' in filename:
			f = open(filename, 'r')
			curr = ''
			curr_type = ''
			for line in f:
				split = line.split(' ')
				label = split[0].strip()
				if label in ['MODERATOR', 'WINNER', 'LOSER', 'AUDIENCE']:
					curr += '\n'
					if curr_type == 'MODERATOR':
						moderator.write(curr)
					elif curr_type == 'WINNER':
						winner.write(curr)
					elif curr_type == 'LOSER':
						loser.write(curr)
					elif curr_type == 'AUDIENCE':
						audience.write(curr)
					else:
						# nothing
						print 'nothing'
					print 'writing ' + curr + ' to ' + curr_type

					curr_type = label
					index = line.find(' ')
					curr = line[index:].rstrip() # cut off label
				else:
					curr += line.rstrip()

			f.close()

	moderator.close()
	winner.close()
	loser.close()
	audience.close()

parse()