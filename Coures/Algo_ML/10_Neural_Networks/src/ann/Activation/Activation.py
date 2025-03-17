import numpy as np

class ReLU:
    @staticmethod
    def forward(Z):
        return np.maximum(0, Z)
    
    @staticmethod
    def backward(dA, Z):
        return dA * (Z > 0)

class Sigmoid:
    @staticmethod
    def forward(Z):
        return 1 / (1 + np.exp(-Z))
    
    @staticmethod
    def backward(dA, Z):
        A = Sigmoid.forward(Z)
        return dA * A * (1 - A)

class Softmax:
    @staticmethod
    def forward(Z):
        """Applique la fonction softmax aux logits Z"""
        exp_Z = np.exp(Z - np.max(Z, axis=0, keepdims=True))  # Stabilisation numérique
        return exp_Z / np.sum(exp_Z, axis=0, keepdims=True)

    @staticmethod
    def backward(dA, Z):
        """Retourne le gradient de softmax"""
        softmax_output = Softmax.forward(Z)
        return dA * softmax_output * (1 - softmax_output)