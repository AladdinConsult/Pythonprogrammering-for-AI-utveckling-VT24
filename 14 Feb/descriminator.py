from tensorflow import keras
from keras.models import Sequential
from keras.models import Dense

def build_discriminator(optimizer ='adam', loss='binary_crossentropy', metrics =['accuracy']):
    model = Sequential()

    #Input layer
    model.add(Dense(128, activation = 'relu', input_shape=(1,)))

    #Hidden  layer

    # Output layer