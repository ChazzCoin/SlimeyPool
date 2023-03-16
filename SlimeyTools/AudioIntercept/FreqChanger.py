import pyaudio
import numpy as np

# Set the parameters for the audio stream
p = pyaudio.PyAudio()
channels = 1
sample_rate = 44100
sample_width = 2

# Open the audio stream
stream = p.open(format=p.get_format_from_width(sample_width),
                channels=channels,
                rate=sample_rate,
                output=True)

# Generate a sine wave with a desired frequency
frequency = 440  # Change this to change the frequency of the sine wave
sine_wave = (np.sin(2*np.pi*np.arange(sample_rate)*frequency/sample_rate)).astype(np.float32)

# Write the sine wave to the audio stream
stream.write(sine_wave.tobytes())

# Close the audio stream
stream.stop_stream()
stream.close()
p.terminate()