import numpy as np


class Linear:
    def __init__(self, X, y):
        self.X = np.concatenate((np.ones(y.shape), X), axis = 1)
        self.y = y
        self.preds = np.zeros(y.shape)
        self.n = y.shape[0]

        self.loss = None
        self.lr = 0.001 # funny, it the lr is too big I don't get convergence
        self.beta = np.random.uniform(low=-1.0, high=1.0, size= (self.X.shape[1], 1))
        self.grad = None



    def forward(self):
            self.preds = np.dot(self.X, self.beta)

    def backward(self):
        self.grad =2*  np.mean((self.preds - self.y)* self.X,
        axis=0, keepdims=True ).T

        self.beta = self.beta -  self.lr * self.grad

    def calculate_loss(self, y, preds):
        return np.mean( (y - preds)**2 )

    def fit(self, iters):
        for _ in range(iters):
            self.forward()
            self.backward()
            self.loss = self.calculate_loss(self.y, self.preds)

    def fit_exact(self):
        self.beta_exact = np.linalg.solve(np.dot(self.X.T,self.X),
        np.dot(self.X.T,self.y))

    def pred(self, X):
        return np.dot(X, self.beta)

    def pred_exact(self, X):
        return np.dot(X, self.beta_exact)


if __name__ == '__main__':
    from data_prep import Data
    data= Data()

    data.load_data('./data/USA_Housing.csv', 'Price')

    data.normalize(norm_target = True)
    X_train, X_test, y_train, y_test =  data.split_data(data.X_norm, data.y_norm)

    linear= Linear(X_train, y_train)
    linear.fit(iters=10000)
    linear.fit_exact()

    print('Beta from gradient descent:\n{}'.format(linear.beta))
    print('Beta from matrix inversion:\n{}'.format(linear.beta_exact))

    print('Training MSE (Gradient descent):{}'.format(linear.loss))

    # Need to make uniform convention for bias matrix
    X_test = np.concatenate((np.ones(y_test.shape), X_test), axis = 1)

    print('Test MSE (Gradient descent):{}'.format(
    linear.calculate_loss(y_test, linear.pred(X_test))
    ))
    print('Test MSE (Matrix inversion):{}'.format(
    linear.calculate_loss(y_test, linear.pred_exact(X_test))
    ))
