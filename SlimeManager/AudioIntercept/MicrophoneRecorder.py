import pyaudio
import wave

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "output.wav"

p = pyaudio.PyAudio()

dev_index = None
for i in range(p.get_device_count()):
    dev = p.get_device_info_by_index(i)
    print(dev)
    if (dev['name'] == 'MacBook Pro Speakers' and dev['hostApi'] == 0):
        dev_index = dev['index']
        print('dev_index', dev_index)

# SPEAKERS = p.get_default_output_device_info()["hostApi"] #The part I have modified
""" Microphone """
# stream = p.open(format = FORMAT,
#                 channels = 1,
#                 rate = RATE,
#                 input = True,
#                 input_device_index = 1,
#                 frames_per_buffer = CHUNK)

""" System Audio """
stream = p.open(format=FORMAT,
                channels=2,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK,
                input_device_index=2)

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()