def parse():
	trump = open('trump_lines.txt', 'w')
	clinton = open('clinton_lines.txt', 'w')
	f = open('2016_general.txt', 'r')
	for line in f:
		split = line.split(' ')
		if split[0] == 'WINNER':
			trump.write(line.split(' ', 1)[1])
		elif split[0] == 'LOSER':
			clinton.write(line.split(' ', 1)[1])
	f.close()
	f = open('2016_rep_primary.txt', 'r')
	for line in f:
		split = line.split(' ')
		if split[0] == 'WINNER':
			trump.write(line.split(' ', 1)[1])
	f.close()
	f = open('2016_dem_primary.txt', 'r')
	for line in f:
		split = line.split(' ')
		if split[0] == 'WINNER':
			clinton.write(line.split(' ', 1)[1])
	f.close()
	f = open('2008_dem_primary.txt', 'r')
	for line in f:
		split = line.split(' ')
		if split[0] == 'LOSER':
			clinton.write(line.split(' ', 1)[1])
	f.close()
	clinton.close()
	trump.close()

parse()