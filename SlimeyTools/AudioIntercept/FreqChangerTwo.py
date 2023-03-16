import wave
import numpy as np
from F import OS

cwd = OS.get_cwd()
filename = f"{cwd}/test.wav"

with wave.open(filename, 'r') as wav_file:
    # Get the audio data as a numpy array
    sine_wave = np.frombuffer(wav_file.readframes(-1), np.int16)
    rate = wav_file.getframerate()
    # Change the frequency of the wav file
    frequency = 440  # Change this to change the frequency of the audio
    sine_wave = sine_wave * (frequency/rate)
    # Open the output wav file
    with wave.open("output.wav", 'w') as output_wav_file:
        # Set the parameters of the output wav file
        output_wav_file.setparams(wav_file.getparams())
        # Write the modified audio data to the output wav file
        output_wav_file.writeframes(sine_wave.tostring())