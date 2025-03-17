import numpy as np

class SGD:
    def __init__(self, learning_rate=0.01):
        self.learning_rate = learning_rate
    
    def update(self, layer, dw, db):
        layer.weights -= self.learning_rate * dw
        layer.biases -= self.learning_rate * db

class Adam:
    def __init__(self, learning_rate=0.001, beta1=0.9, beta2=0.999, epsilon=1e-8):
        self.learning_rate = learning_rate
        self.beta1 = beta1
        self.beta2 = beta2
        self.epsilon = epsilon
        self.m_w, self.v_w = {}, {}
        self.m_b, self.v_b = {}, {}
    
    def update(self, layer, dw, db, t):
        if layer not in self.m_w:
            self.m_w[layer] = np.zeros_like(dw)
            self.v_w[layer] = np.zeros_like(dw)
            self.m_b[layer] = np.zeros_like(db)
            self.v_b[layer] = np.zeros_like(db)
        
        # Moments de premier et second ordre
        self.m_w[layer] = self.beta1 * self.m_w[layer] + (1 - self.beta1) * dw
        self.v_w[layer] = self.beta2 * self.v_w[layer] + (1 - self.beta2) * (dw ** 2)
        self.m_b[layer] = self.beta1 * self.m_b[layer] + (1 - self.beta1) * db
        self.v_b[layer] = self.beta2 * self.v_b[layer] + (1 - self.beta2) * (db ** 2)

        # Correction du biais
        m_w_hat = self.m_w[layer] / (1 - self.beta1 ** t)
        v_w_hat = self.v_w[layer] / (1 - self.beta2 ** t)
        m_b_hat = self.m_b[layer] / (1 - self.beta1 ** t)
        v_b_hat = self.v_b[layer] / (1 - self.beta2 ** t)

        # Mise à jour des paramètres
        layer.weights -= self.learning_rate * m_w_hat / (np.sqrt(v_w_hat) + self.epsilon)
        layer.biases -= self.learning_rate * m_b_hat / (np.sqrt(v_b_hat) + self.epsilon)
