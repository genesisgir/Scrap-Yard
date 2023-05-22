# imports
import numpy
from genesismodel import model
from PIL import Image

# Load and preprocess the image
image_path = r'Scrap-Yard\Lab-Sketches-May-2023\ANN\google-images\sampleimage2.png'
image = Image.open(image_path).convert('L') # Convert to grayscale
image = image.resize((28, 28)) # Resize to 28x28 pixels
image = numpy.array(image) / 255.0 # Normalize pixel values

# Reshape the image
image = image.reshape(1, 28, 28) # Reshape to a 1D vector

# Pass the image through the ANN (genesismodel)
predictions = model.predict(image)

# Interpret the predictions
predicted_digit = numpy.argmax(predictions)

# display prediction
print("Predicted digit:", predicted_digit)