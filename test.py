from sklearn import datasets
import utils

data = datasets.load_iris()

print data.target
print data.data
print len(data.target)
print len(data.data)

#data2 = utils.load_data(5)

#print data2[1]
#print data2[0]
#print len(data2[1])
#print len(data2[0])