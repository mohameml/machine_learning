## 📌 **L'algorithme K-Means : Clustering non supervisé**

L’algorithme **K-Means** est une **méthode de clustering** qui regroupe des points de données en **K clusters** en minimisant la variance intra-cluster.

---

## 🔹 **Comment fonctionne K-Means ?**

1️⃣ **Initialisation** : On choisit \( K \) centres aléatoires.  
2️⃣ **Assignation** : Chaque point est assigné au centre le plus proche (via la distance Euclidienne).  
3️⃣ **Mise à jour** : On recalcule les **centres** en prenant la moyenne des points de chaque cluster.  
4️⃣ **Répétition** : On recommence **jusqu'à convergence** (plus de changements).

🚀 **But :** Minimiser la somme des distances au carré entre chaque point et son centre.  
\[
J = \sum*{i=1}^{K} \sum*{x \in C_i} || x - \mu_i ||^2
\]
où \( C_i \) est le cluster \( i \) et \( \mu_i \) son centroïde.

---

## 📜 **Exemple en Python avec Visualisation**

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Générer des données avec 3 clusters
X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1.0, random_state=42)

# Appliquer K-Means avec K=3
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X)

# Prédictions des clusters
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_

# Affichage des clusters et centroïdes
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', alpha=0.6)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='X', s=200, label="Centroïdes")
plt.title("Clustering avec K-Means")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.show()
```

---

## 🔹 **Explication du Code**

✅ **`make_blobs()`** : Génère des **données artificielles** avec 3 clusters.  
✅ **`KMeans(n_clusters=3)`** : Applique l’algorithme avec \( K=3 \).  
✅ **`kmeans.fit(X)`** : Entraîne K-Means sur les données.  
✅ **Visualisation** :

-   **Couleurs = clusters**
-   **Points rouges = centroïdes**

---

## 📌 **Améliorations possibles :**

🔹 Trouver le **meilleur K** avec la **méthode du coude** 📉.  
🔹 Tester d'autres métriques de distance (Manhattan, Cosine, etc.).  
🔹 Essayer **K-Means++** pour une meilleure initialisation.

Tu veux voir un exemple avec la **méthode du coude** pour choisir \( K \) ? 🚀
