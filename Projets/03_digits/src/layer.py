import numpy as np 
from activation import Activation



class Layer : 

    def __init__(self , input_dim : int , output_dim : int , activation  : Activation):
        self.input_dim = input_dim
        self.output_dim = output_dim
        self.activation = activation

        # init : 
        limit = np.sqrt(6 / (input_dim + output_dim))
        self.W = np.random.randn(output_dim , input_dim) # np.random.uniform(-limit, limit, (output_dim, input_dim))
        # self.W =  np.random.uniform(-1 , 1 , (output_dim , input_dim))
        self.b = np.random.randn(output_dim , 1) # np.zeros((output_dim , 1)) 
        self.z = None 
        self.a = None 
        self.a_prev = None 
    

    def forward(self , X : np.ndarray) -> np.ndarray :   
        """
        X : (input_dim , batch_size)
        """      
        self.a_prev = X
        self.z = np.dot(self.W , X) + self.b 
        self.a = self.activation.f(self.z) 
        return self.a 
    
    def backward(self , dA : np.ndarray , lr : float) -> np.ndarray : 
        """
            - dA: dérivée de la loss par rapport à l'activation courante (output_dim, batch_size)
        """
        m = dA.shape[1] # batch_size 
        dZ = dA * self.activation.df(self.z) # (output_dim : n_l , batch_size : m)
        dW =  (1/m) * np.dot(dZ , self.a_prev.T) # (output_dim, input_dim)
        db = (1/m) * np.sum(dZ , axis=1 , keepdims=True) # (output_dim , 1)

        # compute the dA to next layer: 
        dX = np.dot(self.W.T, dZ) 

        # update : 
        self.W -= lr*dW 
        self.b -= lr*db

        # return for next layer :
        return dX
