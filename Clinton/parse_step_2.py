def initialize():
	distrib = {1800: 0, 1820: 0, 1840: 0, 1860: 0, 1880: 0, 1890: 0, 1900: 0, 1910: 0, 1920: 0, 1940: 0, 1960: 0, 1980: 0, 2000: 0, 'total': 0}
	return distrib


def add_to_distrib(bucket, count, distributions):
	distributions[int(bucket.strip())] += int(count.strip())
	distributions['total'] += int(count.strip())
	return distributions


def normalize(distrib):
	res = list()
	total = distrib['total']
	total.append(float(distrib[1800])/float(total))
	total.append(float(distrib[1820])/float(total))
	total.append(float(distrib[1840])/float(total))
	total.append(float(distrib[1860])/float(total))
	total.append(float(distrib[1880])/float(total))
	total.append(float(distrib[1900])/float(total))
	total.append(float(distrib[1920])/float(total))
	total.append(float(distrib[1940])/float(total))
	total.append(float(distrib[1960])/float(total))
	total.append(float(distrib[1980])/float(total))
	total.append(float(distrib[2000])/float(total))
	return res


def parse():
	f = open('parse_step_1.txt', 'r')
	o = open('distributions.txt', 'w')
	curr_sentence = ''
	distribution = initialize()
	first_time = True
	for line in f:
		split = line.split()
		sentence = split[0]
		bucket = split[1]
		count = split[2]
		if sentence != curr_sentence:
			if not first_time: # done with current sentence
				distrib = normalize(distribution)
				o.write(str(sentence) + '\t' + str(distribution))
				# reset
				sentence = ''
				distribution = initialize()
			else: # starting a new file
				curr_sentence = sentence
				distributions = add_to_distrib(bucket, count, distributions)
				first_time = False
		else: # continuing same sentence
			distributions = add_to_distrib(bucket, count, distributions)


	f.close()
	o.close()

parse()
			