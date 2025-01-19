# Cour : **Customization**


> Matplotlib offre de nombreuses options pour personnaliser vos graphiques, notamment en ajoutant des titres, en étiquetant les axes, et en ajustant les graduations. 


## 1.**`plt.title()`**

- **Définition :**

    La fonction **`plt.title()`** ajoute un titre au graphique.

- **Syntaxe :**

    ```python
    plt.title(label)
    ```

    - **`label`** : Le texte du titre.


## 2. **`plt.xlabel()` et `plt.ylabel()`:**

- **Définition :**

    Ces fonctions permettent d'ajouter une étiquette à l'axe des abscisses (x) et à l'axe des ordonnées (y).

- **Syntaxe :**

    ```python
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    ```

    - **`xlabel` / `ylabel`** : Le texte de l'étiquette.



## 3.**`plt.xticks()` et `plt.yticks()`**

- **Définition :**

    Ces fonctions ajustent les positions et les étiquettes des graduations sur les axes x et y.

- **Syntaxe :**

    ```python
    plt.xticks(ticks=None, labels=None)
    plt.yticks(ticks=None, labels=None)
    ```

    - **`ticks`** : Une liste de positions où placer les graduations.
    - **`labels`** *(optionnel)* : Une liste de textes pour étiqueter les graduations.


- **Exemple :**

    ```python
    import numpy as np
    ticks = np.arange(0, 11, 2)
    labels = ['0', 'Deux', 'Quatre', 'Six', 'Huit', 'Dix']
    plt.xticks(ticks=ticks, labels=labels)
    ```


## 4.**`plt.legend()`**

- **Définition :**

    La fonction **`plt.legend()`** affiche une légende pour décrire les éléments du graphique.

- **Syntaxe :**

    ```python
    plt.legend(loc='best', fontsize=None, title=None)
    ```

    - **`loc`** : Position de la légende (par exemple `"best"`, `"upper left"`, `"center right"`, etc.).
    - **`fontsize`** : Taille de la police.
    - **`title`** : Titre facultatif pour la légende.

- **Exemple :**

    ```python
    plt.plot([1, 2, 3], [1, 4, 9], label="Carré")
    plt.plot([1, 2, 3], [1, 2, 3], label="Linéaire")
    plt.legend(loc="upper left", title="Lignes", fontsize=10)
    ```




