from ann.Loss.Loss import MSE , CrossEntropy
from ann.Optimizer.Optimizer import SGD , Adam
from ann.Backpropagation.Backpropagation import Backpropagation
from ann.Activation.Activation import Softmax
import numpy as np 

class NeuralNetwork:
    def __init__(self, loss_function="MSE", optimizer="SGD", learning_rate=0.01):
        self.layers = []
        self.loss = MSE() if loss_function == "MSE" else CrossEntropy()
        self.optimizer = SGD(learning_rate) if optimizer == "SGD" else Adam(learning_rate)
        self.backprop = Backpropagation(self.loss, self.optimizer)
    
    def add_layer(self, layer):
        self.layers.append(layer)
    
    def forward(self, X):
        for layer in self.layers:
            X = layer.forward(X)
        return X
    
    def train(self, X, y, epochs=1000):
        for epoch in range(epochs):
            y_pred = self.forward(X)
            loss = self.loss.forward(y, y_pred)
            self.backprop.compute_gradients(y, y_pred, self.layers)
            
            if epoch % 100 == 0:
                print(f"Epoch {epoch}, Loss: {loss}")
    def predict(self, X):
        """Effectue une prédiction sans mise à jour des poids"""
        
        return self.forward(X)

    # def backward(self, y_true, y_pred):
    #     """Gestion spéciale pour Softmax + Cross-Entropy"""
    #     if isinstance(self.layers[-1].activation, Softmax) and isinstance(self.loss, CrossEntropy):
    #         loss_grad = y_pred - y_true  # Simplification de ∇L avec softmax
    #     else:
    #         loss_grad = self.loss.backward(y_true, y_pred)
        
    #     for layer in reversed(self.layers):
    #         loss_grad = layer.backward(loss_grad, self.optimizer.learning_rate)
    
    # def train(self, X, y, epochs=1000):
    #     for epoch in range(epochs):
    #         y_pred = self.forward(X)
    #         loss = self.loss.forward(y, y_pred)
    #         self.backward(y, y_pred)
            
    #         if epoch % 100 == 0:
    #             print(f"Epoch {epoch}, Loss: {loss}")
    
    # def predict(self, X):
    #     """Retourne la classe prédite (argmax)"""
    #     y_pred = self.forward(X)
    #     return np.argmax(y_pred, axis=0)
    
