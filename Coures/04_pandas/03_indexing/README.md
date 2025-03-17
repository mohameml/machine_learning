# Cour 03 : **Indexing in Pandas**


## 1. **Indexation avec des crochets `[]` :**

- **Définition :**

    Les crochets permettent un accès simple et direct aux colonnes ou lignes d'un DataFrame ou d'une Series. Ils sont souvent utilisés pour accéder aux **colonnes** par leur nom ou pour sélectionner des **lignes** en utilisant un **slice**.

- **Syntaxe :**

    ```python
    # col : 
    df['col_name'] # type series 
    df[['col_name']]  # type df
    df.col_name 
    df[['col1' , 'col2']]

    # row : 
    df[start:stop:step]
    ```
  - Une seule colonne : `df['col_name']` ou `df.col_name` (si aucun espace ou caractère spécial).
  - Plusieurs colonnes : `df[['col1', 'col2']]` (liste de colonnes).
  - `df[start:stop:step]` sélectionne les lignes comme dans une liste Python.


- **Exemples :**

    ```python
    import pandas as pd

    # Exemple DataFrame
    data = {'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]}
    df = pd.DataFrame(data)

    # Une seule colonne
    print(df['A'])  # Série contenant les valeurs de la colonne 'A'

    # Plusieurs colonnes
    print(df[['A', 'B']])  # DataFrame contenant uniquement les colonnes 'A' et 'B'
    ```

    ```python
    # Accès aux deux premières lignes
    print(df[:2])

    # Lignes en sautant une ligne
    print(df[::2])
    ```


## 2. **Indexation avec `loc`**

- **Définition :**

    La méthode **`loc`** permet d’accéder à des lignes et colonnes en fonction des **étiquettes (labels)** d’index.

- **Syntaxe :**

    ```python
    df.loc[row_labels, column_labels]

    df.loc[[row1 , row2 , row3]] 
    df.loc[:, [col1 , col2 , col3]] # ~ df[[col1 , col2 , col3]]
    df.loc[ [row1 , row2 , row3] , [col1, col2, col3] ]
    ```

    - **row_labels** : Les étiquettes des lignes.
    - **column_labels** : Les étiquettes des colonnes.
    - Peut être une seule étiquette, une liste, un slice, ou une condition booléenne.

- **Exemples :**

    ```python
    # Accès à une ligne par étiquette
    print(df.loc[1])  # Ligne avec l'index 1

    # Accès à une cellule précise (ligne 1, colonne 'B')
    print(df.loc[1, 'B'])

    # Sélection de plusieurs lignes et colonnes
    print(df.loc[[0, 2], ['A', 'C']])  # Lignes 0 et 2, colonnes 'A' et 'C'

    # Utiliser une condition pour filtrer les lignes
    print(df.loc[df['A'] > 1])
    ```


## 3. **Indexation avec `iloc`**

- **Définition :**

    La méthode **`iloc`** permet d’accéder aux lignes et colonnes **par position** (indices entiers uniquement).

- **Syntaxe :**

    ```python
    df.iloc[row_indices, column_indices]
    df.iloc[start:fin, start:fin]
    ```

    - **row_indices** : Les indices des lignes (entiers).
    - **column_indices** : Les indices des colonnes (entiers).
    - Accepte des scalaires, listes, slices, ou masques booléens.

- **Exemples :**

    ```python
    # Accès à une ligne par position
    print(df.iloc[1])  # Ligne à la position 1

    # Accès à une cellule précise (ligne 1, colonne à la position 1)
    print(df.iloc[1, 1])

    # Accès à des lignes et colonnes spécifiques
    print(df.iloc[[0, 2], [0, 2]])  # Lignes 0 et 2, colonnes 0 et 2

    # Utilisation d'un slice
    print(df.iloc[1:3, :])  # Lignes 1 à 2, toutes les colonnes
    ```



