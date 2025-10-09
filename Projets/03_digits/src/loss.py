import numpy as np 
from abc import ABC , abstractmethod

class Loss(ABC):
    @abstractmethod
    def forward(self, y_true : np.array , y_pred : np.array ) -> float:
        pass

    @abstractmethod
    def backward(self, y_true : np.array, y_pred : np.array) -> float:
        pass


class MSE(Loss):
    def forward(self, y_true : np.array, y_pred : np.array) -> np.array:
        return 0.5 * np.mean((y_pred - y_true)**2)
    def backward(self, y_true : np.array, y_pred : np.array) -> np.array:
        return (y_pred - y_true) / y_true.shape[1]

class CrossEntropy(Loss):
    def forward(self, y_true : np.array, y_pred : np.array) -> np.array:
        m = y_true.shape[1]
        eps = 1e-12  # pour éviter log(0)
        loss = -np.sum(y_true * np.log(y_pred + eps)) / m
        return loss

    def backward(self, y_true : np.array, y_pred : np.array) -> np.array:
        m = y_true.shape[1]
        grad = (y_pred - y_true) / m
        return grad
