import numpy as np 

class Backpropagation:
    def __init__(self, loss_function, optimizer):
        self.loss_function = loss_function
        self.optimizer = optimizer

    def compute_gradients(self, y_true, y_pred, layers):
        """Calcule les gradients et met à jour les poids en utilisant l'optimiseur"""
        loss_grad = self.loss_function.backward(y_true, y_pred)
        t = 1  # Compteur pour Adam
        
        for layer in reversed(layers):
            dz = layer.activation.backward(loss_grad, layer.z)
            dw = np.dot(dz, layer.input.T) / layer.input.shape[1]
            db = np.sum(dz, axis=1, keepdims=True) / layer.input.shape[1]
            loss_grad = np.dot(layer.weights.T, dz)

            self.optimizer.update(layer, dw, db, t)
            t += 1
