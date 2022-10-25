import enum
import pickle
import numpy as np
from typing import Union
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures


class Type(enum.Enum):
    StoredModel = -1
    LinearRegression = 0
    PolynomialRegression = 1
    LassoRegression = 2
    RidgeRegression = 3
    LogisticRegression = 4
    SVCClassification = 5
    DecisionTreeClassification = 6


class Model:
    def __init__(self, newModel: bool = True ,X=None, Y=None, test_size=0.2, shuffle: bool = False, model = None):
        if newModel:
            self.__X_train, self.__X_test, self.__Y_train, self.__Y_test \
                = train_test_split(X, Y, test_size=test_size, shuffle=shuffle)
        else:
            self.__model = model

    def createModel(self, modelType: Type = Type.StoredModel, degree: int = 1, c: float = 0.1, kernel: str = 'poly',
                    alpha: int = 50, gamma: float = 0.8, multiClass: str = 'multinomial', solver: str = 'lbfgs',
                    fitIntercept: bool = False, maxDepth: int = 0, randomState: int = 0,
                    maxFeatures: Union[int, float, None] = None, loadedModel=None) -> None:
        if modelType == Type.PolynomialRegression:
            model = self.__PolynomialModel(degree)
        elif modelType == Type.LassoRegression:
            model = self.__lassoRegression(alpha)
        elif modelType == Type.RidgeRegression:
            model = self.__ridgeRegression(alpha)
        elif modelType == Type.LogisticRegression:
            model = self.__LogisticModel(multiClass, solver, fitIntercept)
        elif modelType == Type.SVCClassification:
            model = self.__SVCModel(c, kernel, degree, gamma)
        elif modelType == Type.DecisionTreeClassification:
            model = self.__DTModel(maxDepth, randomState, maxFeatures)
        elif loadedModel is not None:
            model = loadedModel
        else:
            model = self.__linear_regression()
        self.__assigningAttributes(model)

    def __lassoRegression(self, alpha: int) -> linear_model:
        lasso_reg = linear_model.Lasso(alpha=alpha)
        lasso_reg.fit(self.__X_train, self.__Y_train)
        return lasso_reg

    def __ridgeRegression(self, alpha: int) -> linear_model:
        ridge_reg = linear_model.Ridge(alpha=alpha)
        ridge_reg.fit(self.__X_train, self.__Y_train)
        return ridge_reg

    def __linear_regression(self) -> linear_model:
        cls = linear_model.LinearRegression()
        cls.fit(self.__X_train, self.__Y_train)
        return cls

    def __PolynomialModel(self, degree: int) -> linear_model:
        polyFeatures = PolynomialFeatures(degree=degree)
        self.__X_train = polyFeatures.fit_transform(self.__X_train)
        self.__X_test = polyFeatures.fit_transform(self.__X_test)
        return self.__linear_regression()

    def __LogisticModel(self, multiClass: str, solver: str, fitIntercept: bool) -> LogisticRegression:
        log_Model = LogisticRegression(multi_class=multiClass, solver=solver, fit_intercept=fitIntercept)
        log_Model.fit(self.__X_train, self.__Y_train)
        return log_Model

    def __SVCModel(self, c: float, ker: str, d: int, g: float) -> SVC:
        SVC_Model = SVC(C=c, kernel=ker, degree=d, gamma=g)
        SVC_Model.fit(self.__X_train, self.__Y_train)
        return SVC_Model

    def __DTModel(self, maxDepth: int, randomState: int, maxFeatures: Union[int, float, None]) -> \
            DecisionTreeClassifier:
        DT_Model = DecisionTreeClassifier(max_depth=maxDepth, random_state=randomState, max_features=maxFeatures)
        DT_Model.fit(self.__X_train, self.__Y_train)
        return DT_Model

    def SaveModel(self, fileName: str, modelType: Type) -> None:
        modelStr = str(modelType).split(".")
        fileName = "{}_{}.sav".format(fileName, modelStr[1])
        pickle.dump(self.__model, open(fileName, 'wb'))

    @staticmethod
    def LoadModel(fileName: str):
        loaded_Model = pickle.load(open(fileName, 'rb'))
        return Model(False, model = loaded_Model)

    def __assigningAttributes(self, model) -> None:
        self.train_score = model.score(self.__X_train, self.__Y_train)
        self.__model = model
        self.test(self.__X_test, self.__Y_test)
        # self.coef = model.coef

    def test(self, X_test, Y_test):
        self.test_score = self.__model.score(X_test, Y_test)
        self.prediction = self.__model.predict(X_test)
        self.MSE = mean_squared_error(np.asarray(Y_test), self.prediction)