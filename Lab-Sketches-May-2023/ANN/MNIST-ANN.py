# MNIST Digit Recognition with TensorFlow

# load modules
import tensorflow as tf
from tensorflow import keras

# Load the MNIST dataset
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


# Preprocess the data
train_images = train_images / 255.0
test_images = test_images / 255.0


# Define the model
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
], name='flowergenesis')

# Compile the model
model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])


# Train the model
#model.fit(train_images, train_labels, epochs = 5)


# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('flowergenesis Test Accuracy:' , test_acc)