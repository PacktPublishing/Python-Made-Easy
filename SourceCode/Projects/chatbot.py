# Install required modules
# pip install numpy tensorflow keras nltk

import json 
import numpy as np 
import tensorflow as tf
from tensorflow.keras import layers
import random

import nltk
from nltk.stem import WordNetLemmatizer
nltk.download('punkt')
nltk.download('wordnet')

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

vocab = []
tags = []
xy = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        vocab.extend(w)
        xy.append((w, tag))

# lemmatization
vocab = [lemmatizer.lemmatize(w.lower()) for w in vocab if w not in ["?", "!", ".", ","]]
vocab = sorted(list(set(vocab)))

classes = sorted(list(set(tags)))

print(len(xy), "patterns")
print(len(classes), "classes:", classes)
print(len(vocab), "unique lemmatized words:", vocab)

X_train = []
y_train = []
for (pattern_sentence, tag) in xy:
    bag = []
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_sentence]
    for word in vocab:
        bag.append(1) if word in pattern_words else bag.append(0)
    X_train.append(bag)

    label = classes.index(tag)
    y_train.append(label)

X_train = np.array(X_train)
y_train = np.array(y_train)

# Creating a neural network.
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, input_shape=(len(X_train[0]),), activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(len(classes), activation='softmax')
])

# Compiling the model. Using Stochastic Gradient Descent as optimizer and Sparse Categorical Crossentropy as loss function.
sgd = tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='sparse_categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

hist = model.fit(X_train, y_train, epochs=200, batch_size=5, verbose=1)

# Saving the trained model.
model.save('chatbot_model.h5', hist)
