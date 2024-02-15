from discriminator import build_discriminator
from generator import build_generator

def train_gan():
    pass

def create_gan_model(alpha=2.0, discriminator_lr=0.0001, generator_lr=0.0001, epochs=1000, save_model=False, model_path='./15 Feb/models/gan_models.keras'):
    discriminator = build_discriminator()

    generator = build_generator()