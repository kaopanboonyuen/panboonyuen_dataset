import os
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from sklearn.model_selection import train_test_split


class PlantSpeciesModel:
    def __init__(self, image_size=(128, 128), batch_size=32, num_classes=10):
        """Initialize the model with parameters."""
        self.image_size = image_size
        self.batch_size = batch_size
        self.num_classes = num_classes
        self.model = None

    def build_model(self):
        """Build a CNN model."""
        model = models.Sequential([
            layers.InputLayer(input_shape=(self.image_size[0], self.image_size[1], 3)),
            layers.Conv2D(32, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(128, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dropout(0.5),
            layers.Dense(self.num_classes, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        return model

    def prepare_data(self, data_dir):
        """Prepare data using ImageDataGenerator."""
        train_datagen = ImageDataGenerator(rescale=1.0/255.0, 
                                           rotation_range=40, 
                                           width_shift_range=0.2, 
                                           height_shift_range=0.2, 
                                           shear_range=0.2, 
                                           zoom_range=0.2, 
                                           horizontal_flip=True, 
                                           fill_mode='nearest')

        test_datagen = ImageDataGenerator(rescale=1.0/255.0)

        train_generator = train_datagen.flow_from_directory(
            os.path.join(data_dir, 'train'),
            target_size=self.image_size,
            batch_size=self.batch_size,
            class_mode='categorical')

        validation_generator = test_datagen.flow_from_directory(
            os.path.join(data_dir, 'validation'),
            target_size=self.image_size,
            batch_size=self.batch_size,
            class_mode='categorical')

        return train_generator, validation_generator

    def train_model(self, data_dir, epochs=10, save_model=True):
        """Train the model."""
        train_generator, validation_generator = self.prepare_data(data_dir)

        self.model = self.build_model()

        checkpoint = ModelCheckpoint('best_model.h5', save_best_only=True)
        early_stopping = EarlyStopping(monitor='val_loss', patience=5)

        history = self.model.fit(
            train_generator,
            epochs=epochs,
            validation_data=validation_generator,
            callbacks=[checkpoint, early_stopping])

        if save_model:
            self.model.save('plant_species_model.h5')

        return history

if __name__ == "__main__":
    # Train the model with your image data
    model = PlantSpeciesModel()
    model.train_model(data_dir='my_path_to_data_directory', epochs=20)