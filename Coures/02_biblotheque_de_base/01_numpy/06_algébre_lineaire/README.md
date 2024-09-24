# cour 06 : **Algébre Lineaire avce numpy:**

## 1. **`det():`**

-   **Description :**

    > La méthode `det` de NumPy (via le module `linalg`) est utilisée pour calculer le déterminant d'une matrice carrée.

-   **Syntaxe :**

    ```python
    numpy.linalg.det(a)
    ```

    -   `a` : Matrice carrée dont le déterminant doit être calculé.

-   **Exemple :**

    ```python
    import numpy as np

    # Création d'une matrice carrée
    mat = np.array([[1, 2],
                    [3, 4]])

    # Calcul du déterminant
    determinant = np.linalg.det(mat)

    print("Matrice :")
    print(mat)
    print("\nDéterminant de la matrice :", determinant)
    ```

    -   **Output :**

        ```
        Matrice :
        [[1 2]
         [3 4]]

        Déterminant de la matrice : -2.0000000000000004
        ```

## 2 **`inv():`**

-   **Description :**

    > La méthode `inv` de NumPy (via le module `linalg`) est utilisée pour calculer l'inverse d'une matrice carrée.

-   **Syntaxe :**

    ```python
    numpy.linalg.inv(a)
    ```

    -   `a` : Matrice carrée dont l'inverse doit être calculée.

-   **Exemple :**

    ```python
    import numpy as np

    # Création d'une matrice carrée
    mat = np.array([[1, 2],
                    [3, 4]])

    # Calcul de l'inverse de la matrice
    inverse = np.linalg.inv(mat)

    print("Matrice :")
    print(mat)
    print("\nInverse de la matrice :")
    print(inverse)
    ```

    -   **Output :**

        ```
        Matrice :
        [[1 2]
         [3 4]]

        Inverse de la matrice :
        [[-2.   1. ]
         [ 1.5 -0.5]]
        ```

## 3.**`eig():`** (Valeurs propres et vecteurs propres)

-   **Description :**

    > La méthode `eig` de NumPy (via le module `linalg`) est utilisée pour calculer les valeurs propres et les vecteurs propres d'une matrice carrée.

-   **Syntaxe :**

    ```python
    numpy.linalg.eig(a)
    ```

    -   `a` : Matrice carrée pour laquelle les valeurs propres et les vecteurs propres doivent être calculés.

-   **Exemple :**

    ```python
    import numpy as np

    # Création d'une matrice carrée
    mat = np.array([[1, 2],
                    [3, 4]])

    # Calcul des valeurs propres et des vecteurs propres
    valeurs_propres, vecteurs_propres = np.linalg.eig(mat)

    print("Matrice :")
    print(mat)
    print("\nValeurs propres :")
    print(valeurs_propres)
    print("\nVecteurs propres :")
    print(vecteurs_propres)
    ```

    -   **Output :**

        ```
        Matrice :
        [[1 2]
         [3 4]]

        Valeurs propres :
        [-0.37228132  5.37228132]

        Vecteurs propres :
        [[-0.82456484 -0.41597356]
         [ 0.56576746 -0.90937671]]
        ```

## 4. **`norm():`**

-   **Description :**

    > La méthode `norm` de NumPy (via le module `linalg`) est utilisée pour calculer la norme (ou la taille) d'un vecteur ou d'une matrice. Il existe plusieurs types de normes (comme la norme euclidienne ou la norme de Frobenius).

-   **Syntaxe :**

    ```python
    numpy.linalg.norm(x, ord=None, axis=None)
    ```

    -   `x` : Vecteur ou matrice pour lequel la norme doit être calculée.
    -   `ord` : Type de norme (ex. `2` pour la norme euclidienne). Par défaut, la norme `2` est utilisée.
    -   `axis` : Si spécifié, la norme est calculée le long de cet axe.

-   **Exemple :**

    ```python
    import numpy as np

    # Création d'un vecteur
    vec = np.array([1, 2, 3])

    # Calcul de la norme euclidienne
    norme_euclidienne = np.linalg.norm(vec)

    print("Vecteur :")
    print(vec)
    print("\nNorme euclidienne du vecteur :", norme_euclidienne)
    ```

    -   **Output :**

        ```
        Vecteur :
        [1 2 3]

        Norme euclidienne du vecteur : 3.7416573867739413
        ```

-   **Exemple avec une matrice :**

    ```python
    import numpy as np

    # Création d'une matrice
    mat = np.array([[1, 2],
                    [3, 4]])

    # Calcul de la norme de Frobenius (par défaut)
    norme_frobenius = np.linalg.norm(mat)

    print("Matrice :")
    print(mat)
    print("\nNorme de Frobenius de la matrice :", norme_frobenius)
    ```

    -   **Output :**

        ```
        Matrice :
        [[1 2]
         [3 4]]

        Norme de Frobenius de la matrice : 5.477225575051661
        ```
