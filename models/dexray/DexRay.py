import numpy as np
import tensorflow as tf
from PIL import Image

def get_image(path_img):
    image = np.asarray(Image.open(path_img))
    image = tf.convert_to_tensor(image, dtype_hint=None, name=None)
    return image

def get_shape(image):
    return image.shape[0]

def decode_img(path_img):
    image = get_image(path_img)
    shape = tf.numpy_function(get_shape, [image], tf.int64)
    image = tf.reshape(image, [shape, 1, 1])
    image = tf.image.convert_image_dtype(image, tf.float32)
    image = tf.image.resize(image, [IMG_SIZE*IMG_SIZE, 1])
    return tf.reshape(image, [IMG_SIZE*IMG_SIZE, 1])

IMG_SIZE = 128