import tensorflow as tf
from discriminator import build_discriminator
from generator import build_generator
import numpy as np


def load_real_data(filename):
    with open(filename, 'r') as infile:
        return [float(line.strip()) for line in infile]


def train_gan(generator, discriminator, gan_model, real_data, epochs=1000, batch_size=128, visualize=False):
    half_batch = batch_size // 2

    for epoch in range(epochs):
        #Train discriminator
        #Select a random half batch of real data
        idx = np.random.randint(0, len(real_data, half_batch))
        real_samples = real_data[idx]

def create_gan_model(alpha=2.0, discriminator_lr=0.0001, generator_lr=0.0001, epochs=1000, save_model=False, model_path='./15 Feb/models/gan_models.keras'):
    discriminator = build_discriminator()

    generator = build_generator()
    #Build combines GAN model
    initial_noise = tf.keras.Input(shape=(10,))
    initial_fake = generator(initial_noise)
    discriminator.trainable = False
    validity = discriminator(initial_fake)
    gan_model = tf.keras.Model(initial_noise, validity)

    gan_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

    real_data = load_real_data('./15 Feb/data/random_numbers.txt')


    #Train GAN
    train_gan(generator, discriminator, gan_model, real_data, epochs=epochs, visualize=False)








create_gan_model()