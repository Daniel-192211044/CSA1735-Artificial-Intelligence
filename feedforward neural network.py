import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

np.random.seed(0)
X = np.random.rand(100, 10)
y = np.random.randint(2, size=100)

model = Sequential()

model.add(Dense(32, activation='relu', input_shape=(10,)))
model.add(Dense(1, activation='sigmoid'))

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(X, y, epochs=10, batch_size=32, validation_split=0.2)

loss, accuracy = model.evaluate(X, y)
print(f"Loss: {loss}, Accuracy: {accuracy}")
