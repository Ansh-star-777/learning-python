import tensorflow as tf
from tensorflow.keras import layers,models
import matplotlib.pyplot as plt

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

x_train, x_test = x_train / 255.0, x_test / 255.0

model = models.Sequential([
    layers.Flatten(input_shape = (28,28)),
    layers.Dense(128,activation="relu"),
    layers.Dense(10,activation="softmax")
])

