# cour 02 :

> Pandas offre des méthodes très pratiques pour l'importation et l'exportation de données à partir et vers différents formats de fichiers. Ces méthodes commencent généralement par `read_*` pour l'importation et `to_*` pour l'exportation.

## 1. **Importation de données : `read_csv`**

-   **Définition:**

    > La méthode `read_csv()` est utilisée pour lire des fichiers CSV et charger les données dans un DataFrame Pandas.

-   **Syntaxe:**

    ```python
    pd.read_csv(filepath, sep=',', header=0, index_col=None, ...)
    ```

    -   **`filepath`** : Chemin du fichier ou URL.
    -   **`sep`** : Délimiteur utilisé dans le fichier (par défaut, une virgule `,`).
    -   **`header`** : Indique quelle ligne utiliser comme en-tête (par défaut, la première ligne).
    -   **`index_col`** : Colonne(s) à utiliser comme index (facultatif).

-   **Exemple:**

    ```python
    import pandas as pd

    # Lire un fichier CSV et le charger dans un DataFrame
    df = pd.read_csv('data.csv')

    # Afficher les premières lignes du DataFrame
    print(df.head())
    ```

## 2. Exportation de données : `to_csv()`

-   **Définition:**

    > La méthode `to_csv()` permet d'exporter un DataFrame en fichier CSV.

-   **Syntaxe:**

    ```python
    df.to_csv(filepath, sep=',', index=True, header=True, ...)
    ```

    -   **`filepath`** : Chemin où le fichier sera enregistré.
    -   **`sep`** : Délimiteur utilisé pour séparer les valeurs (par défaut, une virgule `,`).
    -   **`index`** : Si `True`, l'index est écrit dans le fichier (par défaut, `True`).
    -   **`header`** : Si `True`, les noms de colonnes sont écrits (par défaut, `True`).

#### RQ : **Autres Méthodes `read_*` et `to_*`**

Pandas offre des méthodes similaires pour d'autres formats, notamment :

-   **`read_excel()`** / **`to_excel()`** pour les fichiers Excel.
-   **`read_json()`** / **`to_json()`** pour les fichiers JSON.
-   **`read_sql()`** / **`to_sql()`** pour les bases de données SQL.
-   **`read_html()`** / **`to_html()`** pour les fichiers HTML.
