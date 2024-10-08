# -*- coding: utf-8 -*-
"""DAY_7_CNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1f8I20xOYWAVlrPs4Og4Ny2SvDH5xOEyb
"""

import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator

#define image size and batch size
IMG_SIZE=224
BATCH_SIZE=32

#creating training data
train_datagen =ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2

)

#creating training data with above parameters

#folder=parameters.flow_from_directory(path,ts,bs,cm,subset)
train_generator=train_datagen.flow_from_directory(
r'/content/drive/MyDrive/Brain_Tumor_Detection-20240301T092752Z-001/Brain_Tumor_Detection/Train',
target_size=(IMG_SIZE,IMG_SIZE),
batch_size=BATCH_SIZE,
class_mode='binary',
subset='training'
)

#creating validation data
valid_generator=train_datagen.flow_from_directory(
r'/content/drive/MyDrive/Brain_Tumor_Detection-20240301T092752Z-001/Brain_Tumor_Detection/Train',
target_size=(IMG_SIZE,IMG_SIZE),
batch_size=BATCH_SIZE,
class_mode='binary',
subset='validation'
)

#define the model
model=keras.Sequential([
    layers.Conv2D(32,(3,3),activation='relu',input_shape=(IMG_SIZE,IMG_SIZE,3)),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(64,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Conv2D(128,(3,3),activation='relu'),
    layers.MaxPooling2D((2,2)),
    layers.Flatten(),
    layers.Dense(128,activation='relu'),
    layers.Dense(1,activation='sigmoid')
])

#compile the model
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(train_generator,validation_data=valid_generator,epochs=5)

model.save("Model.h5","label.txt")