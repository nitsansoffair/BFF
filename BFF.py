import numpy as np

# Initialize an array of random sensor signals
sensor_signals = np.random.rand(10, 1000)

# Perform FFT on each sensor signal
fft_sensor_signals = np.fft.fft(sensor_signals, axis=1)

# Multiply each sensor signal's FFT by a phase shift factor
phase_shift_factor = np.exp(1j * np.random.rand(10, 1000))
shifted_fft_sensor_signals = fft_sensor_signals * phase_shift_factor

# Sum the phase-shifted sensor signals
summed_signal = np.sum(shifted_fft_sensor_signals, axis=0)

# Perform inverse FFT on the summed signal
inverse_fft_summed_signal = np.fft.ifft(summed_signal)

# Result
print(inverse_fft_summed_signal)