# cour 04 : **clean data**

## 1. **Méthode `fillna()`:**

-   **Définition:**

    > La méthode **`fillna()`** est utilisée pour remplacer les valeurs manquantes (NaN) dans un DataFrame ou une série par une valeur spécifiée ou par des méthodes d'interpolation.

-   **Syntaxe:**

    ```python
    DataFrame.fillna(value=None, method=None, axis=None, inplace=False, limit=None, downcast=None)
    ```

    -   **`value`** : Valeur ou dictionnaire de valeurs à utiliser pour remplir les NaN.
    -   **`method`** : Méthode à utiliser pour remplir les NaN, comme `'ffill'` (forward fill) ou `'bfill'` (backward fill).
    -   **`axis`** : 0 ou 1 pour spécifier si l'opération est appliquée sur les lignes ou les colonnes.
    -   **`inplace`** : Si `True`, remplace les données dans le DataFrame d'origine.
    -   **`limit`** : Limite le nombre de remplacements à effectuer.

-   **Exemple:**

    ```python
    import pandas as pd

    # Création d'un DataFrame avec des valeurs manquantes
    data = {
        'Nom': ['Alice', 'Bob', 'Charlie', 'David'],
        'Âge': [25, None, 30, None],
        'Ville': ['Paris', 'Lyon', None, 'Toulouse']
    }
    df = pd.DataFrame(data)

    # Remplacer les valeurs NaN par une valeur spécifiée
    df_rempli = df.fillna(value={'Âge': 0, 'Ville': 'Inconnu'})
    print("DataFrame après remplissage des NaN :")
    print(df_rempli)
    ```

## 2. **Méthode `dropna()`:**

-   **Définition:**

    > La méthode **`dropna()`** est utilisée pour supprimer les lignes ou colonnes qui contiennent des valeurs manquantes (NaN).

-   **Syntaxe:**

    ```python
    DataFrame.dropna(axis=0, how='any', thresh=None, subset=None, inplace=False)
    ```

    -   **`axis`** : 0 pour supprimer des lignes, 1 pour supprimer des colonnes.
    -   **`how`** : `'any'` (supprime si au moins une valeur est NaN) ou `'all'` (supprime si toutes les valeurs sont NaN).
    -   **`thresh`** : Nombre minimum de valeurs non manquantes requises pour ne pas supprimer la ligne/colonne.
    -   **`subset`** : Liste de colonnes à considérer pour déterminer si une ligne doit être supprimée.
    -   **`inplace`** : Si `True`, effectue l'opération sur le DataFrame d'origine.

-   **Exemple:**

    ```python
    # Suppression des lignes contenant des valeurs NaN
    df_sans_na = df.dropna()
    print("\nDataFrame après suppression des lignes contenant des NaN :")
    print(df_sans_na)
    ```
