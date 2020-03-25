import numpy as np


class Logistic:
    def __init__(self, X, y):
        self.X = np.concatenate((np.ones(y.shape), X), axis = 1)
        self.y = y
        self.preds = np.zeros(y.shape)
        self.n = y.shape[0]

        self.loss = None
        self.lr = 0.001 # funny, it the lr is too big I don't get convergence
        self.beta = np.random.uniform(low=-1.0, high=1.0, size= (self.X.shape[1], 1))
        self.grad = None

    def sigmoid(self, x):
        return 1/ (1+ np.exp(-x))

    def forward(self):
            self.preds = self.sigmoid(np.dot(self.X, self.beta))

    def backward(self):
        self.grad = np.mean((self.preds - self.y)* self.X,
        axis=0, keepdims=True ).T
        assert self.beta.shape == self.grad.shape
        self.beta = self.beta -  self.lr * self.grad

    def calculate_loss(self, y, preds):
        preds = np.clip(preds, 1e-15, 1 - 1e-15)
        return np.mean(- y * np.log(preds) - (1-y)* np.log(1-preds))

    def fit(self, iters):
        for _ in range(iters):
            self.forward()
            self.backward()
            self.loss = self.calculate_loss(self.y, self.preds)

    def pred(self, X):
        return self.sigmoid(np.dot(X, self.beta))

    def accuracy(self, X, y):
        return np.mean((linear.pred(X) >=0.5) == y)


if __name__ == '__main__':
    from data_prep import Data
    data= Data()
    from sklearn import datasets
    data_ = datasets.load_breast_cancer()

    data.X = np.array(data_["data"])

    data.y = np.array(data_["target"]).reshape((len(data_["target"]), 1))




    feature_names = data_["feature_names"]

    #data.normalize()
    X_train, X_test, y_train, y_test =  data.split_data(data.X, data.y)

    linear= Logistic(X_train, y_train)
    linear.fit(iters=250)

    print('Beta from gradient descent:\n{}'.format(linear.beta))

    print('Training Binary cross entropy:{}'.format(linear.loss))
    X_test = np.concatenate((np.ones(y_test.shape), X_test), axis = 1)

    #print(X_test.shape, X_train.shape)

    print('Testing Binary cross entropy:{}'.format(
    linear.calculate_loss(y_test, linear.pred(X_test))
    ))
    print('Training accuracy:{}'.format(linear.accuracy(linear.X, linear.y)))
    print('Testing accuracy:{}'.format(linear.accuracy(X_test,y_test)))
