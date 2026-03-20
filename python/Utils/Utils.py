import pandas as pd
import numpy as np

# ********************************#
# Esencial array processing tools.
# Assumes X and y are np arrays,
# where the first axis corresponds
# to the data index
# *********************************

def shuffle(X, y, seed = None):
    """Shuffle X and y arrays along first axis"""
    if seed is not None:
        np.random.seed(seed)
    np.random.shuffle(X)
    np.random.shuffle(y)
    return X, y



class Normalizer():
    def __init__(self, norm_y = False):
        self.X_std = None
        self.X_mean = None
        self.y_std = None
        self.y_mean = None
        self.norm_y = norm_y

    def normalize(self, X, y ):
        X_norm, self.X_mean, self.X_std = self.normalizer(X)
        if self.norm_y:
            y_norm, self.y_mean, self.y_std = self.normalizer(y)
        return X_norm, y_norm

    def normalizer(self, x):
        x_mean= np.mean(x, axis=0, keepdims=True)
        x_std = np.std(x, axis=0, keepdims=True)
        x_norm = (x - x_mean) / x_std
        return  x_norm, x_mean, x_std

    def denormalize(self, X, y):
        X = X * self.X_std + self.X_mean
        if self.norm_y:
            y = y * self.y_std + self.y_mean
        return X, y



def split_data(X, y, frac=0.7):
    """
    Split data into test and train according to first axis
    """
    frac =  int(X.shape[0]* frac)
    X_train, X_test = X[:frac], X[frac:]
    y_train, y_test = y[:frac], y[frac:]

    return X_train, X_test, y_train, y_test

if __name__ == '__main__':

    def test_shuffle():
        X = np.random.random((5,10))
        y = np.random.random((5,1))
        X_aux, y_aux =  shuffle(X, y)
        assert X_aux.shape == X.shape
        assert y_aux.shape == y.shape
        assert np.sum(X_aux , keepdims= True) == np.sum(X, keepdims= True)
        assert np.sum(y_aux , keepdims= True) == np.sum(y, keepdims= True)

    test_shuffle()

    def test_normalization():
        X = np.random.random((5,10))
        y = np.random.random((5,1))
        nrm = Normalizer(norm_y= True)
        X_norm, y_norm = nrm.normalize(X,y)

        assert X.shape == X_norm.shape
        assert y.shape == y_norm.shape

        assert np.abs(np.sum(np.mean(X_norm,axis=0))) < 10**(-15)
        assert np.abs(np.sum(np.mean(y_norm,axis=0))) < 10**(-15)
        dim= X.shape[1]
        assert  (dim- 10**(-15)) <abs( np.sum(np.std(X_norm,axis=0)) ) < (dim+ 10**(-15))
        dim= y.shape[1]
        assert  (dim- 10**(-15)) <abs( np.sum(np.std(y_norm,axis=0)) ) < (dim+ 10**(-15))

    test_normalization()

    def test_split_data():
        X = np.random.random((10,5))
        y = np.random.random((10,1))
        X_train, X_test, y_train, y_test = split_data(X, y, frac=0.7)
        assert np.append(X_train, X_test, axis=0).shape == X.shape
        assert abs(np.sum(X_train) + np.sum(X_test) - np.sum(X))< 10**(-13)
        assert np.append(y_train, y_test, axis=0).shape == y.shape
        assert abs(np.sum(y_train) + np.sum(y_test) - np.sum(y))< 10**(-13)

    test_split_data()
