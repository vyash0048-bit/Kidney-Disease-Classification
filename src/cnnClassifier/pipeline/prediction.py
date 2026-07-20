import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        # Apply the same monkey patch as in evaluation to avoid quantization_config errors
        import keras
        original_dense_init = keras.layers.Dense.__init__
        def new_dense_init(self, *args, **kwargs):
            kwargs.pop("quantization_config", None)
            original_dense_init(self, *args, **kwargs)
        keras.layers.Dense.__init__ = new_dense_init
        
        try:
            model = tf.keras.models.load_model(os.path.join("artifacts", "training", "trained_model.keras"))
        finally:
            keras.layers.Dense.__init__ = original_dense_init

        imagename = self.filename
        test_image = image.load_img(imagename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        
        # Scale the image just like the training/validation data generators
        test_image = test_image / 255.0

        result = np.argmax(model.predict(test_image), axis=1)
        print("Prediction result index:", result)

        if result[0] == 0:
            prediction = 'Cyst'
        elif result[0] == 1:
            prediction = 'Normal'
        elif result[0] == 2:
            prediction = 'Stone'
        elif result[0] == 3:
            prediction = 'Tumor'
        else:
            prediction = 'Unknown'
            
        return [{"image": prediction}]