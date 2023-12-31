#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def modele(X, beta0, beta1):
    return beta0 + beta1 * X

def cout(X, y, beta0, beta1):
    m = len(y)
    predictions = modele(X, beta0, beta1)
    cost = (1/(2*m)) * np.sum((predictions - y)**2)
    return cost

def gradient_descent(X, y, beta0, beta1, alpha, num_iterations):
    m = len(y)
    costs = []

    for _ in range(num_iterations):
        predictions = modele(X, beta0, beta1)
        error = predictions - y

        beta0 -= alpha * (1/m) * np.sum(error)
        beta1 -= alpha * (1/m) * np.sum(error * X)

        cost = cout(X, y, beta0, beta1)
        costs.append(cost)

    return beta0, beta1, costs

# Générer des données synthétiques
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)

# Initialiser les paramètres
beta0 = 0
beta1 = 0

# Définir les hyperparamètres
alpha = 0.01
num_iterations = 1000

# Appliquer la descente de gradient
beta0, beta1, costs = gradient_descent(X, y, beta0, beta1, alpha, num_iterations)

# Afficher les résultats
print("Paramètres finaux après descente de gradient :")
print("beta0 =", beta0)
print("beta1 =", beta1)

# # Tracer la courbe d'apprentissage
# plt.plot(range(num_iterations), costs)
# plt.xlabel('Nombre d\'itérations')
# plt.ylabel('Coût')
# plt.title('Courbe d\'apprentissage')
# plt.show()

# Tracer la courbe d'apprentissage
plt.plot(range(num_iterations), costs)
plt.xlabel('Nombre d\'itérations')
plt.ylabel('Coût')
plt.title('Courbe d\'apprentissage')

# Sauvegarder la figure au lieu de l'afficher directement
plt.savefig('courbe_apprentissage.png')

# Afficher la figure si nécessaire
# plt.show()
