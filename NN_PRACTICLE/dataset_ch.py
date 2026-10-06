import tensorflow as tf
import os

dataset_path = "cat_dog"

IMAGE_SIZE = (128, 128)
BATCH_SIZE = 32
SEED = 123


# ==========================================
# 1. Get all image filenames
# ==========================================

all_files = [
    os.path.join(dataset_path, filename)
    for filename in os.listdir(dataset_path)
    if filename.lower().endswith((".jpg", ".jpeg", ".png"))
]

print("Total images:", len(all_files))


# ==========================================
# 2. Create labels
# ==========================================

labels = []

for filepath in all_files:

    filename = os.path.basename(filepath).lower()

    if filename.startswith("cat."):
        labels.append(0)

    elif filename.startswith("dog."):
        labels.append(1)


print("Total labels:", len(labels))
print("First 10 labels:", labels[:10])


# ==========================================
# 3. Shuffle file paths and labels
# ==========================================

import random

combined = list(zip(all_files, labels))

random.seed(SEED)
random.shuffle(combined)

all_files, labels = zip(*combined)

all_files = list(all_files)
labels = list(labels)


# ==========================================
# 4. Train / Validation split
# ==========================================

total_images = len(all_files)

train_size = int(0.8 * total_images)

train_files = all_files[:train_size]
train_labels = labels[:train_size]

val_files = all_files[train_size:]
val_labels = labels[train_size:]

print("Training images:", len(train_files))
print("Validation images:", len(val_files))


# ==========================================
# 5. Create TensorFlow datasets
# ==========================================

train_ds = tf.data.Dataset.from_tensor_slices(
    (train_files, train_labels)
)

val_ds = tf.data.Dataset.from_tensor_slices(
    (val_files, val_labels)
)


# ==========================================
# 6. Load images
# ==========================================

def load_image(filepath, label):

    image = tf.io.read_file(filepath)

    image = tf.image.decode_jpeg(
        image,
        channels=3
    )

    image = tf.image.resize(
        image,
        IMAGE_SIZE
    )

    return image, label


train_ds = train_ds.map(
    load_image,
    num_parallel_calls=tf.data.AUTOTUNE
)

val_ds = val_ds.map(
    load_image,
    num_parallel_calls=tf.data.AUTOTUNE
)


# ==========================================
# 7. Batch
# ==========================================

train_ds = train_ds.batch(BATCH_SIZE)
val_ds = val_ds.batch(BATCH_SIZE)


# ==========================================
# 8. Prefetch
# ==========================================

train_ds = train_ds.prefetch(tf.data.AUTOTUNE)
val_ds = val_ds.prefetch(tf.data.AUTOTUNE)


print("Dataset ready!")

# ==========================================
# 9. CNN Model
# ==========================================

model = tf.keras.Sequential([

    tf.keras.layers.Input(
        shape=(128, 128, 3)
    ),

    tf.keras.layers.Rescaling(
        1./255
    ),

    tf.keras.layers.Conv2D(
        32,
        (3, 3),
        activation="relu"
    ),

    tf.keras.layers.MaxPooling2D(
        (2, 2)
    ),

    tf.keras.layers.Conv2D(
        64,
        (3, 3),
        activation="relu"
    ),

    tf.keras.layers.MaxPooling2D(
        (2, 2)
    ),

    tf.keras.layers.Conv2D(
        128,
        (3, 3),
        activation="relu"
    ),

    tf.keras.layers.MaxPooling2D(
        (2, 2)
    ),

    tf.keras.layers.Conv2D(
        128,
        (3, 3),
        activation="relu"
    ),

    tf.keras.layers.MaxPooling2D(
        (2, 2)
    ),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(
        128,
        activation="relu"
    ),

    # 0 = Cat
    # 1 = Dog
    tf.keras.layers.Dense(
        1,
        activation="sigmoid"
    )
])


# ==========================================
# 10. Compile
# ==========================================

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)


# ==========================================
# 11. Model summary
# ==========================================

model.summary()


# ==========================================
# 12. Train
# ==========================================

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=5
)


# ==========================================
# 13. Evaluate
# ==========================================

loss, accuracy = model.evaluate(val_ds)

print("Validation Loss:", loss)
print("Validation Accuracy:", accuracy)