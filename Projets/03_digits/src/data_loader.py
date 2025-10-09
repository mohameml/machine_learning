import pickle
import numpy as np 
import matplotlib.pyplot as plt 
from pathlib import Path 
from typing import Tuple , Literal
import matplotlib.pyplot as plt

Data = Tuple[np.ndarray , np.ndarray]



class DataLoaderMNIST:
    def __init__(self, path: str):
        """
        Charge les données MNIST depuis un fichier .pkl ou .pkl.gz
        et prépare les trois ensembles : train, val, test.
        """
        self.path : str  = path
        self.train_data : Data = None
        self.val_data : Data = None
        self.test_data : Data = None

        self._prepare_data()


    def _load_data(self) -> Tuple[Data , Data , Data]:
        """
        - Return the MNIST data as a tuple containing the training data,
        the validation data, and the test data.

        - The ``training_data`` is returned as a tuple with two entries.
            
            - The first entry contains the actual training images.  This is a
            numpy ndarray with 50,000 entries.  Each entry is, in turn, a
            numpy ndarray with 784 values, representing the 28 * 28 = 784
            pixels in a single MNIST image.
            
            - The second entry in the ``training_data`` tuple is a numpy ndarray
            containing 50,000 entries.  Those entries are just the digit
            values (0...9) for the corresponding images contained in the first
            entry of the tuple.

        
        - The ``validation_data`` and ``test_data`` are similar, except
        each contains only 10,000 images.

        This is a nice data format, but for use in neural networks it's
        helpful to modify the format of the ``training_data`` a little.
        That's done in the wrapper function ``load_data_wrapper()``, see
        below.
        """
        with open(self.path , "rb") as f : 
            training_data , validation_data , test_data = pickle.load(f , encoding="latin1")
        return training_data , validation_data , test_data

    def _prepare_data(self):
        
        # 1. Get the data from the file mnist.pkl : 
        training_data , validation_data , test_data = self._load_data()
        X_train , y_train = training_data
        X_val , y_val = validation_data
        X_test , y_test = test_data


        # 2. Conversion en float32 et reshape
        X_train = X_train.astype(np.float32)
        X_val = X_val.astype(np.float32)
        X_test = X_test.astype(np.float32)

        # 2. Normalisation [0, 1]
        X_train /= 255.0
        X_val /= 255.0
        X_test /= 255.0

        # 3. One-hot encoding des labels
        Y_train = self._one_hot(y_train)
        Y_val = self._one_hot(y_val)
        Y_test = self._one_hot(y_test)

        # 4. Transposer pour correspondre au format du réseau : (n_features, n_samples)
        X_train, X_val, X_test = X_train.T, X_val.T, X_test.T
        Y_train, Y_val, Y_test = Y_train.T, Y_val.T, Y_test.T

        self.train_data = (X_train, Y_train)
        self.val_data = (X_val, Y_val)
        self.test_data = (X_test, Y_test)

    def _one_hot(self, y: np.ndarray, num_classes: int = 10) -> np.ndarray:
        """Convertit un vecteur d'étiquettes en matrice one-hot."""
        one_hot = np.zeros((y.size, num_classes))
        one_hot[np.arange(y.size), y] = 1
        return one_hot

    def get(self, split: Literal["train" , "val" , "test"] = "train" , n_samples : int | None = None):
        """
        Retourne (X, Y) pour le split demandé.
        Si n_samples est spécifié, renvoie un sous-ensemble aléatoire de cette taille.
        split ∈ {"train", "val", "test"}
        """
        
        if split == "train":
            X , Y =  self.train_data
        elif split == "val":
            X , Y =  self.val_data
        elif split == "test":
            X , Y = self.test_data
        else:
            raise ValueError("split doit être 'train', 'val' ou 'test'")

        if n_samples is not None :
            m = X.shape[1]

            if n_samples > m : 
                raise ValueError(f"n_samples ({n_samples}) > the size of dataset ({m})")

            indices = np.random.choice(m,n_samples ,replace=True)
            X = X[:,indices]
            Y = Y[:,indices]

        return X , Y 
    

    def visualize(self, split: str = "train", n_images: int = 9):
        """
        Affiche une grille d'images du split choisi (train/val/test)
        avec leurs labels.
        """
        X, Y = self.get(split)
        n_total = X.shape[1]

        # Limiter à n_images disponibles
        n_images = min(n_images, n_total)

        # Sélection aléatoire d'indices
        indices = np.random.choice(n_total, n_images, replace=False)
        X_subset = X[:, indices]
        Y_subset = Y[:, indices]
        labels = np.argmax(Y_subset, axis=0)

        # Déterminer la taille de la grille (ex: 9 → 3x3)
        grid_size = int(np.ceil(np.sqrt(n_images)))

        fig, axes = plt.subplots(grid_size, grid_size, figsize=(6, 6))
        axes = axes.flatten()

        for i, ax in enumerate(axes[:n_images]):
            image = X_subset[:, i].reshape(28, 28)
            ax.imshow(image, cmap="gray")
            ax.set_title(f"{labels[i]}")
            ax.axis("off")

        # Cacher les cases vides
        for ax in axes[n_images:]:
            ax.axis("off")

        plt.suptitle(f"MNIST - {split} ({n_images} images)")
        plt.tight_layout()
        plt.show()
