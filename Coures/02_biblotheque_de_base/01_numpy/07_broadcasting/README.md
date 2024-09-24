# cour 07 : **Broadcasting**

## 1. **Principe du Broadcasting:**

-   **Defintion:**

    > Le **broadcasting** en `numpy` est un mécanisme puissant qui permet d'effectuer des opérations sur des tableaux de tailles différentes, sans avoir à dupliquer les données. Il "étend" un tableau plus petit sur un plus grand pour permettre des opérations élémentaires (addition, multiplication, etc.) de manière efficace en termes de mémoire et de calcul.

    -   Lorsqu'une opération arithmétique (comme une addition, une multiplication, etc.) est effectuée entre deux tableaux de formes différentes, `numpy` essaie d'ajuster automatiquement les formes pour les rendre compatibles via le broadcasting. Les dimensions sont étendues de manière implicite selon certaines règles afin de réaliser l'opération sans créer de copies inutiles.

-   **Règles de Broadcasting:**

    1. Si les deux tableaux n'ont pas le même nombre de dimensions, `numpy` ajoute des dimensions "1" à gauche au tableau avec moins de dimensions.

    2. Ensuite, pour chaque dimension, les tailles doivent correspondre ou l'une des deux doit être de taille 1. Si la taille est 1, `numpy` va étendre cette dimension pour correspondre à la taille de l'autre tableau.

## 2. **Exemples:**

-   **Exemple de Broadcasting:**

    Si on a un tableau 2D et un vecteur 1D, `numpy` va étendre le vecteur pour correspondre à la forme du tableau.

    ```python
    import numpy as np

    # Tableau 2D
    A = np.array([[1, 2, 3],
                [4, 5, 6]])

    # Vecteur 1D
    B = np.array([10, 20, 30])

    # Broadcasting
    C = A + B

    print(C)
    ```

    -   La forme de `A` est `(2, 3)` et la forme de `B` est `(3,)`. `numpy` traite `B` comme s'il avait la forme `(1, 3)` (en ajoutant une dimension à gauche).
    -   Ensuite, `numpy` étend ce vecteur sur deux lignes, de sorte que l'opération devient valide.

    -   **Résultat** :

        ```
        [[11 22 33]
        [14 25 36]]
        ```

-   **Exemple d'opération où le broadcasting échoue:**

    Le broadcasting ne fonctionne que si les tailles sont compatibles. Si les tailles ne peuvent pas être alignées, `numpy` lèvera une erreur.

    ```python
    import numpy as np

    A = np.array([[1, 2, 3],
                [4, 5, 6]])

    B = np.array([10, 20])

    # Cela va provoquer une erreur
    C = A + B
    ```

    Dans ce cas, `B` ne peut pas être broadcasté car sa taille `(2,)` ne correspond pas à la taille `(3,)` de la seconde dimension de `A`.

## 3. **Dangers du Broadcasting:**

-   Le principal danger avec le broadcasting est que, parfois, `numpy` peut effectuer des opérations sans lever d'erreurs, mais les résultats peuvent ne pas correspondre à ce que l'on attend, surtout avec des vecteurs unidimensionnels.

-   **Exemple de cas potentiellement dangereux avec un vecteur:**

    Supposons que tu veuilles soustraire un vecteur de forme `(3,)` d'une matrice 2D, mais tu te trompes sur l'orientation du vecteur.

    ```python
    import numpy as np

    A = np.array([[1, 2, 3],
                [4, 5, 6]])

    B = np.array([1, 2, 3])  # Vecteur (3,)

    # Soustraction
    C = A - B

    print(C)
    ```

    Ici, le résultat est correct :

    ```
    [[0 0 0]
    [3 3 3]]
    ```

    Mais que se passe-t-il si le vecteur est de forme `(3, 1)` au lieu de `(3,)` ?

    ```python
    B = np.array([[1], [2], [3]])  # Vecteur (3,1)

    # Cela va donner un résultat inattendu
    C = A - B
    print(C)
    ```

    **Résultat inattendu** :

    ```
    [[ 0  1  2]
    [ 2  3  4]
    [ 3  4  5]]
    ```

    Parce que `numpy` a étendu le tableau `(3, 1)` pour qu'il corresponde à la première dimension de `A`, ce qui a produit un résultat incorrect pour une soustraction ligne par ligne.

### RQ:

Le broadcasting est extrêmement utile car il permet d'écrire du code plus compact et rapide, mais il peut introduire des erreurs subtiles, surtout lors de l'utilisation de vecteurs de forme `(n,)`. Il est important de toujours être attentif à la manière dont les dimensions sont alignées dans les opérations, et parfois, il peut être utile d'expliciter les dimensions (par exemple, en utilisant `reshape`) pour éviter les erreurs involontaires.
