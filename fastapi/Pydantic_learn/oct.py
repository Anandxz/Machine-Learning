import numpy as np
import matplotlib.pyplot as plt

# Time parameters
dt = 0.01
t = np.arange(-10, 10, dt)

# Unit step u(t)
u = (t >= 0).astype(float)

# Signal x(t) = e^{-3t} u(t)
x = np.exp(-3 * t) * u

# Number of samples
N = len(x)

# FFT
X = np.fft.fft(x)
X = np.fft.fftshift(X) * dt   # CTFT scaling

# Frequency axis
fs = 1 / dt
f = np.arange(-N//2, N//2) * (fs / N)
w = 2 * np.pi * f

# Plot time-domain signal
plt.figure()
plt.plot(t, x)
plt.xlabel('Time (t)')
plt.ylabel('x(t) = e^{-3t}u(t)')
plt.title('Time Domain Signal')
plt.grid(True)

# Plot magnitude of Fourier Transform
plt.figure()
plt.plot(w, np.abs(X))
plt.xlabel('Angular Frequency ω')
plt.ylabel('|X(ω)|')
plt.title('Magnitude of Fourier Transform')
plt.grid(True)

plt.show()
