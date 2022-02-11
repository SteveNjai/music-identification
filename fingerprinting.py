# for data transformation
import numpy as np
# for visualizing the data
import matplotlib.pyplot as plt
# for opening the media file
import scipy.io.wavfile as wavfile

def freq_plot(file,playtime):
    #plot the amplitude vs frequency
    plt.rcParams['figure.dpi'] = 100
    sampFreq, sound = wavfile.read(file)

    #average the left and right channels
    signal = sound[:, 0] #selet left channel only
    signal_final = signal[:int(sampFreq*playtime)]  #play for 'playtime' seconds
    min_amp = min(signal_final) #minimum amplitude
    max_amp = max(signal_final) #maximum amplitude
    avg_amp = (min_amp + max_amp)/2 #average amplitude

    #FFT calculations
    fft_spectrum = np.fft.rfft(signal_final)    #fft spectrum amplitudes
    freq = np.fft.rfftfreq(signal_final.size, d=1. / sampFreq)  #frequency data
    fft_spectrum_abs = np.abs(fft_spectrum) #absolute value of fft spectrum amplitudes
    fft_spectrum_abs_max = max(fft_spectrum_abs)    #max value of fft amplitudes
    fft_spectrum_abs_normalized = fft_spectrum_abs/fft_spectrum_abs_max #normalized amplitudes

    #identify peak amplitudes at a certain frequency for the block
    for i, f in enumerate(fft_spectrum_abs_normalized):
        if f > 0.2:  # looking at amplitudes of the spikes higher than 0.5
            print('frequency = {} Hz with amplitude {} '.format(np.round(freq[i],1), f))

        #The spacing (in Hz) between the peak amplitudes and the difference in heights of the peaks are logged
        amp_diff = 0    #initialize amplitude difference to zero






    #plot
    plt.plot(freq[:11250], fft_spectrum_abs_normalized[:11250])
    plt.xlabel("frequency, Hz")
    plt.ylabel("Amplitude, units")
    plt.title('Frequency FFT :' + file)
    plt.show()





