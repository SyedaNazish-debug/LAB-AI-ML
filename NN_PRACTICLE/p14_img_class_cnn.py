import tensorflow as tf
import matplotlib.pyplot as plt
import os

dataset_path = "dataset1"

IMAGE_SIZE =(128,128)
BATCH_SIZE =32

train_ds = tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="training",
    seed = 123,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE
)

val_ds=tf.keras.utils.image_dataset_from_directory(
    dataset_path,
    validation_split=0.2,
    subset="validation",
    seed = 123,
    image_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE
)

class_name=train_ds.class_names
print("classes:",class_name)

model=tf.keras.Sequential([
    tf.keras.layers.Input(shape=(128,128,3)),
    tf.keras.layers.Rescaling(1./255),
    tf.keras.layers.Conv2D(
        32,(3,3),
        activation="relu"
    ),

    tf.keras.layers.MaxPool2D(
        (2,2)
    ),

    tf.keras.layers.Conv2D(
        64,(3,3),
        activation="relu"
    ),
    tf.keras.layers.MaxPool2D(
        (2,2)
    ),

# second

        tf.keras.layers.Conv2D(
        128, (3, 3), activation="relu"
    ),
    tf.keras.layers.MaxPooling2D(
        (2, 2)
    ),

    tf.keras.layers.Conv2D(
        128,(3,3), activation="relu"
    ),

    tf.keras.layers.MaxPool2D(
        (2,2)
    ),

    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(
        128,activation="relu"
    ),

    tf.keras.layers.Dense(
        1, activation="sigmoid"
    )
])

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
 

model.summary()
 

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=5
)

loss, accuracy = model.evaluate(val_ds)
 
print("Validation Loss:", loss)
print("Validation Accuracy:", accuracy)

