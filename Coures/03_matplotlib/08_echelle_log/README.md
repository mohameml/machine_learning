# cour :  **l'échelle logarithmique**


## 1.**Définition :**

> L'échelle logarithmique est une manière de représenter les données sur un graphique où les graduations des axes ne sont pas espacées de manière linéaire, mais en fonction du **logarithme des valeurs**. Cela signifie que chaque intervalle sur l'axe représente une **multiplication par une constante**, souvent une puissance de 10.

- **Exemple :**  

    Les graduations pourraient être \( 1, 10, 100, 1000, \dots \), où chaque pas représente une multiplication par \( 10 \).


## 2.**Utilisation de l'échelle logarithmique :**

L'échelle logarithmique est utilisée dans plusieurs cas pour mieux visualiser ou analyser des données ayant certaines propriétés spécifiques :

- **Large plage de valeurs**
    
    Lorsque les données varient sur plusieurs ordres de grandeur (par exemple, de \( 10^{-3} \) à \( 10^6 \)), l'échelle linéaire masque souvent les petites valeurs. L'échelle logarithmique permet de voir les petites et grandes valeurs sur un même graphique.

- **Relations exponentielles ou géométriques**

    Pour détecter ou visualiser une relation exponentielle (\( y = a \cdot b^x \)), qui apparaît comme une **ligne droite** sur un axe logarithmique.




## 3.**Utilisation de `plt.xscale('log')`**


- En Python, avec la bibliothèque Matplotlib, vous pouvez facilement convertir un graphique pour utiliser une échelle logarithmique en appliquant la fonction **`plt.xscale()`** ou **`plt.yscale()`**.

- **Syntaxe :**

    ```python
    plt.xscale('log')  # Change l'échelle de l'axe x en logarithmique
    plt.yscale('log')  # Change l'échelle de l'axe y en logarithmique
    ```


    - **`log`** : Échelle logarithmique (base 10 par défaut).
    - **`symlog`** : Échelle logarithmique symétrique, utilisée pour des valeurs positives et négatives.
    - **`logit`** : Échelle logistique.


- **Exemple**

    ```python
    import matplotlib.pyplot as plt
    import numpy as np

    # Générer des données
    x = np.linspace(1, 100, 100)  # x de 1 à 100
    y = x**2  # Relation quadratique y = x^2

    # Tracer les données
    plt.plot(x, y, label="y = x²")
    plt.xlabel("x (échelle linéaire)")
    plt.ylabel("y (échelle linéaire)")
    plt.title("Graphique avec échelle linéaire")
    plt.legend()
    plt.show()
    ```

    ```python
    # Tracer avec échelle logarithmique
    plt.plot(x, y, label="y = x²")
    plt.xscale('log')  # Échelle logarithmique pour l'axe x
    plt.yscale('log')  # Échelle logarithmique pour l'axe y
    plt.xlabel("x (échelle logarithmique)")
    plt.ylabel("y (échelle logarithmique)")
    plt.title("Graphique avec échelle logarithmique")
    plt.legend()
    plt.show()
    ```

