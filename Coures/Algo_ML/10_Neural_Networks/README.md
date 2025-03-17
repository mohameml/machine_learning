## 🤖 **Réseaux de Neurones (Neural Networks)**

Les **réseaux de neurones artificiels (ANNs - Artificial Neural Networks)** sont des **modèles d'apprentissage automatique inspirés du cerveau humain**. Ils sont utilisés dans plusieurs applications comme la classification, la régression, la reconnaissance d'images et le traitement du langage naturel.

---

## 🔹 **Structure d'un Réseau de Neurones**

Un réseau de neurones est composé de plusieurs couches de **neurones artificiels** :

1️⃣ **Couche d'entrée (Input Layer)** : Reçoit les données d'entrée.  
2️⃣ **Couches cachées (Hidden Layers)** : Effectuent des calculs et extraient des caractéristiques.  
3️⃣ **Couche de sortie (Output Layer)** : Fournit le résultat final (classe ou valeur prédite).

📌 **Chaque neurone applique une fonction d'activation pour introduire de la non-linéarité**.

---

## 🔥 **Fonctionnement d'un Neurone**

Un neurone artificiel prend un vecteur d’entrée \( X = (x_1, x_2, ..., x_n) \) et effectue un calcul sous forme de somme pondérée :

\[
z = w_1 x_1 + w_2 x_2 + ... + w_n x_n + b
\]

Puis, il applique une **fonction d'activation** \( f(z) \) pour produire une sortie :

\[
y = f(z)
\]

🔹 **Exemples de fonctions d'activation :**  
✅ **Sigmoïde** : \( f(z) = \frac{1}{1 + e^{-z}} \) (utilisée en classification binaire).  
✅ **ReLU (Rectified Linear Unit)** : \( f(z) = \max(0, z) \) (réseau profond).  
✅ **Softmax** : Pour la classification multi-classes.

---

## 📜 **Exemple en Python : Réseau de Neurones avec Keras (Classification)**

```python
import numpy as np
import tensorflow as tf
from tensorflow import keras
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Génération d'un dataset en forme de lune
X, y = make_moons(n_samples=1000, noise=0.2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Création du modèle
model = keras.Sequential([
    keras.layers.Dense(10, activation="relu", input_shape=(2,)),  # Couche cachée avec 10 neurones
    keras.layers.Dense(10, activation="relu"),  # Deuxième couche cachée
    keras.layers.Dense(1, activation="sigmoid")  # Couche de sortie (classification binaire)
])

# Compilation du modèle
model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Entraînement
history = model.fit(X_train, y_train, epochs=50, validation_data=(X_test, y_test), verbose=0)

# Évaluation
loss, acc = model.evaluate(X_test, y_test)
print(f"Précision du modèle : {acc:.2f}")

# Visualisation de la frontière de décision
def plot_decision_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = (Z > 0.5).astype(int).reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.coolwarm)
    plt.title("Réseau de Neurones - Frontière de Décision")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()

# Affichage
plot_decision_boundary(model, X, y)
```

---

## 📊 **Explication du Code**

✅ **`make_moons()`** : Génère des données en forme de **lunes** pour classification.  
✅ **`keras.Sequential()`** : Définit un réseau de neurones avec 2 couches cachées de 10 neurones.  
✅ **`Dense(activation="relu")`** : Utilise **ReLU** pour mieux capturer les non-linéarités.  
✅ **`Dense(activation="sigmoid")`** : Utilise **Sigmoïde** pour la classification binaire.  
✅ **Visualisation de la frontière de décision** 🎨.

---

## 🚀 **Avantages des Réseaux de Neurones**

✅ **Capacité à modéliser des relations complexes** (non-linéarité).  
✅ **Scalabilité** : Fonctionne bien avec de grandes quantités de données.  
✅ **Utilisé pour la vision, le NLP, et bien plus**.

📌 **Inconvénients :**  
🔹 Besoin de **beaucoup de données** pour bien généraliser.  
🔹 Plus **lent** que des modèles simples comme la régression logistique.  
🔹 Difficile à **interpréter** (boîte noire).

Tu veux un exemple avec un **réseau plus profond (Deep Learning) et TensorFlow** ? 🚀
