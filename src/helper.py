import os
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow.keras.models import load_model


class PlantSpeciesInference:
    def __init__(self, model_path):
        """Initialize with the pre-trained model."""
        self.model = load_model(model_path)

    def prepare_image(self, img_path, target_size=(128, 128)):
        """Load and preprocess the image for inference."""
        img = image.load_img(img_path, target_size=target_size)
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0
        return img_array

    def predict(self, img_path):
        """Make a prediction on the image."""
        img_array = self.prepare_image(img_path)
        predictions = self.model.predict(img_array)
        class_idx = np.argmax(predictions, axis=1)
        return class_idx[0]

    def evaluate_model(self, data_dir):
        """Evaluate the model performance on test data."""
        test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale=1./255)
        test_generator = test_datagen.flow_from_directory(
            data_dir,
            target_size=(128, 128),
            batch_size=32,
            class_mode='categorical')

        loss, accuracy = self.model.evaluate(test_generator)
        return loss, accuracy

if __name__ == "__main__":
    # Example for running inference
    inference = PlantSpeciesInference('plant_species_model.h5')
    result = inference.predict('path_to_image.jpg')
    print(f"Predicted class: {result}")

    # Example for model evaluation
    loss, accuracy = inference.evaluate_model('path_to_test_data')
    print(f"Test loss: {loss}, Test accuracy: {accuracy}")