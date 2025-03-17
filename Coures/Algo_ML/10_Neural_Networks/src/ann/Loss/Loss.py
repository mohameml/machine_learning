import numpy as np

class MSE:
    @staticmethod
    def forward(y_true, y_pred):
        return np.mean((y_true - y_pred) ** 2)
    
    @staticmethod
    def backward(y_true, y_pred):
        return 2 * (y_pred - y_true) / y_true.size

class CrossEntropy:
    @staticmethod
    def forward(y_true, y_pred):
        y_pred = np.clip(y_pred, 1e-9, 1 - 1e-9)  # Éviter log(0)
        return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

    @staticmethod
    def backward(y_true, y_pred):
        y_pred = np.clip(y_pred, 1e-9, 1 - 1e-9)
        return (y_pred - y_true) / (y_pred * (1 - y_pred) * y_true.shape[1])
