import numpy as np

a = np.array(['made.', 'I', "don't", 'think', 'that'])
b = np.array(['I', "don't", 'think', 'that', 'even'])
c = np.array(["don't", 'think', 'that', 'even', 'if'])

string = 'made. i dont think that'
print string.split()
x = np.array(string.split())
print a

#a = np.array([1, 2, 3])
#b = np.array([2, 3, 4])
concat = np.vstack((x, b))
print concat.shape
concat = np.vstack((concat, c))
print concat.shape