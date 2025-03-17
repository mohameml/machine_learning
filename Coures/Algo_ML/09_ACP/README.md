## 🌍 **Analyse en Composantes Principales (ACP - PCA en anglais)**

L'**Analyse en Composantes Principales (ACP)** est une technique de **réduction de dimension** utilisée en **machine learning et statistiques** pour :  
✅ Réduire la dimension des données tout en conservant un maximum d'information.  
✅ Identifier les axes de variation les plus importants dans les données.  
✅ Faciliter la **visualisation** et l’**interprétation** des données.

---

## 🔹 **Comment fonctionne l'ACP ?**

L'ACP projette les données sur un nouvel espace de dimension réduite en utilisant les **valeurs propres et vecteurs propres** de la matrice de covariance.

1️⃣ **Centrage des données** : Soustraction de la moyenne pour avoir une moyenne de 0.  
2️⃣ **Calcul de la matrice de covariance** : Mesure la relation entre les variables.  
3️⃣ **Décomposition spectrale (SVD ou valeurs propres)** : Trouver les **composantes principales**.  
4️⃣ **Projection des données** : Transformation des données selon les **axes principaux**.  
5️⃣ **Sélection des composantes** : On garde celles qui expliquent le plus de variance.

🚀 **But :** Trouver une nouvelle base où les données sont mieux représentées avec moins de dimensions.

---

## 📜 **Exemple en Python avec Visualisation (ACP sur Iris)**

```python
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Chargement du dataset Iris
iris = load_iris()
X = iris.data
y = iris.target
labels = iris.target_names

# Normalisation des données (obligatoire pour ACP)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Application de l'ACP (réduction à 2 dimensions pour visualisation)
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X_scaled)

# Visualisation des données après ACP
plt.figure(figsize=(8,6))
sns.scatterplot(x=X_pca[:,0], y=X_pca[:,1], hue=y, palette="Set1", legend='full')
plt.xlabel("Composante Principale 1")
plt.ylabel("Composante Principale 2")
plt.title("Projection ACP des données Iris")
plt.show()

# Affichage de la variance expliquée par chaque composante
print(f"Variance expliquée par la première composante : {pca.explained_variance_ratio_[0]:.2f}")
print(f"Variance expliquée par la deuxième composante : {pca.explained_variance_ratio_[1]:.2f}")
```

---

## 📊 **Explication du Code**

✅ **Standardisation** 📏 : L’ACP est sensible aux échelles, donc on normalise avec `StandardScaler()`.  
✅ **Application de l’ACP** 🧮 : `PCA(n_components=2)` pour réduire à **2 dimensions**.  
✅ **Visualisation** 🎨 : Un **scatter plot** montre les clusters des différentes classes d'Iris.  
✅ **Variance expliquée** 📈 : Permet de voir combien d’information chaque axe retient.

---

## 🚀 **Avantages de l’ACP**

✅ **Réduit la dimensionnalité**, utile pour des modèles plus rapides.  
✅ **Élimine la redondance** entre les variables (corrélations fortes).  
✅ **Facilite la visualisation** des données en haute dimension.

📌 **Inconvénients** :  
🔹 Perd un peu d'interprétabilité (les nouvelles dimensions ne sont pas directement liées aux features initiales).  
🔹 Fonctionne mieux si les variables sont bien **corrélées**.

Tu veux voir une version **3D** de la visualisation de l'ACP ? 🚀
