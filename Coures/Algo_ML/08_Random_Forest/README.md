## 🌳 **Random Forest : Un Algorithme d'Ensemble Apprentissage**

L'algorithme **Random Forest** est une **méthode d'ensemble** basée sur **plusieurs arbres de décision**. Il est utilisé pour la **classification** et la **régression**.

---

## 🔹 **Comment fonctionne Random Forest ?**

1️⃣ **Création de plusieurs arbres de décision** (d'où le terme "forêt").  
2️⃣ **Chaque arbre est entraîné sur un sous-ensemble aléatoire des données** (technique du bootstrap).  
3️⃣ **Chaque arbre vote** pour une classe (classification) ou fait une moyenne des prédictions (régression).  
4️⃣ **Prédiction finale :**

-   🏆 **Classification** : La classe majoritaire parmi les arbres.
-   📈 **Régression** : Moyenne des prédictions des arbres.

🔹 Random Forest réduit **le surapprentissage** par rapport à un **arbre unique** ! 🎯

---

## 📜 **Exemple en Python : Classification avec Random Forest**

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Génération d'un dataset de classification
X, y = make_classification(n_samples=500, n_features=2, n_informative=2, n_redundant=0, random_state=42)

# Séparation en train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modèle Random Forest avec 100 arbres
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Prédiction et évaluation
y_pred = rf.predict(X_test)
print(f"Précision du modèle : {accuracy_score(y_test, y_pred):.2f}")

# Visualisation de la frontière de décision
def plot_decision_boundary(model, X, y):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.contourf(xx, yy, Z, alpha=0.3, cmap=plt.cm.coolwarm)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.coolwarm)
    plt.title("Random Forest - Frontière de Décision")
    plt.xlabel("Feature 1")
    plt.ylabel("Feature 2")
    plt.show()

# Affichage de la frontière de décision
plot_decision_boundary(rf, X, y)
```

---

## 📊 **Explication du Code**

✅ **`make_classification()`** : Génère un dataset avec **2 features** (pour visualisation).  
✅ **`RandomForestClassifier(n_estimators=100)`** : Utilise **100 arbres** 🌳.  
✅ **`fit(X_train, y_train)`** : Entraîne la forêt sur les données.  
✅ **`accuracy_score(y_test, y_pred)`** : Évalue la **précision** du modèle.  
✅ **Visualisation de la frontière de décision** 📈.

---

## 🚀 **Avantages de Random Forest**

✅ **Réduit le surapprentissage** comparé à un arbre unique.  
✅ **Très performant** pour les problèmes de classification et régression.  
✅ **Gère bien les données bruitées et les valeurs manquantes**.  
✅ **Peut gérer des datasets avec de nombreuses features**.

📌 **Inconvénients :** Plus lent que des modèles simples comme la régression logistique.

Tu veux voir un **exemple de Random Forest pour la régression** ? 🔥
