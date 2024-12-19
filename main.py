import matplotlib.pyplot as plt
import numpy as np
fs = 100
k = np.arange(0,1,1/fs)
f = 0.25+2*np.sin(2*np.pi*5*k)+np.sin(2*np.pi*12.5*k)+1.5*np.sin(2*np.pi*20*k)+0.5*np.sin(2*np.pi*35*k)
w = np.fft.fftfreq(len(f), d=1/fs)
F = np.fft.fft(f)

plt.figure(figsize=(10, 6))
# Original Signal
plt.subplot(3, 1, 1)
plt.plot(k, f)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title('Original Signal')

# Magnitude Spectrum
plt.subplot(3, 1, 2)
plt.plot(w, np.abs(F))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude Spectrum')
# Magnitude Spectrum
plt.subplot(3, 1,3)
plt.plot(w, np.unwrap(np.angle(F)))
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Magnitude Spectrum')

plt.tight_layout()
plt.show()