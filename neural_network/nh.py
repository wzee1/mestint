from keras.api.models import Sequential
from keras.api.layers import Dense
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn.metrics import classification_report
import numpy as np

# load the dataset
data = np.loadtxt('pima-indians-diabetes.csv', delimiter=',')
ROW_LENGTH = 8

# split into input (X) and output (y) variables
X = data[:, :ROW_LENGTH]
y = data[:, ROW_LENGTH]

# split dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# determining if the dataset is multiclass or not
IS_MULTICLASS = False
if IS_MULTICLASS:
    LAST_ACTIVATION = "softmax"
    MODEL_LOSS = "categorical_crossentropy"
else:
    LAST_ACTIVATION = "sigmoid"
    MODEL_LOSS = "binary_crossentropy"

# define the keras model
model = Sequential()
model.add(Dense(8, input_dim=ROW_LENGTH, activation='relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(24, activation='relu'))
model.add(Dense(1, activation=LAST_ACTIVATION))
model.compile(loss=MODEL_LOSS, metrics=['accuracy'])

# fit the keras model on the dataset
history = model.fit(X_train, y_train, batch_size=32, epochs=100)

# plot loss value
plt.plot(history.history['loss'])
plt.show()

plt.plot(history.history['accuracy'])
plt.show()
# evaluate the keras model
res = model.evaluate(X_test, y_test, return_dict=True)
print(res)

# last step:
y_pred_test = model.predict(X_test)
if IS_MULTICLASS:
    y_pred_test_classes = np.argmax(y_pred_test, axis=1)
else:
    y_pred_test_classes = (y_pred_test > 0.5).astype(int)
print(classification_report(y_test, y_pred_test_classes))