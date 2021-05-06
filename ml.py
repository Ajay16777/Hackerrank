import sklearn
from sklearn import tree

features = [[1,150],[2,50],[2,60],[1,120],[1,122],[2,80]]
label = [1,2,2,1,1,2]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,label)
print(clf.predict([[1,140]]))