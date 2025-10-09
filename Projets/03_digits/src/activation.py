import numpy as np 
from abc import ABC , abstractmethod


class Activation(ABC):
    """
    abstrct class for activation functions 
    """

    @abstractmethod
    def f(self , x : np.ndarray) -> np.ndarray : 
        """
        Calculates the activation function f(x) element by element.
        """
        pass

    @abstractmethod
    def df(self , x : np.ndarray) -> np.ndarray : 
        """
        Calculates function f'(x) element by element.        
        """
        pass 


class Sigmoid(Activation):

    def f(self , x : np.ndarray) -> np.ndarray : 
        return 1 / (1 + np.exp(-x))
    
    def df(self , x : np.ndarray) -> np.ndarray : 
        s = self.f(x)
        return s*(1 -s)
    

class Tanh(Activation):

    def f(self , x : np.ndarray) -> np.ndarray : 
        return np.tanh(x)
    
    def df(self , x : np.ndarray) -> np.ndarray : 
        return 1 - np.tanh(x)**2 
    

class ReLU(Activation):

    def f(self , x : np.ndarray) -> np.ndarray : 
        return np.maximum(0 , x)
    
    def df(self , x) : 
        return (x > 0).astype(float)
    

class Softmax(Activation):
    
    def f(self, x: np.ndarray) -> np.ndarray:
        exp_x = np.exp(x - np.max(x, axis=0, keepdims=True))  # stabilité numérique
        return exp_x / np.sum(exp_x, axis=0, keepdims=True)
    
    def df(self, x: np.ndarray) -> np.ndarray:
        # Ce gradient est géré dans la CrossEntropy, donc on ne l’utilise pas directement.
        return np.ones_like(x)
