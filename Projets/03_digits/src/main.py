import numpy as np 
import matplotlib.pyplot as plt 

from data_loader import DataLoaderMNIST
from network import NeuralNetwork
from layer import Layer
from activation import Sigmoid , ReLU , Softmax
from loss import MSE , CrossEntropy



def main(): 

    # 1. load data : 
    loader = DataLoaderMNIST('./data/mnist.pkl')

    X_train , Y_train = loader.get("train", n_samples=10000)
    X_val , Y_val = loader.get("val", n_samples=1000)
    X_test , Y_test = loader.get("test", n_samples=1000)

    print(f"Train set: {X_train.shape}, {Y_train.shape}")

    # 2. create the NeuralNetwork
    model = NeuralNetwork(loss=MSE())
    # model.add(Layer(784 , 30 , Sigmoid()))
    # model.add(Layer(30, 10 , Sigmoid()))


    model.add(Layer(784 , 128 , Sigmoid()))
    model.add(Layer(128, 64 , Sigmoid()))
    model.add(Layer(64 , 10 , Sigmoid()))

    # 3. Train the model :
    model.train(
        X=X_train,
        Y=Y_train,
        epochs=30,
        batch_size=10,
        lr=2.0
    )

    train_acc = model.accuracy(X_train , Y_train)
    print(f"Train accuracy: {train_acc*100:.2f}%")

    # 4. evalute the model  : 
    val_loss = model.evaluate(X_val , Y_val)
    print(f"Validation loss : {val_loss:.4f}")
    val_acc = model.accuracy(X_val, Y_val)
    print(f"Validation accuracy: {val_acc*100:.2f}%")

    # 5. Test the model : 
    X_test_sample = X_test[:,[0]]
    Y_test_sample = Y_test[:,[0]]
    Y_pred = model.forward(X_test_sample)
    pred_label = np.argmax(Y_pred)
    true_label = np.argmax(Y_test_sample)
    print("test with .....")
    print(f"Y_pred : {Y_pred}")
    print(f"True label: {true_label}, Predicted: {pred_label}")

    # 6. Visualisation : 
    plt.imshow(X_test_sample.reshape(28, 28), cmap="gray")
    plt.title(f"True: {true_label} | Predicted: {pred_label}")
    plt.axis("off")
    plt.show()

if __name__ == "__main__":
    main()