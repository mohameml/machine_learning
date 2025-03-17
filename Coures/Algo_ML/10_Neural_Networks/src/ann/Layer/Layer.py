import numpy as np

class Layer:
    def __init__(self, input_size, output_size, activation):
        self.input_size = input_size
        self.output_size = output_size
        self.activation = activation
        
        # Initialisation des poids et biais
        self.weights = np.random.randn(output_size, input_size) * 0.01
        self.biases = np.zeros((output_size, 1))
    
    def forward(self, X):
        """Applique la transformation linéaire et l'activation"""
        self.input = X
        self.z = np.dot(self.weights, X) + self.biases
        self.output = self.activation.forward(self.z)
        return self.output
    
    def backward(self, d_output, learning_rate):
        """Calcule les gradients et met à jour les paramètres"""
        dz = self.activation.backward(d_output, self.z)
        dw = np.dot(dz, self.input.T) / self.input.shape[1]
        db = np.sum(dz, axis=1, keepdims=True) / self.input.shape[1]
        d_input = np.dot(self.weights.T, dz)
        
        # Mise à jour des paramètres
        self.weights -= learning_rate * dw
        self.biases -= learning_rate * db
        return d_input
