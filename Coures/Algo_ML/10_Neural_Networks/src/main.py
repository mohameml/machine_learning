import numpy as np 
from ann.Layer.Layer import Layer
from ann.NeuralNetwork.NeuralNetwork import NeuralNetwork
from ann.Activation.Activation import ReLU , Sigmoid

# Création du réseau
nn = NeuralNetwork(loss_function="MSE", optimizer="Adam", learning_rate=0.001)
nn.add_layer(Layer(2, 4, ReLU()))
nn.add_layer(Layer(4, 1, Sigmoid()))

# Données fictives
X = np.random.rand(2, 10)  # 10 échantillons, 2 features
y = np.random.rand(1, 10)  # Valeurs cibles

# Entraînement
nn.train(X, y, epochs=1000)


# Données test
X_test = np.random.rand(2, 5)  # 5 échantillons

# Prédiction
y_pred = nn.predict(X_test)
print("Prédictions:", y_pred)