from Models import *
import time
import seaborn as sns
import matplotlib.pyplot as plt
from Helper import *

########  Loading File  ########
data=pd.read_csv("my_new_data3.csv", header=0)
data.dropna(how='any',inplace=True)

X=data[['date', 'type', 'airline', 'source', 'destination', 'time_taken', 'stop', 'dep_time']]
Y=data['price']


########  Linear Regression model  ########
before = time.time()
linear_model = Model(True, X, Y, test_size=0.3)
linear_model.createModel(Type.LinearRegression)
after = time.time()
linear_model.displayInfo("Linear regression", int(after-before))

########  Polynomial Regression model  ########
before = time.time()
poly_model = Model(True, X, Y, test_size=0.3)
poly_model.createModel(Type.PolynomialRegression, degree=5)
after = time.time()
poly_model.displayInfo("Polynomial regression", int(after-before))

# Correlation #
plt.subplots(figsize=(16, 12))
corr = data.corr()
sns.heatmap(corr, annot=True)
plt.show()


from Models import *
from sklearn.tree import DecisionTreeClassifier
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

# loading the iris dataset
iris = datasets.load_iris()

# X -> features, y -> label
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2, shuffle=False)
# dividing X, y into train and test data
dt_Model = Model(True, X, y, test_size=0.2, shuffle=False)
dt_Model.createModel(modelType=Type.DecisionTreeClassification, maxDepth=2)
dt_Model.SaveModel("DTModel", Type.DecisionTreeClassification)

data = Model.LoadModel("DTModel_DecisionTreeClassification.sav")

i = 0
# print("data:"+str(data.train_score))
print(dt_Model.train_score)
data.test(X_train, y_train)
print(data.test_score)

print("Test")
print(dt_Model.test_score)
print(data.test(X_test, y_test))
print(data.test_score)
print("-"*50)

dtree_model = DecisionTreeClassifier(max_depth=2).fit(X_train, y_train)
dtree_predictions = dtree_model.predict(X_test)
# creating a confusion matrix
cm = confusion_matrix(y_test, dtree_predictions)
print(round(dtree_model.score(X_train, y_train), 2))
print(round(dtree_model.score(X_test, y_test), 2))
