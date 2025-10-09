from data_loader import DataLoaderMNIST

loader = DataLoaderMNIST("./data/mnist.pkl")

# Afficher 9 images du training set
loader.visualize(split="train", n_images=16)
