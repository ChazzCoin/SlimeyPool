import sys

import librosa
from pydub import AudioSegment
import pygame
import numpy as np
from numpy.fft import fft


def modify_pixels_to_beat(image_data, beat_samples, beat_strength, max_offset):
    # Get shape of image data
    img_shape = image_data.shape
    # Create a copy of the image data to modify
    modified_data = image_data.copy()
    # Loop through each beat sample
    for i, sample in enumerate(beat_samples):
        # Map beat strength to an offset
        offset = int(beat_strength[i] * max_offset)
        # Modify pixels based on offset
        for j in range(img_shape[0]):
            # Check if new position is within bounds
            new_pos = j - offset
            if 0 <= new_pos < img_shape[0]:
                # Modify pixels
                modified_data[j, :, :] = image_data[new_pos, :, :]
    return modified_data


samples, sample_rate = librosa.load("summer.mp3", sr=None, mono=True)
# Perform beat detection
strength = librosa.beat.beat_track(y=samples, sr=sample_rate)
tempo, beats = librosa.beat.beat_track(y=samples, sr=sample_rate)

# Initialize Pygame
pygame.init()
# Set window size
WIDTH, HEIGHT = 800, 600
# Create Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Load image file
image = pygame.image.load("image.JPG")
image_data = pygame.surfarray.array3d(image)
# Load and play audio file
pygame.mixer.init()
pygame.mixer.music.load("summer.mp3")
pygame.mixer.music.play()

# Analyze audio data
# samples = np.array(pygame.mixer.music.get_pos(), dtype=float)
# spectrum = np.abs(fft(samples))

# Load the audio file
# audio = AudioSegment.from_file("bartender.mp3", format="mp3")
# Convert the audio to a numpy array
# audio_signal = audio.get_array_of_samples()
# Get the sample rate
# sample_rate = audio.frame_rate

# Convert the audio to a single channel audio signal
# audio_channels = audio.set_channels(1)
# Get the audio signal as a numpy array
# samples = np.array(audio_channels.get_array_of_samples(), dtype=float)

# Perform the FFT on the audio signal
# spectrum = np.abs(np.fft.rfft(samples))
spectrum = np.abs(fft(samples))
# Detect beat frequency
# beat_frequency = detect_beat(audio_signal, sample_rate)
original_image = image_data
# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Clear screen
    screen.fill((0, 0, 0))

    # Check if current sample is a beat
    pos = pygame.mixer.music.get_pos()
    if pos % beats.any() == 0:
        print("Pos == Beat")
        # Modify image data based on audio data
        for i, s in enumerate(spectrum):
            # print("Spectrum Looper")
            # Map audio data to position offset
            offset = int(s * 100)

            # Modify position of image data
            imgShape = image_data.shape[0]
            off = i + offset
            if off >= 0 and off < imgShape:
                image_data[i, :, :] = image_data[off, :, :]
            else:
                # Handle out-of-bounds indices
                if off < 0:
                    off = 0
                else:
                    off = imgShape - 1
                image_data[i, :, :] = image_data[off, :, :]
        # Render modified image
        print(np.sum(np.abs(image_data - original_image)))
        screen.blit(pygame.surfarray.make_surface(image_data), (0, 0))
        # Update display
        pygame.display.update()