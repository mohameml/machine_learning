import numpy as np 
from layer import Layer 
from loss import Loss 

class NeuralNetwork :

    def __init__(self , loss : Loss):
        self.layers : list[Layer] = []
        self.loss : Loss = loss

    def add(self , layer : Layer):
        self.layers.append(layer)

    def forward(self , X : np.ndarray) -> np.ndarray : 
        for layer in self.layers : 
            X = layer.forward(X)
        return X 
    
    def backward(self , y_true : np.ndarray , y_pred : np.ndarray , lr : float) :
        grad = self.loss.backward(y_true , y_pred)
        for layer in reversed(self.layers):
            grad = layer.backward(grad ,lr)

    def train(self,
        X : np.ndarray, # shape (n_features : n_0 , n_samples )
        Y : np.ndarray, # shape (n_outputs : n_L , n_samples)
        epochs : int ,
        batch_size : int , 
        lr : float
    ):
        n_samples = X.shape[1]
        for epoch in range(epochs):
            # shuffle the data : 
            indices = np.random.permutation(n_samples)
            X = X[: , indices]
            Y = Y[:,indices]
            # Découpage en mini-batches 
            for k in range(0 , n_samples , batch_size) :
                # Empilement en matrices 2D (features x batch_size)
                X_batch = X[:,k:k+batch_size]
                Y_batch =  Y[:,k:k+batch_size]
                # train : forwrad and backword 
                Y_pred = self.forward(X_batch)
                self.backward(y_true=Y_batch,y_pred=Y_pred,lr=lr)
            loss_value = self.evaluate(X , Y)
            acc = self.accuracy(X ,Y)
            print(f"Epoch {epoch + 1}/{epochs} - Loss : {loss_value:.4f} , - Acc : {acc*100:.2f}%")


    def evaluate(self, X: np.ndarray, Y: np.ndarray) -> float:
        Y_pred = self.forward(X)
        loss_value = self.loss.forward(Y, Y_pred)
        return float(loss_value)
    
    def accuracy(self, X, Y):
        Y_pred = self.forward(X)
        pred_labels = np.argmax(Y_pred, axis=0)
        true_labels = np.argmax(Y, axis=0)
        return np.mean(pred_labels == true_labels)



