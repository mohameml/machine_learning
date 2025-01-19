# cour 01 : **Introduction:**

> Le **data preprocessing** en machine learning (ML) est une étape clé de préparation des données avant de les utiliser dans un modèle. Il vise à nettoyer, transformer et structurer les données pour les rendre exploitables et améliorer les performances du modèle.

### 1. **Collecte des données**

-   **Description** : Récupération des données à partir de différentes sources (bases de données, fichiers CSV, APIs).
-   **Librairie Python** : `pandas`, `SQLAlchemy`, `requests`
-   **Exemple** :
    ```python
    import pandas as pd
    data = pd.read_csv('data.csv')  # Chargement d'un fichier CSV
    ```

### 2. **Gestion des données manquantes**

-   **Description** : Remplacer ou supprimer les valeurs manquantes dans les datasets.
-   **Librairie Python** : `pandas`
-   **Exemple** :

    ```python
    # Supprimer les lignes avec des valeurs manquantes
    data.dropna(inplace=True)

    # Remplacer les valeurs manquantes par la moyenne de la colonne
    data.fillna(data.mean(), inplace=True)
    ```

### 3. **Encodage des variables catégorielles**

-   **Description** : Conversion des variables catégorielles en variables numériques pour que le modèle puisse les utiliser.
-   **Librairie Python** : `pandas`, `sklearn.preprocessing`
-   **Exemple** :

    ```python
    # Encodage one-hot avec pandas
    data = pd.get_dummies(data, columns=['category_column'])

    # Encodage label avec sklearn
    from sklearn.preprocessing import LabelEncoder
    encoder = LabelEncoder()
    data['encoded_column'] = encoder.fit_transform(data['category_column'])
    ```

### 4. **Feature Scaling (Mise à l'échelle des caractéristiques)**

-   **Description** : Standardiser ou normaliser les données pour que toutes les caractéristiques soient sur une même échelle.
-   **Librairie Python** : `sklearn.preprocessing`
-   **Exemple** :

    ```python
    from sklearn.preprocessing import StandardScaler, MinMaxScaler

    # Standardisation (moyenne 0, écart-type 1)
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)

    # Normalisation (valeurs entre 0 et 1)
    normalizer = MinMaxScaler()
    data_normalized = normalizer.fit_transform(data)
    ```

### 5. **Séparation des données (train/test split)**

-   **Description** : Séparer les données en ensembles d'entraînement et de test pour évaluer les performances du modèle.
-   **Librairie Python** : `sklearn.model_selection`
-   **Exemple** :

    ```python
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    ```

### 6. **Détection et gestion des valeurs aberrantes (outliers)**

-   **Description** : Identifier et traiter les valeurs anormales qui peuvent fausser les résultats du modèle.
-   **Librairie Python** : `pandas`, `numpy`, `scipy`
-   **Exemple** :

    ```python
    # Utiliser l'IQR (Interquartile Range) pour détecter les outliers
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1

    # Filtrer les valeurs aberrantes
    data_outliers_removed = data[~((data < (Q1 - 1.5 * IQR)) | (data > (Q3 + 1.5 * IQR))).any(axis=1)]
    ```

### 7. **Transformation des données (log, sqrt, etc.)**

-   **Description** : Appliquer des transformations mathématiques aux données pour réduire l'effet des distributions asymétriques.
-   **Librairie Python** : `numpy`, `pandas`
-   **Exemple** :
    ```python
    import numpy as np
    # Appliquer une transformation logarithmique
    data['log_transformed'] = np.log(data['column'] + 1)  # +1 pour éviter les log(0)
    ```

### 8. **Réduction de dimension (PCA)**

-   **Description** : Réduire le nombre de caractéristiques tout en conservant le plus d'information possible.
-   **Librairie Python** : `sklearn.decomposition`
-   **Exemple** :

    ```python
    from sklearn.decomposition import PCA

    pca = PCA(n_components=2)
    data_pca = pca.fit_transform(data)
    ```
