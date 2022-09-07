import tensorflow as tf
from tensorflow.keras.applications.xception import Xception
from tensorflow.keras.models import load_model
import numpy as np


gpu_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(gpu_devices[0], True)
logical_gpu_devices = tf.config.list_logical_devices('GPU')

model = Xception()
img = np.zeros([299,299,3],dtype=np.uint8)

print(model.predict(np.array([tf.keras.applications.xception.preprocess_input(img)])))

# import tensorflow as tf
# gpus = tf.config.experimental.list_physical_devices('GPU')
# if gpus:
#   for gpu in gpus:
#     tf.config.experimental.set_memory_growth(gpu, True)
# else:
#   print("No GPU device found")