import tensorflow as tf
import tensorflow_io as tfio
import matplotlib.pyplot as plt
from IPython.display import Audio

audio = tfio.audio.AudioIOTensor('./test.mp3')
#print(audio)
print(audio[:10, 0])