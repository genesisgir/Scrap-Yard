# MNIST Digit Recognition with TensorFlow

# load modules, tensorflow, keras
import tensorflow, numpy
from tensorflow import keras
from PIL import Image

# Load the MNIST dataset
mnist_dataset = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist_dataset.load_data(path='mnist.npz') # Tuple of NumPy arrays: (x_train, y_train), (x_test, y_test).

''' <- why do we load the dataset?

█░░ █▀█ ▄▀█ █▀▄ █ █▄░█ █▀▀   █▀▄ ▄▀█ ▀█▀ ▄▀█ █▀ █▀▀ ▀█▀ █▀
█▄▄ █▄█ █▀█ █▄▀ █ █░▀█ █▄█   █▄▀ █▀█ ░█░ █▀█ ▄█ ██▄ ░█░ ▄█

ᴄʜᴀᴛɢᴘᴛ sʏsɴᴏᴘsɪs
Loading the dataset is an essential step in machine learning tasks because it provides the necessary input data and corresponding labels for training 
and evaluating the model. Here are a few reasons why we load the dataset:

Accessing the Data: Loading the dataset allows us to access the training and test data, which are required for training and evaluating the 
machine learning model. The dataset typically consists of input features (e.g., images, text, numerical data) and corresponding labels or 
target values. Loading the dataset provides us with access to this data, enabling us to use it in our machine learning pipeline.

Preparing the Training Data: The loaded dataset is often split into separate training and test sets. The training set is used to train the model, 
while the test set is used to evaluate its performance on unseen data. Loading the dataset allows us to access these separate subsets, which are 
crucial for training and evaluation.

Data Exploration and Analysis: Loading the dataset allows us to explore and analyze its characteristics, such as the number of samples, 
the dimensionality of the input features, the distribution of labels, etc. This exploration helps us gain insights into the data and make 
informed decisions during the model development process.

Preprocessing and Data Transformation: Loading the dataset provides an opportunity to preprocess and transform the data as needed. 
This can include tasks such as data normalization, feature scaling, handling missing values, encoding categorical variables, and more. 
Loading the dataset allows us to access the raw data and perform these preprocessing steps before using it for training the model.

By loading the dataset, we gain access to the necessary input data and labels, which are fundamental for training and evaluating a 
machine learning model. It enables us to access, analyze, preprocess, and transform the data as required, setting the foundation for subsequent 
steps in the machine learning pipeline.
'''

# normalize/Preprocess the data
train_images = train_images / 255.0
test_images = test_images / 255.0

''' <- why do we pre process the data?


█▄░█ █▀█ █▀█ █▀▄▀█ ▄▀█ █░░ █ ▀█ ▄▀█ ▀█▀ █ █▀█ █▄░█
█░▀█ █▄█ █▀▄ █░▀░█ █▀█ █▄▄ █ █▄ █▀█ ░█░ █ █▄█ █░▀█

ᴄʜᴀᴛɢᴘᴛ sʏsɴᴏᴘsɪs
The purpose of normalization in this context is to bring the pixel values to a common scale. Dividing each pixel value by 255.0 scales the values 
down to a range of 0 to 1. Normalization is often applied to input data in machine learning tasks to ensure that features have similar ranges and 
prevent any particular feature from dominating the learning process.

By normalizing the pixel values in the range of 0 to 1, it becomes easier for the neural network model to learn and converge efficiently. 
Additionally, normalization can help in mitigating the impact of lighting conditions and variations in pixel intensities across different 
images, making the model more robust to such variations.

Note that the choice of 255.0 as the denominator is specific to the MNIST dataset, where the pixel values range from 0 to 255.0. For other datasets, 
the denominator may vary based on the specific range of pixel values present in the data.

'''

# Define the model
model = keras.Sequential(# architectural layers
[
    keras.layers.Flatten(input_shape=(28, 28)), # flattening the input images (28x28 pixels) from 2D array to 1D array of (784 pixels)
    keras.layers.Dense(218, activation='relu'), # artificial neurons = 215/activation function = recitified linear unit
    keras.layers.Dense(10, activation='softmax') # artificial neurons = 10/activation function = softmax
],
    # model name
    name='genesismodel'
    )

''' <- why do we define the model?

█▀▄ █▀▀ █▀▀ █ █▄░█ █ █▄░█ █▀▀   ▀█▀ █░█ █▀▀   █▀▄▀█ █▀█ █▀▄ █▀▀ █░░
█▄▀ ██▄ █▀░ █ █░▀█ █ █░▀█ █▄█   ░█░ █▀█ ██▄   █░▀░█ █▄█ █▄▀ ██▄ █▄▄

ᴄʜᴀᴛɢᴘᴛ sʏsɴᴏᴘsɪs
Defining the model is a crucial step in machine learning because it specifies the architecture, structure, and behavior of the neural network 
that will be trained on the dataset. Here's why we need to define the model:

Architecture Design: Defining the model involves determining the architecture of the neural network, 
which includes the number and arrangement of layers, the type of layers used (e.g., dense, convolutional, recurrent), 
and the connections between them. The architecture design depends on the specific problem and the characteristics of the data. 
By defining the model, we establish the blueprint for how the neural network will process the input data and make predictions.

Model Complexity and Capacity: The model definition allows us to control the complexity and capacity of the neural network. 
Different architectures and configurations have different levels of complexity, which determines the model's ability to capture and 
represent complex patterns and relationships in the data. By defining the model, we can adjust its capacity to balance between underfitting 
(model too simple to learn) and overfitting (model too complex and memorizing the training data).

Layer Configurations: Defining the model involves specifying the configurations of the individual layers within the network. 
Each layer can have different properties, such as the number of units or neurons, activation functions, regularization techniques, and more. 
By configuring the layers, we can shape the behavior and functionality of the network, allowing it to learn and generalize from the input data.

Model Compilation: Once the model is defined, it needs to be compiled before training. 
Compiling the model involves specifying additional properties such as the loss function, optimizer, and evaluation metrics. 
The loss function quantifies the discrepancy between the model's predictions and the true labels, while the optimizer determines 
how the model's weights are updated during training. Defining the model allows us to set these components appropriately based on the 
problem and requirements.

Model Reusability: Defining the model makes it reusable and portable. Once a model is defined, it can be saved to disk and loaded later for retraining,
evaluation, or deployment. By defining the model architecture, it becomes a self-contained entity that can be shared, replicated, or used in 
different projects.
'''

# Compile the model
model.compile(
    optimizer='adam',
        loss='sparse_categorical_crossentropy', 
            metrics='accuracy'
)

''' <- why do we compile the model?

█▀▀ █▀█ █▀▄▀█ █▀█ █ █░░ █▀▀   ▀█▀ █░█ █▀▀   █▀▄▀█ █▀█ █▀▄ █▀▀ █░░
█▄▄ █▄█ █░▀░█ █▀▀ █ █▄▄ ██▄   ░█░ █▀█ ██▄   █░▀░█ █▄█ █▄▀ ██▄ █▄▄

ᴄʜᴀᴛɢᴘᴛ sʏsɴᴏᴘsɪs
Compiling the model is a necessary step before training it on the data. When we compile the model, we specify additional properties that are 
essential for the training process. Here's why we need to compile the model:

Loss Function: The loss function quantifies the discrepancy between the model's predictions and the true labels in the training data. 
It serves as a measure of how well the model is performing. Different machine learning tasks, such as classification or regression, 
require different types of loss functions. When compiling the model, we need to specify the appropriate loss function based on the problem at hand.

Optimizer: The optimizer determines how the model's weights are updated during the training process. It implements a specific algorithm, such as 
Stochastic Gradient Descent (SGD) or Adam, to optimize the model's performance. The choice of optimizer can have a significant impact on the model's 
convergence and learning speed. When compiling the model, we need to specify the optimizer we want to use.

Metrics: Metrics are used to evaluate and monitor the model's performance during training and evaluation. 
Common metrics for classification tasks include accuracy, precision, recall, and F1-score. By specifying the metrics, 
we can track and report these performance measures during the training process.

Additional Parameters: Compiling the model allows us to specify additional parameters, such as learning rate, regularization techniques, or custom 
callbacks. These parameters provide fine-tuning options to improve the model's training process or add specific functionalities.

Once the model is compiled, it is ready to be trained on the training data. The compilation step prepares the model with the necessary 
components for the learning process, such as the loss function, optimizer, and metrics. It sets the stage for the model to learn from the input 
data, optimize its weights, and make predictions.

It's important to note that the choice of loss function, optimizer, and metrics depends on the specific problem and requirements. 
Different tasks may require different combinations of these components. The compilation step allows us to customize these components based on the 
nature of the problem we are solving.
'''

# Train the model
model.fit(train_images, train_labels, epochs=5)

''' <- why do we train the model?

▀█▀ █▀█ ▄▀█ █ █▄░█   ▀█▀ █░█ █▀▀   █▀▄▀█ █▀█ █▀▄ █▀▀ █░░
░█░ █▀▄ █▀█ █ █░▀█   ░█░ █▀█ ██▄   █░▀░█ █▄█ █▄▀ ██▄ █▄▄

ᴄʜᴀᴛɢᴘᴛ sʏsɴᴏᴘsɪs
Training the model is the process of optimizing its parameters (weights and biases) using the provided training data. The main goal of training is 
to enable the model to learn patterns and relationships within the data, so it can make accurate predictions on unseen or new data. Here's why we 
train the model:

Learn from Data: By training the model, we expose it to a large amount of labeled training data. During training, the model adjusts its parameters 
based on the input data and corresponding labels. This adjustment process is driven by the optimization algorithm (e.g., gradient descent) and the 
chosen loss function. Through repeated iterations, the model learns to recognize patterns, extract relevant features, and establish relationships 
between the input data and the target labels.

Optimize Model Parameters: The training process aims to find the optimal values for the model's parameters (weights and biases) that minimize the 
chosen loss function. The optimization algorithm adjusts these parameters iteratively, moving them in the direction that reduces the loss. 
This optimization process allows the model to find the best representation of the underlying patterns in the training data.

Generalize to Unseen Data: Training the model helps it generalize its learning to unseen or new data. The model learns to capture the essential 
patterns and generalize its understanding beyond the training examples it has seen. The goal is to train the model in a way that it can accurately 
predict the labels or make meaningful inferences on unseen instances that it hasn't encountered during training.

Improve Performance: Through training, the model gradually improves its performance over time. As it encounters more training examples and 
undergoes more iterations, it refines its predictions, reduces the training loss, and increases its ability to generalize to new data. 
The training process allows the model to adapt and improve its performance on the specific task it is trained for.

Iterative Feedback Loop: Training the model provides a feedback loop where the model's performance is evaluated and used to guide further improvements. 
By monitoring the model's performance on a validation set or using other evaluation techniques, we can assess how well it is learning and make 
adjustments to the model's architecture, hyperparameters, or training strategy as needed. This iterative process helps refine the model and 
achieve better results.

In summary, training the model is crucial for enabling it to learn from the provided data, optimize its parameters, improve its performance, 
and generalize its understanding to unseen instances. It is the core step in the machine learning workflow, where the model learns to make 
accurate predictions based on the patterns and relationships in the training data.
'''

# Evaluate the model
test_loss, test_acc = model.evaluate(test_images, test_labels)
print('genesismodel test accuracy:', test_acc)

''' <- why do we evaluate the model?

█▀▀ █░█ ▄▀█ █░░ █░█ ▄▀█ ▀█▀ █▀▀   ▀█▀ █░█ █▀▀   █▀▄▀█ █▀█ █▀▄ █▀▀ █░░
██▄ ▀▄▀ █▀█ █▄▄ █▄█ █▀█ ░█░ ██▄   ░█░ █▀█ ██▄   █░▀░█ █▄█ █▄▀ ██▄ █▄▄

ᴄʜᴀᴛɢᴘᴛ sʏsɴᴏᴘsɪs

Evaluating the model is an important step in assessing its performance and determining how well it generalizes to unseen data. 
Here's why we evaluate the model:

Performance Assessment: Evaluating the model allows us to measure its performance on unseen or new data. By providing a separate dataset, 
called a test set or validation set, we can evaluate how well the model generalizes its learning beyond the training data. It helps us understand 
the model's accuracy, precision, recall, or other relevant metrics, which are crucial in assessing its quality and effectiveness.

Generalization Check: Evaluating the model helps us assess its ability to generalize and make accurate predictions on data it hasn't seen during 
training. It measures how well the model can understand and capture the underlying patterns in the data, without overfitting (memorizing) the 
training examples. Evaluating the model on unseen data provides an unbiased estimate of its performance in real-world scenarios.

Model Selection and Comparison: Evaluation allows us to compare different models or variations of the same model. 
By evaluating and comparing their performance metrics, such as accuracy or loss, we can make informed decisions 
about which model to choose for a given task. It helps us select the most suitable model architecture, hyperparameters, 
or training strategies based on their performance on the evaluation data.

Hyperparameter Tuning: Evaluation is essential for tuning the model's hyperparameters. 
Hyperparameters are parameters that define the model's configuration or training process but are not learned from the data. 
Examples include learning rate, batch size, or regularization strength. By evaluating the model's performance with different 
hyperparameter settings, we can select the optimal values that yield the best results.

Model Deployment Decision: Evaluation results influence the decision of whether to deploy the model in a real-world application or not. 
By understanding the model's performance and limitations through evaluation, we can determine if it meets the desired accuracy or 
quality thresholds for the specific use case. It helps us make informed decisions about whether the model is reliable and suitable for deployment.

In summary, evaluating the model is crucial for assessing its performance, measuring its generalization ability, comparing different models, 
tuning hyperparameters, and making informed decisions about model selection and deployment. It provides insights into the model's effectiveness, 
reliability, and suitability for real-world applications.
'''