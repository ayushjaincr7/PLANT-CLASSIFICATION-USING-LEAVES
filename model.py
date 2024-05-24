from keras.models import load_model
from keras.utils import img_to_array
import numpy as np
from PIL import Image
from tensorflow.keras.applications.resnet50 import preprocess_input

model = load_model('trained_model/model.h5')

def preprocessing_img(img_path):
    op_img = Image.open(img_path)
    img_resize = op_img.resize((224,224))
    img2arr = img_to_array(img_resize)
    img_preprocessed = preprocess_input(img2arr)  # Preprocess the image
    img_reshape = img_preprocessed.reshape(1, 224, 224, 3)
    return img_reshape

def predict_result(predict):
    pred = model.predict(predict)
    class_index = np.argmax(pred, axis=1)[0] # Get the index of the most probable class
    probability = pred[0][class_index] * 100  # Convert to percentage
    return class_index, probability
