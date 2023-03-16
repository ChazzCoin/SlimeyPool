import pygame
import numpy as np
import librosa
import matplotlib.cm as cm
from matplotlib import pyplot as plt
from numpy.fft import fft

def beat_detection(samples, sample_rate):
    bpm = None
    # Compute the autocorrelation of the audio signal
    autocorrelation = np.correlate(samples, samples, mode="full")
    autocorrelation = autocorrelation[len(autocorrelation) // 2:]
    autocorrelation = autocorrelation / np.max(autocorrelation)

    # Find the first local maximum that is greater than a threshold
    threshold = 0.1
    for i, x in enumerate(autocorrelation):
        if x > threshold and (i == 0 or x > autocorrelation[i - 1]) and (
                i == len(autocorrelation) - 1 or x > autocorrelation[i + 1]):
            bpm = sample_rate / i
            break

    return bpm

def detect_beat(audio_signal, sample_rate):
    """
    Detect beat frequency in audio signal using Tzanetakis and Cook algorithm
    Parameters:
        audio_signal (ndarray): audio signal data
        sample_rate (int): sample rate of the audio signal
    Returns:
        float: beat frequency
    """
    # Analyze audio data
    samples = np.array(audio_signal, dtype=float)
    spectrum = np.abs(fft(samples))
    # Find peaks in spectrum
    peak_indices = np.argwhere(np.r_[True, spectrum[1:] > spectrum[:-1]] & np.r_[spectrum[:-1] > spectrum[1:], True])[:,0]
    # Calculate beat period
    beat_period = sample_rate / peak_indices.mean()
    # Calculate beat frequency
    beat_frequency = sample_rate / beat_period
    return beat_frequency

# Initialize pygame
pygame.init()

# Load an image
img = pygame.image.load("image.jpg")

# Get the screen size
screen = pygame.display.set_mode(img.get_size())

# Load the audio file
# pygame.mixer.music.load("summer.mp3")

# Start playing the audio
# pygame.mixer.music.play()

samples, sample_rate = librosa.load("summer.mp3", sr=None, mono=True)
# Perform beat detection
tempo, beats = librosa.beat.beat_track(y=samples, sr=sample_rate)
plt.plot(b)
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()





# Define a color map
# cmap = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]])
# Repeat the color map to match the number of beats
# cmap = np.tile(cmap, (len(beats), 1))

cmap = cm.get_cmap("hsv", 256)
cmap = cmap(np.arange(256))[:, :3] * 255

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current time of the song
    time = pygame.mixer.music.get_pos()

    # Find the closest beat to the current time
    beat_index = np.searchsorted(beats, time / 1000 * sample_rate, side="left") % len(beats)

    # Change the pixels of the image based on the beat
    img_array = np.array(img)
    # img_array[:, :, :] = cmap[beat_index % len(cmap), :]
    # img_array[:, :, :] = cmap[beat_index, :]
    img_array[:, :, :] = cmap[beat_index % len(cmap), :]
    img = pygame.surfarray.make_surface(img_array)

    # Draw the image on the screen
    screen.blit(img, (0, 0))
    pygame.display.update()

# Quit pygame
pygame.quit()
