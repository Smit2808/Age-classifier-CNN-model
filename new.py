import os
import pathlib
import numpy as np
import tensorflow as tf
from tensorflow.keras.layers.experimental.preprocessing import Rescaling
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization, InputLayer
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.losses import CategoricalCrossentropy
from tensorflow.keras.callbacks import TensorBoard, ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras import backend as k

model = tf.keras.models.load_model('best_model.h5')

img_pred = image.load_img('output.jfif', target_size=(48, 48))
img_pred = image.img_to_array(img_pred)
img_pred = np.expand_dims(img_pred, axis=0)
rslt = model.predict(img_pred)
print(rslt)

r1=np.argmax(rslt)
print(r1)

if r1 == 0:
	print("1-10")
elif r1 == 1:
	print("11-20")
elif r1 == 2:
	print("21-30")
elif r1 == 3:
	print("31-40")
elif r1 == 4:
	print("41-50")
elif r1 == 5:
	print("51-60")
elif r1 == 6:
	print("60+")