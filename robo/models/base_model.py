import numpy as np


class BaseModel(object):
    """
     Abstract base class for all models 
    """
    def __init__(self, *args, **kwargs):
        self.X = None
        self.y = None

    def train(self, X, y):
        self.X = X
        self.y = y

    def predict(self, X):
        raise NotImplementedError()