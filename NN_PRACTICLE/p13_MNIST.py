import tensorflow as tf
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()

X_train = X_train.astype("float32")/255.0
X_test = X_test.astype("float32")/255.0

X_train = X_train[...,tf.newaxis]
X_test = X_test[...,tf.newaxis]

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(28,28,1)),
    tf.keras.layers.Conv2D(
        32,(3,3),activation="relu"
    ),

    tf.keras.layers.MaxPool2D((2,2)
    ),

    tf.keras.layers.Conv2D(
        64,(3,3),activation="relu"
    ),

    tf.keras.layers.MaxPool2D((2,2)
    ),

    tf.keras.layers.Flatten(),

    tf.keras.layers.Dense(
        128,activation="relu"
    ),

    tf.keras.layers.Dense(
        10,activation="softmax"
    )
])

model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


model.summary()
history = model.fit(
    X_train,
    y_train,
    epochs=5,
    batch_size=32,
    validation_split=0.1
)

test_loss,test_acc =model.evaluate(
    X_test,
    y_test,
    verbose=0
)

print("Test loss:",test_loss)
print("Test accuracy:",test_acc)
index=0

predictions = model.predict(
    X_test[index:index+1],
    verbose=0
)

predict_digit = predictions.argmax()
print("True digit:",y_test[index])
print("prediction:",predict_digit)

plt.imshow(
    X_test[index].squeeze(),
    cmap="gray"
)
plt.title(
    f"Actual:{y_test[index]},"
    f"Prediction:{predict_digit}"
)

plt.axis("off")
plt.show()