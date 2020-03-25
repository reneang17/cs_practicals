import pandas as pd
import numpy as np

class Data:

    def __init__(self):
        self.df = None
        self.X = None
        self.y = None
        self.cols = None

    def load_data(self, fname, target, cols = 'all'):
        """
        Load data from file, drop non-numeric columns
        """
        #df = pd.read_csv('./data/USA_Housing.csv')
        self.df = pd.read_csv(fname)
        self.df = self.df.select_dtypes(include=np.number)
        if cols is 'all':
            cols = list(self.df.columns)
            cols.remove(target)

        self.X = np.array(self.df.loc[:,cols])
        self.y = np.array(self.df.loc[:,target]).reshape((len(self.df), 1))

    def normalize(self, axis=0):
        self.X_norm, self.X_mean, self.X_std = self.normalizer(self.X)
        self.y_norm, self.y_mean, self.y_std = self.normalizer(self.y)

    def normalizer(self, x, axis=0):
        x_mean= np.mean(x, axis,keepdims=True)
        x_std = np.std(x,axis=axis, keepdims=True)
        x_norm = (x - x_mean) / x_std
        check_normalization(x, x_norm)
        return  x_norm, x_mean, x_std

    def denormalize(self, x, y, axis=0):
        return  x * self.X_std + self.X_mean ,  y * self.y_std + self.y_mean


    def split_data(self, x, y, p=0.8):
        """
        Randomly split data into test and train
        """
        mask = np.random.rand(y.shape[0]) < p

        return x[mask==True, :], x[mask==False, :], \
            y[mask==True, :], y[mask==False,:]

def check_normalization(x, x_norm):
    assert x.shape == x_norm.shape
    assert np.abs(np.sum(np.mean(x_norm,axis=0))) < 10**(-15)
    dim= x.shape[1]
    assert  (dim- 10**(-15)) <abs( np.sum(np.std(x_norm,axis=0)) ) < (dim+ 10**(-15))
