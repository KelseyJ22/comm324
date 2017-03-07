from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import utils
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import numpy as np

count_vect = CountVectorizer()
log_reg = LogisticRegression()
naive_bayes = GaussianNB()
knn = KNeighborsClassifier()
decision_tree = DecisionTreeClassifier()
svm = SVC()

train = utils.load_train()
test = utils.load_test()

train_counts = count_vect.fit_transform(train[0])
transformer = TfidfTransformer(use_idf=False).fit(train_counts)
train_data = transformer.transform(train_counts).toarray()
test_counts = count_vect.transform(test[0])
test_data = transformer.transform(test_counts).toarray()
dense = np.array(train[1])
expected = list(map(int, test[1]))

log_reg.fit(train_data, dense)
print(log_reg)
log_reg_pred = log_reg.predict(test_data)
print 'Logistic Regression Results:'
print '- - - - - - - - - - - - - - - - - - - - - - - - - - - -'
print(metrics.classification_report(expected, log_reg_pred))
print(metrics.confusion_matrix(expected, log_reg_pred))


naive_bayes.fit(train_data, dense)
print(naive_bayes)
nb_pred = naive_bayes.predict(test_data)
print 'Naive Bayes Results:'
print '- - - - - - - - - - - - - - - - - - - - - - - - - - - -'
print(metrics.classification_report(expected, nb_pred))
print(metrics.confusion_matrix(expected, nb_pred))


knn.fit(train_data, dense)
print(knn)
knn_pred = knn.predict(test_data)
print 'K-Nearest Neighbors Results:'
print '- - - - - - - - - - - - - - - - - - - - - - - - - - - -'
print(metrics.classification_report(expected, knn_pred))
print(metrics.confusion_matrix(expected, knn_pred))


decision_tree.fit(train_data, dense)
print(decision_tree)
dec_tree_pred = decision_tree.predict(test_data)
print 'Decision Tree Results:'
print '- - - - - - - - - - - - - - - - - - - - - - - - - - - -'
print(metrics.classification_report(expected, dec_tree_pred))
print(metrics.confusion_matrix(expected, dec_tree_pred))


svm.fit(train_data, dense)
print(svm)
svm_pred = svm.predict(test_data)
print 'Support Vector Machine Results:'
print '- - - - - - - - - - - - - - - - - - - - - - - - - - - -'
print(metrics.classification_report(expected, svm_pred))
print(metrics.confusion_matrix(expected, svm_pred))