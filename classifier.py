from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
import utils
from sklearn import datasets

dataset = utils.load_data(5)
print 'data loaded'

# fit a logistic regression model to the data
log_reg = LogisticRegression()
naive_bayes = GaussianNB()
knn = KNeighborsClassifier()
decision_tree = DecisionTreeClassifier()
svm = SVC()

log_reg.fit(dataset[0], dataset[1])
naive_bayes.fit(dataset[0], dataset[1])
knn.fit(dataset[0], dataset[1])
decision_tree.fit(dataset[0], dataset[1])
svm.fit(dataset[0], dataset[1])

print(log_reg)
print(naive_bayes)
print(knn)
print(decision_tree)
print(svm)

# make predictions
expected = dataset[1]
log_reg_pred = log_reg.predict(dataset[0])
nb_pred = naive_bayes.predict(dataset[0])
nb_pred = knn.predict(dataset[0])
dec_tree_pred = decision_tree.predict(dataset[0])
svm_pred = svm.predict(dataset[0])

# summarize the fit of the model
print 'Logistic Regression Results:'
print '- - - - - - - - - - - - - - - - - - - - - - - - - - - -'
print(metrics.classification_report(expected, log_reg_pred))
print(metrics.confusion_matrix(expected, log_reg_pred))

print 'Naive Bayes Results:'
print '- - - - - - - - - - - - - - - - - - - - - - - - - - - -'
print(metrics.classification_report(expected, nb_pred))
print(metrics.confusion_matrix(expected, nb_pred))

print 'K-Nearest Neighbors Results:'
print '- - - - - - - - - - - - - - - - - - - - - - - - - - - -'
print(metrics.classification_report(expected, nb_pred))
print(metrics.confusion_matrix(expected, nb_pred))

print 'Decision Tree Results:'
print '- - - - - - - - - - - - - - - - - - - - - - - - - - - -'
print(metrics.classification_report(expected, dec_tree_pred))
print(metrics.confusion_matrix(expected, dec_tree_pred))

print 'Support Vector Machine Results:'
print '- - - - - - - - - - - - - - - - - - - - - - - - - - - -'
print(metrics.classification_report(expected, svm_pred))
print(metrics.confusion_matrix(expected, svm_pred))