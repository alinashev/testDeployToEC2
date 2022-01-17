import numpy as np


class Calculator:
    def __init__(self, N):
        self.N = N

    def create(self):
        return np.arange(self.N)
