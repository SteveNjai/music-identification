# for data transformation
import numpy as np
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
import scipy.io.wavfile as wavfile

def spectrogram(file,playtime, window_size, srate):
    # function to generate the spectrogram.
    #window size is the size in power of 2
    #srate is the sampling rate.
    #playtime is the duration of sample to analyze in seconds

    Fs, aud = wavfile.read(file)
    #average out left and right channels
    aud = aud[:, 0]  # select left channel only

    first = aud[:int(Fs * playtime)]  # trim the first 125 seconds
    powerSpectrum, frequenciesFound, time, imageAxis = plt.specgram(first,Fs=srate, NFFT=window_size)
    plt.title('Spectrogram: '+ file)
    plt.xlabel('time, s')
    plt.ylabel('Frequency, Hz')
    plt.show()

