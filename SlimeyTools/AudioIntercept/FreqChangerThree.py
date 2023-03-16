import pyaudio
import wave
import numpy as np
from scipy.io.wavfile import read
from F import OS
# Set the parameters for the audio stream
p = pyaudio.PyAudio()
channels = 1
sample_rate = 44100
sample_width = 2

cwd = OS.get_cwd()
filename = f"{cwd}/test.wav"
# Open the wav file
rate, data = read(filename)

# Get the audio data as a numpy array
sine_wave = np.array(data, dtype=np.float32)

# Change the frequency of the wav file
frequency = 440  # Change this to change the frequency of the audio
sine_wave = sine_wave * (frequency/rate)

# Open the audio stream
stream = p.open(format=p.get_format_from_width(sample_width),
                channels=channels,
                rate=sample_rate,
                output=True)

# Write the audio data to the stream
stream.write(sine_wave.tobytes())

# Close the audio stream
stream.stop_stream()
stream.close()
p.terminate()