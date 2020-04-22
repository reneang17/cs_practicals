import numpy as np
import numpy.testing as npt

from Games.Utils import shuffle, split_data, Normalizer

def test_shuffle():
    X = np.random.random((5,10))
    y = np.random.random((5,1))
    X_aux, y_aux =  shuffle(X, y)
    assert X_aux.shape == X.shape
    assert y_aux.shape == y.shape
    assert np.sum(X_aux , keepdims= True) == np.sum(X, keepdims= True)
    assert np.sum(y_aux , keepdims= True) == np.sum(y, keepdims= True)

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

def test_split_data():
    X = np.random.random((10,5))
    y = np.random.random((10,1))
    X_train, X_test, y_train, y_test = split_data(X, y, frac=0.7)
    assert np.append(X_train, X_test, axis=0).shape == X.shape
    assert abs(np.sum(X_train) + np.sum(X_test) - np.sum(X))< 10**(-13)
    assert np.append(y_train, y_test, axis=0).shape == y.shape
    assert abs(np.sum(y_train) + np.sum(y_test) - np.sum(y))< 10**(-13)
