# for data transformation
import numpy as np
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
import scipy.io.wavfile as wavfile

#import files
from specgram import spectrogram
from fingerprinting import freq_plot

#parameters
audio = 'Audio files/awakening - january.wav'
playtime =2 #seconds to analyze
sample_rate = 44100
window_size = 2048

#run spectrogram function
freq_plot(audio,playtime)
#run FFT function
spectrogram(audio,playtime, window_size, sample_rate) #call the spectrogram