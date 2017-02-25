def get_ngrams(split):
        ngrams = list()
        for i in range(0, len(split)-5): # getting 5-grams
                ngrams.append(split[i:i+5])
        return ngrams

def process():
        dataset = list()
        loser = open('loser_test.txt', 'r')
        winner = open('winner_test.txt', 'r')
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


        o = open('test.conll', 'w')
        o2 = open('dev.conll', 'w')
        o.write('-DOCSTART-\tO\n\n')
        o2.write('_DOCSTART-\tO\n\n')
        count = 0
        for line in dataset:
                if count % 2 == 0:
                        o.write(line + '\n')
                else:
                        o2.write(line + '\n')
                count += 1

        o2.close()
        o.close()
        winner.close()
        loser.close()

process()